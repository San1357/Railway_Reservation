import math
import random 
import psycopg2
import psycopg2.extras 
from book_ticket import Ticket
from train_search import Search


DB_Host = "127.0.0.1" 
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"

conn = psycopg2.connect(host = DB_Host, database = DB_name, user = DB_user, password = DB_pass)
cur = conn.cursor()

class CancelTicket(Ticket,Search):
    def __init__(self,pnr_no):
        self.pnr_no = pnr_no
        #super(Cancel_ticket, self).__init__(pnr)

    def get_cancel_ticket(self):
       
        #self.Pnrgenerator()
        print("Pnr_no:",self.pnr_no)
        
        cur.execute("delete from traininfo where pnr_number in (%s)",([self.pnr_no]))       
        #cur.execute("update traindetail set avail_seat = %s where train_no = %s",(self.no_of_Seat_u_wanna_book + self.info[5],self.train_no))
        conn.commit()
        print("Your Ticket is  Cancelled!!!")
        print(" ThankYou !! Visit Again!! ")
        return self.pnr_no
        
'''c = CancelTicket(16171998977)
c.get_cancel_ticket()

print("cur is closed")
cur.close()
print("conn is closed")
conn.close() 
'''