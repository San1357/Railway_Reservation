from flask import Flask, jsonify, request
import json
from book_ticket import Ticket


app = Flask(__name__)


@app.route('/')
def hello():
    print("Welcome")


@app.route('/booking', methods=['POST'])
def booking():

    if request.method == "POST":
        req_json = request.json
        name = req_json['Name']
        print(name)
        age = req_json['Age']
        print(age)
        email = req_json['Email']
        print(email)
        aadhaar_no = req_json['Aadhaar_no']
        print(aadhaar_no)
        booking_class = req_json['booking_class']
        print(booking_class)
        train_no = req_json['train_no']
        print(train_no)
        from_station = req_json['from_station']
        print(from_station)
        to_station = req_json['to_station']
        print(to_station)
        date = req_json['date']
        print(date)
        no_of_seat_for_booking = req_json['no_of_seat_for_booking']
        print(no_of_seat_for_booking)
        

        ticket_object = Ticket(
            name,
            age,
            email,
            aadhaar_no,
            booking_class,
            train_no,
            from_station,
            to_station,
            date,
            no_of_seat_for_booking)
        ticket_object.booking_ticket()
        no_of_seat_booked = ticket_object.seat_booking()
        print(str(no_of_seat_booked))
        pnr_number = ticket_object.pnr_generator()
        print(str(pnr_number))
        return jsonify({"Your PNR number number is ": str(pnr_number),
                        "no. Of seat you booked": str(no_of_seat_booked),
                        "status": True})


if __name__ == "__main__":
    app.run(debug=True)
