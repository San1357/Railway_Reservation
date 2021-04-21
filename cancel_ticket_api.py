from flask import Flask, jsonify, request

from cancel_ticket import CancelTicket

app = Flask(__name__)


@app.route('/')
def hello():
    print("Welcome to Cancel Ticket Function!!")


@app.route('/_cancel_ticket', methods=['POST'])
def _cancel_ticket():
    if request.method == 'POST':
        req_json = request.json
        pnr_no = req_json['pnr_no']
        print(pnr_no)
        cancel_ticket_object = CancelTicket(pnr_no)
        pnr_of_cancel_ticket = cancel_ticket_object.get_cancel_ticket()
        print(str(pnr_of_cancel_ticket))

        return jsonify({"PNR Number": str(pnr_of_cancel_ticket), "Ticket Cancelled Status": True})


if __name__ == "__main__":
    app.run(debug=True)
