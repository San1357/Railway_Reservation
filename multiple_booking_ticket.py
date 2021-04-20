import datetime
import psycopg2
import psycopg2.extras


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


class MultipleBooking:

    def parsing(self):
        self.no_of_seat = 0
        self.train_no = 0
        self.passenger_detail_list = []

        self.request = {
            "train_no": 12110,
            "no_of_seat": 3,
            "booking_class": "General",
            "from_station": "Noida",
            "to_station": "Gorakhpur",
            "date": "12-03-2021",
            "passenger":
                    [

                        {
                            "name": "brijesh",
                            "email": "brijesh105@gmail.com",
                            "age": 19,
                            "aadhaar_no": 1300219,
                        },
                        {
                            "name": "vinuj",
                            "email": "vinuj123@gmail.com",
                            "age": 19,
                            "aadhaar_no": 1972192,
                        },
                        {
                            "name": "sidhu",
                            "email": "sidhu123@gmail.com",
                            "age": 19,
                            "aadhaar_no": 1972152,
                        },
                    ]
        }
        self.passenger_details = self.request['passenger']
        print("passenger:", self.passenger_details)
        self.train_no = self.request['train_no']
        self.no_of_seat = self.request['no_of_seat']
        self.booking_class = self.request['booking_class']
        self.from_station = self.request['from_station']
        self.to_station = self.request['to_station']
        print("--------------------------------")
        print(self.train_no)
        print(self.no_of_seat)
        print(self.booking_class)
        print(self.from_station)
        print(self.to_station)


        
    def get_available_seat(self):
        pass

    def update_traindetail(self):
        pass

    def pnr_generator(self):
        pass

    def update_passenger_info(self):
        pass

    def book_seat(self):
        pass

    def create_response(self):
        pass
