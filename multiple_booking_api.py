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
    pass

    

if __name__ == "__main__":
    app.run(debug=True)
