from flask import Flask, jsonify, request
import pprint
from multiple_booking_ticket import MultipleBooking
from train_search import Search
from cancel_ticket import CancelTicket
from database import Database
from pnr_status_check import PnrChecker


app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


@app.route('/multiple_bookings', methods=['POST'])
def multiple_bookings_api():
    if request.method == "POST":
        req_json = request.json
        pprint.pprint(req_json)  # pprint will print your response in response json format.

        ticket_booking = MultipleBooking()
        ticket_booking.parsing(req_json)
        ticket_booking.book_seat()

        response = ticket_booking.create_response()
        return response


@app.route('/search_api', methods=['POST'])
def search_api():
    if request.method == "POST":
        req_json = request.json
        from_station = req_json['from_station']
        print(from_station)
        to_station = req_json['to_station']
        print(to_station)
        date = req_json['date']
        print(date)

        train_search_object = Search(from_station, to_station, date)
        train_search_object.train_search()
        detail_of_train = train_search_object.get_train_details()
        schedule_of_train = train_search_object.train_schedule()
        print(detail_of_train)
        return jsonify({"Your Details are": detail_of_train, "Train Schedule are": schedule_of_train})


@app.route('/_cancel_ticket', methods=['POST'])
def cancel_ticket_api():
    if request.method == 'POST':
        req_json = request.json
        pnr_no = req_json['pnr_no']
        print(pnr_no)
        cancel_ticket_object = CancelTicket(pnr_no)
        pnr_of_cancel_ticket = cancel_ticket_object.get_cancel_ticket()
        print(str(pnr_of_cancel_ticket))

        return jsonify({"PNR Number": str(pnr_of_cancel_ticket), "Ticket Cancelled Status": True})


@app.route('/pnr_connect', methods=['POST'])
def pnrc_api():

    f = ('Not confirmed', 'yes')
    j = ('confirmed', 'yes')
    if request.method == 'POST':
        req_json = request.json
        pnr_nos = req_json['pnr_nos']
        response = PnrChecker()
        json_ify = jsonify(response.pnr_connect(pnr_nos))

        print(json_ify)
        return json_ify
    return jsonify({"response: Post Called"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
