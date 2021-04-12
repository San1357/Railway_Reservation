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

    def get_cancel_ticket(self):
        print("Pnr_no:", self.pnr_no)
        cur.execute(
            "delete from passenger_details where pnr_number in (%s)", ([
                self.pnr_no]))
        conn.commit()
        print("Your Ticket is  Cancelled!!!")
        print(" ThankYou !! Visit Again!! ")
        return self.pnr_no


ticket_cancel = CancelTicket(16171998977)
ticket_cancel.get_cancel_ticket()

print("cur is closed")
cur.close()
print("conn is closed")
conn.close()
