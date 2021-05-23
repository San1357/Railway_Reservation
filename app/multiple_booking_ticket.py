import datetime
from flask import jsonify
from database import Database

import uuid

req_json = {
            "train_no": 12110,
            "no_of_seat": 1,
            "passenger":
                        [

                            {
                                "name": "adii",
                                "email": "adii105@gmail.com",
                                "age": 19,
                                "aadhaar_no": 123455
                            }
                        ]
            }


class MultipleBooking:
    def __init__(self):
        self.db = Database()

    def parsing(self, req_json):
        request = {}
        self.no_of_seat = 0
        self.train_no = 0
        request = req_json

        passenger_details = request['passenger']
        self.train_no = request['train_no']
        self.no_of_seat = request['no_of_seat']
        print("passenger:", passenger_details)
        print("--------------------------------")
        print("Train_No:", self.train_no)
        print("Data Type of Train_no:", type(self.train_no))
        print("no of Seat :", self.no_of_seat)

        print("-----------passenger_details(list_of_tuple)-------------------")
        passenger_detail_list_of_tuple = []
        for pass_detail in passenger_details:

            name = pass_detail['name']
            age = pass_detail['age']
            email = pass_detail['email']
            aadhaar_no = pass_detail['aadhaar_no']
            check_data = [(name, age, email, aadhaar_no,)]
            print('name:', name, 'age : ', age, 'email:', email, 'aadhaar_no:', aadhaar_no)
            print("check_data:", check_data)

            is_present, self.uuid = self.db.check_person_is_present(name, age, email, aadhaar_no)

            if is_present:
                passenger_record = self.db.select_all_from_user_details(self.uuid)
                passenger_detail_list_of_tuple.append(passenger_record)
                print("UUID exist", self.uuid)
                print("is_present:", is_present)
                print("passenger_record:", passenger_record)
            else:
                self.uuid = self.db.generate_uuid_for_user_details()
                passenger_details_tuple = self.uuid + (name, age, email, aadhaar_no,)
                passenger_detail_list_of_tuple.append(passenger_details_tuple)
                self.db.insert_records_in_user_detail(passenger_detail_list_of_tuple)
                print("created uuid for new passenger_record", self.uuid)
                print("passenger_detail_tuple :", passenger_details_tuple)
                print("Data type of Passenger detail:", type(passenger_details_tuple))

            print("is_present:", is_present, "UUID: ", self.uuid)
            print("-----------------final list ---------------")
        print("Passenger_detail_list:", passenger_detail_list_of_tuple)
        print(type(passenger_detail_list_of_tuple))

    def get_available_seat(self):
        self.avail_seat = 0
        train_details = self.db.get_avail_seats_using_train_no(self.train_no)
        self.avail_seat = train_details[5]
        print("available seat:", self.avail_seat)
        self.avail_seat

    def update_traindetail(self):
        self.db.update_available_seat_in_train_detail(self.avail_seat, self.train_no)

    def pnr_generator(self):
        ct = datetime.datetime.now()

        pnr_list_value_as_tuple = ()
        self.pnr_list_value = []
        generating_pnr = int((ct.timestamp() * 1000000))

        for pnr in range(0, self.no_of_seat):
            emptytuple = ()
            pnr = (pnr + generating_pnr)
            pnr_list_value_as_tuple = emptytuple + (pnr,)
            self.pnr_list_value.append(pnr_list_value_as_tuple)
            print("generated pnr:", pnr)
            print("PNR Number(in tuple form):", pnr_list_value_as_tuple)

        print("Pnr Number(in List of tuple form) :", self.pnr_list_value)
        print("Your PNR NUMBER IS:", self.pnr_list_value)

    def booking_ticket(self):
        u_id = []
        uu_id = ()
        self.db.insert_pnr_details(self.pnr_list_value)
        train_id = self.db.get_train_id_from_traindetails(self.train_no)
        pnr_id = self.db.get_pnr_id_from_pnr_details(self.pnr_list_value)
        uu_id = (self.uuid,) + train_id + pnr_id
        u_id.append(uu_id)
        self.db.insert_booking_details_database(u_id)
        print("Train_id:", train_id)
        print("type of Train_id:", type(train_id))
        print(":PNR_ID", pnr_id)
        print("type of PNR_ID", type(pnr_id))
        print("PASSENGER_ID:", self.uuid)
        print("type of PASSENGER_ID:", type(uuid,))
        print("uuid:", uu_id)
        print("U_id:", u_id)

    def book_seat(self):
        self.get_available_seat()

        if self.no_of_seat < self.avail_seat:
            self.avail_seat = self.avail_seat - self.no_of_seat
            self.update_traindetail()
            # self.pnr_generator()
            # self.update_passenger_info()
            self.status = "True"
            self.no_of_seat
        else:
            self.status = "False"

    def create_response(self):
        if self.status == "True":
            # a = 0
            result = {
                "status": "booked",
                "no_of_seat_booked": str(self.no_of_seat)
            }

        elif self.status == "False":
            result = {
                "status": "not booked",
                "no_of_seat_booked": str(0)
            }
        print(result)
        return jsonify(result)


if __name__ == "__main__":
    ticket_booking_object = MultipleBooking()
    ticket_booking_object.parsing(req_json)
    ticket_booking_object.get_available_seat()
    ticket_booking_object.update_traindetail()
    ticket_booking_object.pnr_generator()
    ticket_booking_object.booking_ticket()
    ticket_booking_object.book_seat()
    ticket_booking_object.create_response()
