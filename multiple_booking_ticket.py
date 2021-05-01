import datetime
from flask import jsonify
from database import Database


class MultipleBooking:
    def __init__(self):
        self.db = Database()


    def parsing(self, req_json):
        self.request = {}
        self.no_of_seat = 0
        self.train_no = 0
        self.passenger_detail_list = []
        self.request = req_json

        self.passenger_details = self.request['passenger']
        print("passenger:", self.passenger_details)
        self.train_no = self.request['train_no']
        self.no_of_seat = self.request['no_of_seat']
        self.booking_class = self.request['booking_class']
        self.from_station = self.request['from_station']
        self.to_station = self.request['to_station']
        print("--------------------------------")
        print("Train_no:", self.train_no)
        print("Data Type of Train_no:", type(self.train_no))
        print("no of Seat :", self.no_of_seat)
        print("Booking Class:", self.booking_class)
        print("From Station:", self.from_station)
        print("To Station:", self.to_station)

        print("-----------passenger_details(list_of_tuple)-------------------")
        self.passenger_detail_list_of_tuple = []

        for i in self.passenger_details:

            self.passenger_detail_tuple = (i['name'], i['email'], i['age'], i['aadhaar_no'], self.from_station, self.to_station, self.booking_class, self.train_no)
            print("Passenger detail:", self.passenger_detail_tuple)
            print("Data type of Passenger detail:", type(self.passenger_detail_tuple))
            # list of tuple
            self.passenger_detail_list_of_tuple.append(self.passenger_detail_tuple)

        print("-----------------final list ---------------")
        print("Passenger_detail_list:", self.passenger_detail_list_of_tuple)
        print(type(self.passenger_detail_list_of_tuple))

    def get_available_seat(self):
        self.avail_seat = 0
        self.rows = self.db.get_DB_avail_seats(self.train_no)
        self.avail_seat = self.rows[5]
        print("available seat:", self.avail_seat)
        return self.avail_seat

    def update_traindetail(self):
        self.db.update_DB_train_detail(self.avail_seat, self.train_no)

    def pnr_generator(self):
        ct = datetime.datetime.now()

        self.pnr_list_value_as_tuple = ()
        self.pnr_list_value = []
        self.pnr = int((ct.timestamp() * 1000000))

        for b in range(0, self.no_of_seat):
            b = (b + self.pnr)
            emptytuple = ()
            self.pnr_list_value_as_tuple = emptytuple + (b,)
            print("PNR Number(in tuple form):", self.pnr_list_value_as_tuple)
            self.pnr_list_value.append(self.pnr_list_value_as_tuple)
            print("Pnr Number:", self.pnr_list_value)

        print("Pnr Number(in List of tuple form) :", self.pnr_list_value)
        print(self.pnr_list_value)
        print("Your PNR NUMBER IS:", self.pnr_list_value)

    def update_passenger_info(self):
        for t in range(0, self.no_of_seat):
            self.passenger_detail_list_of_tuple[t] = self.passenger_detail_list_of_tuple[t] + self.pnr_list_value[t]
        print("Passenger detail(including Pnr number):", self.passenger_detail_list_of_tuple)
        self.db.update_passengerdetail(self.passenger_detail_list_of_tuple)

    def book_seat(self):
        self.get_available_seat()

        if self.no_of_seat < self.avail_seat:
            self.avail_seat = self.avail_seat - self.no_of_seat
            self.update_traindetail()
            self.pnr_generator()
            self.update_passenger_info()
            self.status = "True"
            return self.no_of_seat
        else:
            self.status = "False"

    def create_response(self):
        if self.status == "True":
            a = 0
            result = {
                "status": "booked",
                "no_of_seat_booked": str(self.no_of_seat)
            }

        elif self.status == "False":
            result = {
                "status": "not booked",
                "no_of_seat_booked": str(a)
            }
        print(result)
        return jsonify(result)


if __name__ == "__main__":
    ticket_booking_object = MultipleBooking()
    ticket_booking_object.parsing()
    ticket_booking_object.get_available_seat()
    ticket_booking_object.update_traindetail()
    ticket_booking_object.pnr_generator()
    ticket_booking_object.update_passenger_info()
    ticket_booking_object.book_seat()
    ticket_booking_object.create_response()
