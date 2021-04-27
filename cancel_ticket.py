import psycopg2
# from multiple_booking_ticket import MultipleBooking
from train_search import Search


DB_Host = "localhost"
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "password"

conn = psycopg2.connect(
    host=DB_Host,
    database=DB_name,
    user=DB_user,
    password=DB_pass)
cur = conn.cursor()


class CancelTicket(Search):
    def __init__(self, pnr_no):
        self.pnr_no = pnr_no
        
    def get_cancel_ticket(self):
        
        print("Pnr_no:", self.pnr_no)
        incrementby1 = 1
        cur.execute(
            "select * from passenger_details where pnr_number = %s", ([self.pnr_no]))
        self.rows = list(cur.fetchone())
        print(self.rows)
        print(type(self.rows))
        print("train no:", self.rows[7])

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
                self.rows2[5], incrementby1, self.rows[7]
            ]))
        conn.commit()
        print("Your Ticket is  Cancelled!!!")
        print("ThankYou !! Visit Again!! ")
        return self.pnr_no

'''
ticket_cancel = CancelTicket(1618944043898834)
ticket_cancel.get_cancel_ticket()

print("cur is closed")
cur.close()
print("conn is closed")
conn.close()
'''