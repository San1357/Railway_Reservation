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
        b = CancelTicket(pnr_no)
        c = b.get_cancel_ticket()
        print(str(c))

        return jsonify({"PNR Number": str(c), "Ticket Cancelled Status": True})


if __name__ == "__main__":
    app.run(debug=True)
