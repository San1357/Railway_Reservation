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
            "select * from traindetail where fromstation = %s and tostation = %s",
            (fromstation, tostation))
        e = list(self.cur.fetchone())
        print(e)
        return e

    def get_DB_avail_seats(self, train_no):
        self.cur.execute("select * from traindetail where train_no = %s", ([
            train_no]))
        f = list(self.cur.fetchone())
        self.avail_seat = f[5]
        self.train_no = f[2]
        print("train_no:", self.train_no)
        print("f:",f)
        return f

    def update_DB_train_detail(self, avail_seat, train_no):
        self.cur.execute("update traindetail set avail_seat = %s where train_no = %s", (
            avail_seat, train_no))
        g = self.conn.commit()
        print("g:",g)
        return g

    def update_passengerdetail(self, passenger_detail_list_of_tuple):
        passenger_detail_list_of_tuple
        self.cur.executemany("insert into passenger_details(name, email, age, aadhaar_no, fromstation, tostation, class, train_no, pnr_number)values(%s, %s,%s, %s,%s, %s, %s, %s, %s)", passenger_detail_list_of_tuple)
        h = self.conn.commit()
        return h

    def all_from_passenger_info(self, pnr_no):
        self.cur.execute(
            "select * from passenger_details where pnr_number = %s", ([pnr_no]))
        a = list(self.cur.fetchone())
        print("a:",a)
        return a

    def all_from_train_Details(self, train_no):
        self.cur.execute(
            "select * from traindetail where train_no = %s", ([train_no])
        )
        b = list(self.cur.fetchone())
        print("b:", b)
        return b

    def delete_row_from_passenger_details(self, pnr_no):
        self.cur.execute(
            "delete from passenger_details where pnr_number in (%s)", ([
                pnr_no]))
        c = self.conn.commit()
        return c

    def update_traindetail(self, avail_seat, train_no):
        incrementby1 = 1
        self.cur.execute(
            "update traindetail set avail_seat = %s + %s where train_no = %s", ([
                avail_seat, incrementby1, train_no
            ]))
        o = self.conn.commit()
        return o


if __name__ == "__main__":
    
    pnr_list_value = pnr_generator(1)
    passenger_detail_list_of_tuple = [('jeet', 'jeet105@gmail.com', 19, 1491041, 'Noida', 'Gorakhpur', 'General', 12110,)]
    print(passenger_detail_list_of_tuple)
    print(pnr_list_value)
    passenger_detail_list_of_tuple[0] = passenger_detail_list_of_tuple[0] + pnr_list_value[0]
    db = Database()
    db.get_DB_Train_Details("Gorakhpur", "Pune")
    db.get_DB_avail_seats(12110)
    db.update_DB_train_detail(22, 12110)
    db.update_passengerdetail(passenger_detail_list_of_tuple)
    db.all_from_passenger_info(1619692464584002)
    db.all_from_train_Details(12110)
    db.all_from_passenger_info(1619692464584002)
    db.all_from_train_Details(12110)
    db.delete_row_from_passenger_details(1619692464584002)


    db.update_traindetail(22, 12110)
