import psycopg2
import datetime
import uuid
myuuid = uuid.uuid4()


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
        db_host = "localhost"
        db_name = "myfirstdatabase"
        db_user = "postgres"
        db_pass = "password"

        self.conn = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_pass)
        self.cur = self.conn.cursor()

    def get_all_from_train_details(self, fromstation, tostation):
        self.cur.execute(
            "select * from Train_details where from_station = %s and to_station = %s",
            (fromstation, tostation))
        train_details = list(self.cur.fetchone())
        # print(Train_details)
        return train_details

    def get_train_uuid_from_traindetails(self, train_no):
        self.cur.execute("select t_id from Train_details where train_no = %s", ([train_no]))
        train_uuid = (self.cur.fetchone())
        print("Train_id:", train_uuid)
        return train_uuid

    def get_pnr_uuid_from_pnr_details(self, pnr_list_value):
        self.cur.execute("select pnr_id from pnr_details where pnr_number = %s", pnr_list_value)
        pnr_uuid = (self.cur.fetchone())
        print("pnr_id:", pnr_uuid)
        return pnr_uuid

    def generate_uuid_for_user_details(self):
        self.cur.execute("SELECT uuid_generate_v4(); ")
        generated_passenger_uuid = self.cur.fetchone()
        print("------------generating_passenger_uid----------")
        print("generate_passenger_uid:", generated_passenger_uuid)
        return generated_passenger_uuid

    def get_avail_seats_using_train_no(self, train_no):
        self.cur.execute("select * from Train_details where train_no = %s", ([
            train_no]))
        getting_all_from_train_details = list(self.cur.fetchone())
        avail_seat = getting_all_from_train_details[5]
        print("avail_seat:", avail_seat)
        return avail_seat

    def update_available_seat_in_train_details(self, avail_seat, train_no):
        self.cur.execute("update Train_details set avail_seats = %s where train_no = %s", (
            avail_seat, train_no))
        self.conn.commit()

    def insert_records_in_user_detail(self, passenger_detail_list_of_tuple):
        self.cur.executemany("insert into user_details(passenger_uid, name, age, email, aadhaar_no)values(%s, %s,%s, %s, %s)", passenger_detail_list_of_tuple)
        self.conn.commit()

    def insert_records_in_pnr_details(self, pnr_list_value):
        self.cur.execute("insert into pnr_details(pnr_id, pnr_number) values(uuid_generate_v4(), %s)", (pnr_list_value))
        self.conn.commit()

    def insert_records_in_booking_details(self, U_id):
        self.cur.executemany("insert into booking_details(passenger_uid, t_id, pnr_id) values(%s, %s, %s)", U_id)
        self.conn.commit()

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
        """, (name, age, email, aadhaar_no))
        passenger_record = self.cur.fetchone()

        print("passenger_record: ", passenger_record)

        if passenger_record is None:
            uuid = None
            is_present = False
        else:
            is_present = True
            uuid, name, age, email, aadhaar_no = passenger_record

        return is_present, uuid

    def all_from_pnr_details(self, pnr_no):
        self.cur.execute("select * from pnr_details where pnr_number = %s", (pnr_no))
        pnr_details_info = self.cur.fetchone()
        print(pnr_details_info)
        empty = []
        if pnr_details_info is None:
            print("Pnr_details_info", empty)
            return empty
        else:
            print("pnr_details_info:", pnr_details_info)
            return pnr_details_info

    def all_from_booking_details(self, pnr_uuid):
        self.cur.execute("select * from booking_details where pnr_id = %s", ([pnr_uuid]))
        booking_details_info = list(self.cur.fetchone())
        print("booking_details_info:", booking_details_info)
        return booking_details_info

    def all_from_train_details(self, train_uuid):
        self.cur.execute("select * from train_details where t_id = %s", ([train_uuid]))
        train_details_record = list(self.cur.fetchone())
        print("train_details_record:", train_details_record)
        return train_details_record

    def delete_row_from_booking_details(self, pnr_uuid):
        self.cur.execute(
            "delete from booking_details where pnr_id in (%s)", ([
                pnr_uuid]))
        self.conn.commit()

    def delete_row_from_pnr_details(self, pnr_uuid):
        self.cur.execute(
            "delete from pnr_details where pnr_id in (%s)", ([
                pnr_uuid]))
        self.conn.commit()

    def update_seats_in_train_details(self, avail_seat, train_uuid):
        incrementby1 = 1
        self.cur.execute(
            "update train_details set avail_seats = %s + %s where t_id = %s", ([
                avail_seat, incrementby1, train_uuid
            ]))
        self.conn.commit()

    def pnr_of_pnr_status(self, pnr_nos):

        self.cur.execute(
            "select status, pnrpresentstatus from pnr_store where pnr_no = %s;", (pnr_nos,))

        pnr_status = self.cur.fetchone()
        print("pnr status:", pnr_status)
        return pnr_status


if __name__ == "__main__":

    U_id = [('b6f9bcd7-400a-4b7e-a21b-b87c6f8e77fc', 'b6a936d9-6dfe-4d26-81df-c7912140e3ca', 'c8758945-f378-45d4-95bb-33d64df413af')]
    uuid = 'b6f9bcd7-400a-4b7e-a21b-b87c6f8e77fc'
    db = Database()
    db.get_all_from_train_details("gkp", "pune")
    db.get_train_uuid_from_traindetails(12110)
    db.get_pnr_uuid_from_pnr_details([(1621751452546704,)])
    db.generate_uuid_for_user_details()
    db.get_avail_seats_using_train_no(12110)
    db.update_available_seat_in_train_details(45, 12110)
    db.insert_records_in_user_detail([(str(myuuid), 'sunovada', 19, 'sunovada21@gmail.com', 821952,)])
    db.insert_records_in_pnr_details([(43073875292983,)])
    db.insert_records_in_booking_details(U_id)
    db.select_all_from_user_details(uuid)
    db.check_person_is_present('san', 19, 'san21@gmail.com', 983452)
    db.all_from_pnr_details(1621751452546704)
    db.all_from_booking_details('c8758945-f378-45d4-95bb-33d64df413af')
    db.all_from_train_details('b6a936d9-6dfe-4d26-81df-c7912140e3ca')
    # db.delete_row_from_user_details(1621751683964907)
    db.delete_row_from_booking_details('e2ee6000-30cc-4adc-9dba-c268297fae0c')
    db.delete_row_from_pnr_details('e2ee6000-30cc-4adc-9dba-c268297fae0c')
    db.update_seats_in_traindetail(45, 'b6a936d9-6dfe-4d26-81df-c7912140e3ca')
    # db.pnr_of_pnr_status(7934082101)
