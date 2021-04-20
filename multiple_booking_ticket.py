import datetime
import psycopg2
import psycopg2.extras


DB_Host = "127.0.0.1"
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"
h = 0

conn = psycopg2.connect(
    host=DB_Host,
    database=DB_name,
    user=DB_user,
    password=DB_pass)
cur = conn.cursor()


class MultipleBooking:

    def parsing(self):
        pass
    def get_available_seat(self):
        pass

    def update_traindetail(self):
        pass

    def pnr_generator(self):
        pass

    def update_passenger_info(self):
        pass

    def book_seat(self):
        pass

    def create_response(self):
        pass
