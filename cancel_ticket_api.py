from flask import Flask, jsonify, request

from Cancel_Ticket import Cancel_ticket

import psycopg2
import psycopg2.extras

app = Flask(__name__)

@app.route('/')
def hello():
    print("Welcome to Cancel Ticket Function!!")


@app.route('/CancelTicket', methods = ['POST'])
def CancelTicket():
    
    if request.method =='POST':
        req_json = request.json
        Pnr_No = req_json['Pnr_No']
        print(Pnr_No)


        b = Cancel_ticket(Pnr_No)
        c = b.get_cancel_ticket()
        print(str(c))

        return jsonify({"PNR Number": str(c),
                        "Ticket Cancelled Status":True

        
        })



if __name__ == "__main__":
    app.run(debug=True)


