from flask import Flask, jsonify, request
import json
import pprint

from multiple_booking_ticket import MultipleBooking


app = Flask(__name__)


@app.route('/')
def hello():
    print("Welcome")



@app.route('/multiple_bookings', methods=['POST'])
def multiple_bookings():
    if request.method == "POST":
        req_json = request.json
        pprint.pprint(req_json) # pprint will print your response in response json format.

        ticket_booking = MultipleBooking()
        ticket_booking.parsing(req_json)
        ticket_booking.book_seat()

        response = ticket_booking.create_response()
        
        return response

    

if __name__ == "__main__":
    app.run(debug=True)
