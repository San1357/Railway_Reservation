import datetime

import psycopg2
import psycopg2.extras
from TrainSearch import Search

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


class Ticket(Search):
    def __init__(
            self,
            name,
            age,
            email,
            aadhaar_no,
            booking_class,
            train_no,
            from_station,
            to_station,
            date,
            no_of_seat_for_booking):
        self.name = name
        self.age = age
        self.email = email
        self.aadhaar_no = aadhaar_no
        self.booking_class = booking_class
        self.train_no = train_no
        super(Ticket, self).__init__(from_station, to_station, date)
        self.no_of_seat_for_booking = no_of_seat_for_booking

    def booking_ticket(self):
        print("NAME: ", self.name)
        print("AGE:", self.age)
        print("EMAIL:", self.email)
        print("AADHAAR_NO:", self.aadhaar_no)
        print("BOOKING_CLASS", self.booking_class)
        print("TRAIN NO:", self.train_no)
        print("no_of_seat_for_booking:", self.no_of_seat_for_booking)
        List1 = []
        List1.append(self.name)
        List1.append(self.age)
        List1.append(self.email)
        List1.append(self.aadhaar_no)
        List1.append(self.from_station)
        List1.append(self.to_station)
        List1.append(self.booking_class)
        List1.append(self.train_no)
        pas = List1.copy()
        pas_set = (List1)
        print(pas)
        print(pas_set)
        cur.execute(
            "insert into TrainInfo (name, age, email, aadhaar_no, fromstation, tostation, Class, train_no)values(%s, %s, %s, %s, %s, %s, %s, %s)",
            (pas))
        conn.commit()
        print("Record of Pasenger inserted!!")

    def seat_booking(self):
        self._train_search()

        print("Hello world ", self.info)
        self.get_train_details()

        if self.no_of_seat_for_booking <= self.info[5]:
            print("Congratulations!!")
            print("You got ur seats book:", self.no_of_seat_for_booking)
            self.info[5] = self.info[5] - self.no_of_seat_for_booking
            cur.execute(
                "update traindetail set avail_seat = %s where fromstation = %s and tostation = %s",
                (self.info[5],
                 self.from_station,
                 self.to_station))
            conn.commit()
            count = self.no_of_seat_for_booking
            print(count, "success")
            print("Now, Total no. of Seats available:", self.info[5])
            return count
            '''result = {
                "status": True,
                "no.Of Seat Booked": count,
                "Total no.Of Seat available": self.info[5]
            }'''

        if self.no_of_seat_for_booking > self.info[5]:
            print("Sorry We don't have this no. of seat available.")
            print(
                "We have only",
                self.info[5],
                "no . of seat available. ThankYou!!!")
            count1 = 0
            return count1

            '''result = {
                "Status": False,
                "no. of seat Booked": "not enough seat available",
                "Total no. Of Seat available": self.info[5]
            }'''

    def pnr_generator(self):
        ct = datetime.datetime.now()
        self.pnr = int(ct.timestamp() * 10)

        cur.execute(
            "update TrainInfo set pnr_number = %s where aadhaar_no = %s",
            (self.pnr,
             self.aadhaar_no))

        conn.commit()
        print("Your PNR NUMBER IS:", (self.pnr))
        return(self.pnr)


'''a = Ticket("diya", 19, "diya105@gmail.com", 130409, "Gkp", "kanpur","General", 1000409,"Gorakhpur","Pune","12-03-2021")
print("------------ a.BOooking_ticket --------------")
a.Booking_Ticket()
print("-------------a.Seat_booking ------------")
a.seat_booking()
print("-----a.Pnrgenerator----------")
a.Pnrgenerator()
print("cur is closed")
cur.close()
print("conn is closed")
conn.close()'''
