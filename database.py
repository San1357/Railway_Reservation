import psycopg2


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
        self.from_station = fromstation
        self.to_station = tostation
        self.cur.execute(
            "select * from traindetail where fromstation = %s and tostation = %s",
            (self.from_station, self.to_station))
        e = list(self.cur.fetchone())
        print(e)
        return e

    def get_DB_avail_seats(self, train_no):
        self.train_no = train_no
        self.cur.execute("select * from traindetail where train_no = %s", ([
            self.train_no]))
        f = list(self.cur.fetchone())
        print(f)
        return f

    def update_DB_train_detail(self, avail_seat, train_no):
        self.avail_seat = avail_seat
        self.train_no = train_no
        self.cur.execute("update traindetail set avail_seat = %s where train_no = %s", (
            self.avail_seat, self.train_no))

        g = self.conn.commit()
        return g

    def update_passengerdetail(self, passenger_detail_list_of_tuple):
        self.passenger_detail_list_of_tuple = passenger_detail_list_of_tuple
        self.cur.executemany("insert into passenger_details(name, email, age, aadhaar_no, fromstation, tostation, class, train_no, pnr_number)values(%s, %s,%s, %s,%s, %s, %s, %s, %s)", self.passenger_detail_list_of_tuple)
        h = self.conn.commit()
        return h

    def all_from_passenger_info(self, pnr_no):
        self.pnr_no = pnr_no
        self.cur.execute(
            "select * from passenger_details where pnr_number = %s", ([self.pnr_no]))
        a = list(self.cur.fetchone())
        return a

    def all_from_train_Details(self, train_no):
        self.train_no = train_no
        self.cur.execute(
            "select * from traindetail where train_no = %s", ([self.train_no])
        )
        b = list(self.cur.fetchone())
        return b


    def delete_row_from_passenger_details(self, pnr_no):
        pass

    def update_traindetail(self, avail_seat, train_no):
        pass


if __name__ == "__main__":
    db = Database()
    db.get_DB_Train_Details()
    db.get_DB_avail_seats()
    db.update_DB_train_detail()
    db.update_passengerdetail()
    db.all_from_passenger_info()
    db.all_from_train_Details()
    db.all_from_passenger_info()
    db.all_from_train_Details()
    db.delete_row_from_passenger_details()
    db.update_traindetail()
