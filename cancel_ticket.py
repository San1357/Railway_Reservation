import psycopg2
from book_ticket import Ticket
from train_search import Search


DB_Host = "127.0.0.1"
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"

conn = psycopg2.connect(
    host=DB_Host,
    database=DB_name,
    user=DB_user,
    password=DB_pass)
cur = conn.cursor()


class CancelTicket(Ticket, Search):
    def __init__(self, pnr_no):
        self.pnr_no = pnr_no
        # super(CancelTicket, self).__init__(from_station, to_station, date)
        # self.no_of_seat_for_booking = no_of_seat_for_booking

    def get_cancel_ticket(self):
        # self.train_search()
        # print ("hi:", self.traindetail_info)
        # self.get_train_details()
        print("Pnr_no:", self.pnr_no)
        cur.execute(
            "select * from passenger_details where pnr_number = %s", ([
                self.pnr_no]))
        self.rows = list(cur.fetchone())
        print(self.rows)
        print(type(self.rows))
        print("train no:", self.rows[7])
        print("seat booked ", self.rows[9])

        cur.execute(
            "select * from traindetail where train_no = %s", ([self.rows[7]])
        )
        self.rows2 = list(cur.fetchone())
        print(self.rows2)
        print(type(self.rows2))
        print("avail_seat", self.rows2[5])

        cur.execute(
            "delete from passenger_details where pnr_number in (%s)", ([
                self.pnr_no]))
        cur.execute(
            "update traindetail set avail_seat = %s + %s where train_no = %s", ([
                self.rows2[5], self.rows[9], self.rows[7]
            ]))
        conn.commit()
        print("Your Ticket is  Cancelled!!!")
        print("ThankYou !! Visit Again!! ")
        return self.pnr_no


ticket_cancel = CancelTicket(16183117212)
ticket_cancel.get_cancel_ticket()

print("cur is closed")
cur.close()
print("conn is closed")
conn.close()