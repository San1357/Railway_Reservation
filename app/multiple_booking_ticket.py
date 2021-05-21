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
        