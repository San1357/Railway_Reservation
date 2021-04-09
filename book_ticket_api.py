from flask import Flask, jsonify, request

from book_ticket import Ticket


app = Flask(__name__)


@app.route('/')
def hello():
    print("Welcome")


@app.route('/booking', methods=['POST'])
def booking():
    '''print("Welcome to booking")
    print("NAME: ", name)
    print("AGE:",age)
    print("EMAIL:",email)
    print("AADHAAR_NO:",aadhaar_no)
    print("FROM_STATION:",fromstation)
    print("TOSTATION:",tostation)
    print("CLASS",Class)
    print("TRAIN NO:",train_no)'''

    if request.method == "POST":
        req_Json = request.json
        Name = req_Json['Name']
        print(Name)
        Age = req_Json['Age']
        print(Age)
        Email = req_Json['Email']
        print(Email)
        Aadhaar_no = req_Json['Aadhaar_no']
        print(Aadhaar_no)
        booking_class = req_Json['booking_class']
        print(booking_class)
        train_no = req_Json['train_no']
        print(train_no)
        from_station = req_Json['from_station']
        print(from_station)
        to_station = req_Json['to_station']
        print(to_station)
        date = req_Json['date']
        print(date)
        no_of_seat_for_booking = req_Json['no_of_seat_for_booking']
        print(no_of_seat_for_booking)

        a = Ticket(
            Name,
            Age,
            Email,
            Aadhaar_no,
            booking_class,
            train_no,
            from_station,
            to_station,
            date,
            no_of_seat_for_booking)
        a.booking_ticket()
        e = a.seat_booking()
        print(str(e))
        d = a.pnr_generator()
        print(str(d))
        return jsonify({"Your PNR number number is ": str(d),
                        "no. Of seat you booked": str(e),
                        "status": True})


if __name__ == "__main__":
    app.run(debug=True)
