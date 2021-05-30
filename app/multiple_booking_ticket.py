import datetime
import uuid
from flask import jsonify
from database import Database
db = Database()


req_json = {
            "train_no": 12110,
            "no_of_seat": 1,
            "passenger":
                        [
                            {
                                "name": "adiii",
                                "email": "adiii105@gmail.com",
                                "age": 19,
                                "aadhaar_no": 124465
                            }
                        ]
            }


def pnr_generator(no_of_seat):
    ct = datetime.datetime.now()
    
    pnr_list_in_form_of_tuple = ()#pnr_list_value_as_tuple = ()
    pnr_list = [] #pnr_list_value = []
    generating_pnr = int((ct.timestamp() * 1000000))

    for pnr in range(0, no_of_seat):
        emptytuple = ()
        pnr = (pnr + generating_pnr)
        pnr_list_in_form_of_tuple = emptytuple + (pnr,)
        pnr_list.append(pnr_list_in_form_of_tuple)
        print("generated pnr:", pnr)
        print("PNR Number(in tuple form):", pnr_list_in_form_of_tuple)

    print("Pnr Number(in List of tuple form) :", pnr_list)
    print("Your PNR NUMBER IS:", pnr_list)
    return pnr_list



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

    def is_passenger_detail_exist(self): 

        print("-----------passenger_details(list_of_tuple)-------------------")
        passenger_detail_list_of_tuple = []
        for pass_detail in passenger_details:

            name = pass_detail['name']
            age = pass_detail['age']
            email = pass_detail['email']
            aadhaar_no = pass_detail['aadhaar_no']
            print('name:', name, 'age : ', age, 'email:', email, 'aadhaar_no:', aadhaar_no)

            is_passenger_detail_present, self.passenger_uuid = self.db.check_person_is_present(name, age, email, aadhaar_no)

            if is_passenger_detail_present:
                passenger_record = self.db.select_all_from_user_details(self.passenger_uuid)
                passenger_detail_list_of_tuple.append(passenger_record)
                print("UUID exist", self.passenger_uuid)
                print("is_present:", is_passenger_detail_present)
                print("passenger_record:", passenger_record)
            else:
                self.passenger_uuid = self.db.generate_uuid_for_user_details()
                passenger_details_in_form_of_tuple = self.passenger_uuid + (name, age, email, aadhaar_no,)
                passenger_detail_list_of_tuple.append(passenger_details_in_form_of_tuple)
                self.db.insert_records_in_user_detail(passenger_detail_list_of_tuple)
                print("created uuid for new passenger_record", self.passenger_uuid)
                print("passenger_detail_in_form_of_tuple :", passenger_details_in_form_of_tuple)
                print("Data type of Passenger detail:", type(passenger_details_in_form_of_tuple))

            print("is_present:", is_passenger_detail_present, "UUID: ", self.passenger_uuid)
            print("-----------------final list ---------------")
        print("Passenger_detail_list:", passenger_detail_list_of_tuple)
        print(type(passenger_detail_list_of_tuple))

    def booking_ticket(self):
        u_id = []
        uu_id = ()
        self.pnr_list = pnr_generator(self.no_of_seat)
        self.db.insert_records_in_pnr_details(self.pnr_list)
        train_uuid = self.db.get_train_id_from_traindetails(self.train_no)
        pnr_uuid = self.db.get_pnr_id_from_pnr_details(self.pnr_list)
        uu_id = (self.passenger_uuid,) + train_id + pnr_id
        u_id.append(uu_id)
        self.db.insert_records_in_booking_details(u_id)
        print("-------- TRAIN_UUID --------")
        print("Train_UUID:", train_id)
        print("type of Train_UUID:", type(train_uuid))
        print("-------- PNR_UUID --------")
        print(":PNR_UUID", pnr_id)
        print("type of PNR_UUID", type(pnr_uuid))
        print("-------- PASSENGER_UUID --------")
        print("PASSENGER_UUID:", self.passenger_uuid)
        print("type of PASSENGER_UUID:", type(self.passenger_uuid,))
        print("uuid:", uu_id)
        print("U_id:", u_id)

    def book_seat(self):

        self.avail_seat = self.db.get_avail_seats_using_train_no(self.train_no)
        print("available seat:", self.avail_seat)

        if self.no_of_seat < self.avail_seat:
            self.avail_seat = self.avail_seat - self.no_of_seat
            self.db.update_available_seat_in_train_details(self.avail_seat, self.train_no)

            # self.pnr_generator()
            # self.update_passenger_info()
            self.status = "True"
            self.no_of_seat
        else:
            self.status = "False"

    def get_avail_seat(self):
        self.message = "sorry this no of seat is not available. so, we cant book any seat."
        message2 = "Welcome! You are In."
        self.avail_seat = db.get_avail_seats_using_train_no(self.train_no)


    def create_response(self):

        if self.status_two:
            if self.status == "True":
                result = {
                    "status": "booked",
                    "no of seat booked": str(self.no_of_seat)
                }

            elif self.status == "False":
                result = {
                    "status": "not booked",
                    "no of seat booked": str(0)
                }
            print(result)
            #return jsonify(result)
        else:
            
            result = {
                "no of seat you want": str(self.no_of_seat),
                "seat available": str(self.avail_seat),
                "status": self.message,
                "no of seat booked": str(0)
            }
            print(result)

    def main_funcn(self, req_json):

        self.parsing(req_json)
        avail_seat = db.get_avail_seats_using_train_no(self.train_no)

        self.status_two = False
        if self.no_of_seat <= avail_seat:
            self.is_passenger_detail_exist()
            self.booking_ticket()
            self.book_seat()
            self.status_two = True
        else:
            self.get_avail_seat()
        self.create_response_mod()


if __name__ == "__main__":
    ticket_booking_object = MultipleBooking()
    ticket_booking_object.main_funcn_mod_mod(req_json)
