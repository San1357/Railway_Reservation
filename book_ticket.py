import datetime

import psycopg2
import psycopg2.extras
from train_search import Search

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
        passenger_detail_list = []
        passenger_detail_list.append(self.name)
        passenger_detail_list.append(self.age)
        passenger_detail_list.append(self.email)
        passenger_detail_list.append(self.aadhaar_no)
        passenger_detail_list.append(self.from_station)
        passenger_detail_list.append(self.to_station)
        passenger_detail_list.append(self.booking_class)
        passenger_detail_list.append(self.train_no)
        print(passenger_detail_list)
        cur.execute(
            "insert into passenger_details (name, age, email, aadhaar_no, fromstation, tostation, Class, train_no)values(%s, %s, %s, %s, %s, %s, %s, %s)",
            (passenger_detail_list))
        conn.commit()
        print("Record of Pasenger inserted!!")

    def seat_booking(self):
        self.train_search()

        print("Hello world ", self.traindetail_info)
        self.get_train_details()

        seat_booked = 0
        if self.no_of_seat_for_booking <= self.traindetail_info[5]:
            print("Congratulations!!")
            print("You got ur seats book:", self.no_of_seat_for_booking)
            self.traindetail_info[5] = self.traindetail_info[5] - self.no_of_seat_for_booking
            cur.execute(
                "update traindetail set avail_seat = %s where fromstation = %s and tostation = %s",
                (self.traindetail_info[5],
                 self.from_station,
                 self.to_station))
            conn.commit()
            seat_booked = self.no_of_seat_for_booking
            print(seat_booked, "success")
            print("Now, Total no. of Seats available:", self.traindetail_info[5])
            # return count

        elif self.no_of_seat_for_booking > self.traindetail_info[5]:
            print("Sorry We don't have this no. of seat available.")
            print(
                "We have only",
                self.traindetail_info[5],
                "no . of seat available. ThankYou!!!")
            seat_booked = 0
            # return count1
        
        return seat_booked


    def pnr_generator(self):
        ct = datetime.datetime.now()
        self.pnr = int(ct.timestamp() * 10)

        cur.execute(
            "update passenger_details set pnr_number = %s where aadhaar_no = %s",
            (self.pnr,
             self.aadhaar_no))

        conn.commit()
        print("Your PNR NUMBER IS:", (self.pnr))
        return(self.pnr)

'''
booking_ticket = Ticket("shiya", 19, "shiya105@gmail.com", 1305809, "General", 1000409,"Gorakhpur","Pune","12-03-2021",1)
print("------------ BOooking_ticket --------------")
booking_ticket.booking_ticket()
print("-------------Seat_booking ------------")
booking_ticket.seat_booking()
print("-----Pnrgenerator----------")
booking_ticket.pnr_generator()
print("cur is closed")
cur.close()
print("conn is closed")
conn.close()'''