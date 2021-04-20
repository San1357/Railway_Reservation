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

        print("-----------passenger_details(list_of_tuple-------------------")
        self.passenger_detail_list_of_tuple = []

        for i in self.passenger_details:

            self.passenger_detail_tuple = (i['name'], i['email'], i['age'], i['aadhaar_no'], self.from_station, self.to_station, self.booking_class, self.train_no)
            print(self.passenger_detail_tuple)
            print(type(self.passenger_detail_tuple))
            # list of tuple
            self.passenger_detail_list_of_tuple.append(self.passenger_detail_tuple)

        print("-----------------final list ---------------")
        print("Passenger_detail_list:", self.passenger_detail_list_of_tuple)
        print(type(self.passenger_detail_list_of_tuple))


    def get_available_seat(self):
        self.avail_seat = 0
        cur.execute("select * from traindetail where train_no = %s", ([
            self.train_no]))
        self.rows = list(cur.fetchone())
        self.avail_seat = self.rows[5]
        print("available seat:", self.avail_seat)
        return self.avail_seat

    def update_traindetail(self):
        cur.execute("update traindetail set avail_seat = %s where train_no = %s", (
            self.avail_seat, self.train_no))

        conn.commit()

    def pnr_generator(self):
        ct = datetime.datetime.now()

        self.pnr_list_value_as_tuple = ()
        self.pnr_list_value = []
        self.pnr = int((ct.timestamp() * 1000000))

        for b in range(0, self.no_of_seat):
            b = (b + self.pnr)
            emptytuple = ()
            self.pnr_list_value_as_tuple = emptytuple + (b,)
            print("wer:", self.pnr_list_value_as_tuple)
            self.pnr_list_value.append(self.pnr_list_value_as_tuple)
            print("b:", self.pnr_list_value)

        print("asd:", self.pnr_list_value)
        print(self.pnr_list_value)
        print("Your PNR NUMBER IS:", self.pnr_list_value)

    def update_passenger_info(self):
        for t in range(0, self.no_of_seat):
            print("t:", t)
            self.passenger_detail_list_of_tuple[t] = self.passenger_detail_list_of_tuple[t] + self.pnr_list_value[t]
        print("append_both:", self.passenger_detail_list_of_tuple)

    def book_seat(self):
        pass

    def create_response(self):
        pass
