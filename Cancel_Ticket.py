import math
import random 
import psycopg2
import psycopg2.extras 
from Bookticket4 import Ticket
from TrainSearch import Search


DB_Host = "127.0.0.1" 
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"

conn = psycopg2.connect(host = DB_Host, database = DB_name, user = DB_user, password = DB_pass)
cur = conn.cursor()

class Cancel_ticket(Ticket,Search):
    def __init__(self,Pnr_no):
        self.Pnr_no = Pnr_no
        #super(Cancel_ticket, self).__init__(pnr)

    def get_cancel_ticket(self):
       
        #self.Pnrgenerator()
        print("Pnr_no:",self.Pnr_no)
        
        cur.execute("delete from traininfo where pnr_number in (%s)",([self.Pnr_no]))       
        cur.execute("update traindetail set avail_seat = %s where train_no = %s",(self.no_of_Seat_u_wanna_book + self.info[5],self.train_no))
        conn.commit()
        print("Your Ticket is  Cancelled!!!")
        print(" ThankYou !! Visit Again!! ")
        return self.Pnr_no
        
'''c = Cancel_ticket(16171998977)
c.get_cancel_ticket()

print("cur is closed")
cur.close()
print("conn is closed")
conn.close()'''