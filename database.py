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
        pass

    def update_DB_train_detail(self, avail_seat, train_no):
        pass

    def update_passengerdetail(self, passenger_detail_list_of_tuple):
        pass

    def all_from_passenger_info(self, pnr_no):
        pass

    def all_from_train_Details(self, train_no):
        pass

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
