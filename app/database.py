import psycopg2
import datetime


def pnr_generator(no_of_seat):
    ct = datetime.datetime.now()
    pnr_list_value_as_tuple = ()
    pnr_list_value = []
    pnr = int((ct.timestamp() * 1000000))
    for b in range(0, no_of_seat):
        b = (b + pnr)
        emptytuple = ()
        pnr_list_value_as_tuple = emptytuple + (b,)
        print("PNR Number(in tuple form):", pnr_list_value_as_tuple)
        pnr_list_value.append(pnr_list_value_as_tuple)
        print("Pnr Number:", pnr_list_value)

    print("Pnr Number(in List of tuple form) :", pnr_list_value)
    print(pnr_list_value)
    print("Your PNR NUMBER IS:", pnr_list_value)
    return pnr_list_value


class Database:

    def __init__(self):
        DB_Host = "localhost"
        DB_name = "myfirstdatabase"
        DB_user = "postgres"
        DB_pass = "password"

        self.conn = psycopg2.connect(
            host=DB_Host,
            database=DB_name,
            user=DB_user,
            password=DB_pass)
        self.cur = self.conn.cursor()

    def get_DB_Train_Details(self, fromstation, tostation):
        self.cur.execute(
            "select * from Train_details where from_station = %s and to_station = %s",
            (fromstation, tostation))
        e = list(self.cur.fetchone())
        # print(e)
        return e
    
    def get_trainId_from_traindetails(self, train_no):
        self.cur.execute("select t_id from Train_details where train_no = %s", ([train_no]))
        dt = (self.cur.fetchone())
        print("dt:", dt)
        return dt

    def get_pnr_Id_from_pnr_details(self, pnr_list_value):
        self.cur.execute("select pnr_id from pnr_details where pnr_number = %s", pnr_list_value)
        op = (self.cur.fetchone())
        print("op:", op)
        return op
    

    def set_passenger_uid_for_user_details(self):
        self.cur.execute("SELECT uuid_generate_v4(); ")
        gt = self.cur.fetchone()
        print("------------gt----------")
        print("gt:", gt)
        return gt

    def get_DB_avail_seats(self, train_no):
        self.cur.execute("select * from Train_details where train_no = %s", ([
            train_no]))
        f = list(self.cur.fetchone())
        self.avail_seat = f[5]
        self.train_no = f[3]
        print("train_no:", self.train_no)
        print("f:", f)
        return f

    def update_DB_train_detail(self, avail_seat, train_no):
        self.cur.execute("update Train_details set avail_seats = %s where train_no = %s", (
            avail_seat, train_no))
        g = self.conn.commit()
        print("g:", g)
        return g

    def update_passengerdetail(self, passenger_detail_list_of_tuple ):
        self.cur.executemany("insert into user_details(passenger_uid, name, age, email, aadhaar_no)values(%s, %s,%s, %s, %s)", passenger_detail_list_of_tuple)
        h = self.conn.commit()
        print("h:", h)
        return h

    def update_pnr_details(self, pnr_list_value):
        self.cur.execute("insert into pnr_details(pnr_id, pnr_number) values(uuid_generate_v4(), %s)",(pnr_list_value))
        wrq = self.conn.commit()
        print("wrq:", wrq)
        return wrq

    def booking_details_database(self, U_id):
        self.cur.executemany("insert into booking_details(passenger_uid, t_id, pnr_id) values(%s, %s, %s)", U_id)
        yrq = self.conn.commit()
        print("yrq:", yrq)
        return yrq

    def select_all_from_user_details(self, uuid):
        """
        """
        self.cur.execute("""
        select * from user_details
        where passenger_uid = %s
        """, (uuid,))
        passenger_record = self.cur.fetchone()
        return passenger_record

    def check_person_is_present(self, name, age, email, aadhaar_no):
        """
        """
        self.cur.execute("""
        select * from user_details 
        where name = %s and age = %s and email= %s and aadhaar_no = %s
        """, 
        (name, age, email, aadhaar_no))
        passenger_record = self.cur.fetchone()
        
        print("passenger_record: ", passenger_record)
        
        if passenger_record == None:
            uuid = None
            is_present = False
        else:
            is_present = True
            uuid, name, age, email, aadhaar_no = passenger_record

        return is_present, uuid


    def all_from_passenger_info(self, pnr_no):
        self.cur.execute(
            "select * from user_details where pnr_number = %s", ([pnr_no]))
        a = list(self.cur.fetchone())
        print("a:", a)
        return a

    def all_from_pnr_details(self, pnr_no):
        self.cur.execute("select * from pnr_details where pnr_number = %s", ([pnr_no]))
        eu = list(self.cur.fetchone())
        print("eu:", eu)
        return eu

    def all_from_booking_details(self, pnr_id):
        self.cur.execute("select * from booking_details where pnr_id = %s", ([pnr_id]))
        pu = list(self.cur.fetchone())
        print("pu:", pu)
        return pu
        

    def all_from_train_Details(self, t_id):
        self.cur.execute("select * from train_details where t_id = %s", ([t_id]))
        b = list(self.cur.fetchone())
        print("b:", b)
        return b

    def delete_row_from_passenger_details(self, pnr_no):
        self.cur.execute(
            "delete from user_details where pnr_number in (%s)", ([
                pnr_no]))
        c = self.conn.commit()
        return c

    def delete_row_from_booking_details(self, pnr_id):
        self.cur.execute(
            "delete from booking_details where pnr_id in (%s)", ([
                pnr_id]))
        cu = self.conn.commit()
        return cu

    def delete_row_from_pnr_details(self, pnr_id):
        self.cur.execute(
            "delete from pnr_details where pnr_id in (%s)", ([
                pnr_id]))
        cut = self.conn.commit()
        return cut

    def update_traindetail(self, avail_seat, train_id):
        incrementby1 = 1
        self.cur.execute(
            "update train_details set avail_seats = %s + %s where t_id = %s", ([
                avail_seat, incrementby1, train_id
            ]))
        o = self.conn.commit()
        return o

    def pnr_of_pnr_status(self, pnr_nos):

        self.cur.execute(
            "select status, pnrpresentstatus from pnr_store where pnr_no = %s;", (pnr_nos,))

        pnr_status = self.cur.fetchone()
        print("pnr status:", pnr_status)
        return pnr_status


if __name__ == "__main__":

    pnr_list_value = pnr_generator(1)
    passenger_detail_list_of_tuple = [('jeet', 19, 'jeet105@gmail.com', 1491041, 'f4322e3c-a304-4177-b8c4-56b45b1bdd28', 1619692464584002,)]
    print(passenger_detail_list_of_tuple)
    '''print(pnr_list_value)
    passenger_detail_list_of_tuple[0] = passenger_detail_list_of_tuple[0] + pnr_list_value[0]
    db = Database()
    # db.get_DB_Train_Details("Gorakhpur", "Pune")
    db.get_trainId_from_traindetails(12110)
    db.get_DB_avail_seats(12110)
    db.update_DB_train_detail(22, 12110)'''
    db = Database()    
    db.update_passengerdetail(passenger_detail_list_of_tuple)
    '''db.all_from_passenger_info(1619692464584002)
    db.all_from_train_Details(12110)
    db.all_from_passenger_info(1619692464584002)
    db.all_from_train_Details(12110)
    db.delete_row_from_passenger_details(1619692464584002)
    db.update_traindetail(22, 12110)
    db.pnr_of_pnr_status(7934082101)'''
