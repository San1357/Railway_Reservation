from flask import Flask, jsonify, request

import psycopg2

DB_Host = "127.0.0.1"
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"
h = 0

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Welcome To Pnr Status Checker'


@app.route('/pnr_connect/<int:a>')
def pnr_connect(a):
    conn = psycopg2.connect(
        host=DB_Host, database=DB_name, user=DB_user, password=DB_pass)

    cur = conn.cursor()
    cur.execute(
        "select status, pnrpresentstatus from pnr_store where pnr_no = %s;", (a,))

    print("cur : ", cur)
    v = cur.fetchone()

    conn.commit()

    cur.close()

    conn.close()

    print("v: ", v)

    return v


@app.route('/pnr_connect', methods=['GET', 'POST'])
def pnrc():

    f = ('Not confirmed', 'yes')
    j = ('confirmed', 'yes')
    if request.method == 'POST':
        req_json = request.json
        pnr_nos = req_json['pnr_nos']
        h = pnr_connect(pnr_nos)
        if h == f:
            print("h : ", h)
            print(f"{pnr_nos} is a valid Pnr number")
            result = {
                "PNR NUMBER": pnr_nos,
                "Status": "Valid",
                "CNF STATUS": "Not Confirmed",
                "Present": "This PNR number is present.",
                "Overall Status": False
            }

        if h == j:
            print("h : ", h)
            print(f"{pnr_nos} is a valid Pnr number")
            result = {
                "PNR NUMBER": pnr_nos,
                "Status": "Valid",
                "CNF STATUS": "Confirmed",
                "Present": "This PNR number is present.",
                "Overall Status": True
            }
        else:
            print(None)
            print(f"{pnr_nos} is Not a valid Pnr number")
            result = {
                "PNR NUMBER": pnr_nos,
                "Status": "Not Valid",
                "CNF STATUS": "Not Confirmed",
                "Present": "This PNR number is not present.",
                "Overall Status": None
            }

        response = jsonify(result)
        print(response)
        return response
    return jsonify({"response: Post Called"})


if __name__ == "__main__":
    app.run(debug=True)
