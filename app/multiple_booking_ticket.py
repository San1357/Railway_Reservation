import datetime
from flask import jsonify
from database import Database

import uuid
import pprint


req_json = {
            "train_no": 12110,
            "no_of_seat": 1,
            "passenger":
                    [

                        {
                            "name": "wsad",
                            "email": "wsad105@gmail.com",
                            "age": 19,
                            "aadhaar_no": 421479
                        }
                    ]
        }



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
        print("--------------------------------")
        print("Train_No:", self.train_no)
        print("Data Type of Train_no:", type(self.train_no))
        print("no of Seat :", self.no_of_seat)


        print("-----------passenger_details(list_of_tuple)-------------------")
        self.passenger_detail_list_of_tuple = []
        for pass_detail in self.passenger_details:

            name = pass_detail['name']
            age = pass_detail['age']
            email = pass_detail['email']
            aadhaar_no = pass_detail['aadhaar_no']
            print('name:',name, 'age : ', age, 'email:', email, 'aadhaar_no:', aadhaar_no)

            check_data = [(name, age, email, aadhaar_no,)]
            print("check_data:", check_data)

            is_present, self.uuid = self.db.check_person_is_present(name, age, email, aadhaar_no)

            if is_present:
                print("UUID exist", self.uuid)
                print("is_present:", is_present)
                passenger_record = self.db.select_all_from_user_details(self.uuid)
                print("passenger_record:", passenger_record)
                self.passenger_detail_list_of_tuple.append(passenger_record)
            else:
                self.uuid = self.db.set_passenger_uid_for_user_details()
                print("created uuid for new passenger_record",self.uuid)
                self.passenger_details_tuple = self.uuid + (name, age, email, aadhaar_no,)
                print("passenger_detail_tuple :", self.passenger_details_tuple)
                print("Data type of Passenger detail:", type(self.passenger_details_tuple))
                self.passenger_detail_list_of_tuple.append(self.passenger_details_tuple)
                self.db.update_passengerdetail(self.passenger_detail_list_of_tuple)

            print("is_present:", is_present, "UUID: ", self.uuid)
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
            print("b1:", b)
            b = (b + self.pnr)
            print("b2:", b)
            emptytuple = ()
            self.pnr_list_value_as_tuple = emptytuple + (b,)
            print("PNR Number(in tuple form):", self.pnr_list_value_as_tuple)
            self.pnr_list_value.append(self.pnr_list_value_as_tuple)
            print("Pnr Number:", self.pnr_list_value)

        print("Pnr Number(in List of tuple form) :", self.pnr_list_value)
        print("Your PNR NUMBER IS:", self.pnr_list_value)
        self.db.update_pnr_details(self.pnr_list_value)
        Train_Id = self.db.get_trainId_from_traindetails(self.train_no)
        print("Train_id:",Train_Id)
        print("type of Train_id:",type(Train_Id))
        pnr_Id = self.db.get_pnr_Id_from_pnr_details(self.pnr_list_value)
        print(":PNR_ID", pnr_Id)
        print("type of PNR_ID", type(pnr_Id))
        print("PASSENGER_ID:", self.uuid)
        print("type of PASSENGER_ID:", type(uuid,))
        UU_ID = ()
        UU_ID = (self.uuid,) + Train_Id + pnr_Id 
        print(UU_ID)
        self.U_id.append(UU_ID)
        print("U_id:", self.U_id)
        self.db.booking_details_database(self.U_id)

