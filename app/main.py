from flask import Flask, jsonify, request
import pprint
from multiple_booking_ticket import MultipleBooking
from train_search import Search
from cancel_ticket import CancelTicket


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
        response = ticket_booking.main_funcn(req_json)
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

        train_search_object = Search()
        train_search_object.train_search(from_station, to_station, date)
        detail_of_train = train_search_object.get_train_details()
        response_of_train = train_search_object.train_details_response()
        schedule_of_train = train_search_object.train_schedule()
        print(detail_of_train)
        return jsonify({"Your Details are": detail_of_train, "response ": response_of_train,  "Train Schedule are": schedule_of_train})


@app.route('/_cancel_ticket', methods=['POST'])
def cancel_ticket_api():
    if request.method == 'POST':
        req_json = request.json
        pnr_no = req_json['pnr_no']
        print(pnr_no)
        cancel_ticket_object = CancelTicket()
        cancel_ticket_object.enter_pnr_no(pnr_no)
        cancel_ticket_object.check_pnr_exist_or_not()
        pnr_response = cancel_ticket_object.response_of_pnr()

        return jsonify({"PNR Number": str(pnr_response), "Ticket Cancelled Status": True})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
