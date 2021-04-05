from flask import Flask, jsonify, request

from Bookticket4 import Ticket

import psycopg2
import psycopg2.extras

app = Flask(__name__)

@app.route('/')
def hello():
    print("Welcome")


@app.route('/Booking',methods = ['POST'])
def Booking():
    '''print("Welcome to booking")
    print("NAME: ", name)
    print("AGE:",age)
    print("EMAIL:",email)
    print("AADHAAR_NO:",aadhaar_no)
    print("FROM_STATION:",fromstation)
    print("TOSTATION:",tostation)
    print("CLASS",Class)
    print("TRAIN NO:",train_no)'''

    if request.method =="POST":
        req_Json =request.json
        Name = req_Json['Name']
        print(Name)
        A_ge = req_Json['A_ge']
        print(A_ge)
        E_mail = req_Json['E_mail']
        print(E_mail)
        A_adhaar_no = req_Json['A_adhaar_no']
        print(A_adhaar_no)
        F_romstation = req_Json['F_romstation']
        print(F_romstation)
        T_ostation = req_Json['T_ostation']
        print(T_ostation)
        C_lass = req_Json['C_lass']
        print(C_lass)
        T_rain_no = req_Json['T_rain_no']
        print(T_rain_no)
        Fromstation = req_Json['Fromstation']
        print(Fromstation)
        Tostation = req_Json['Tostation']
        print(Tostation)
        Date = req_Json['Date']
        print(Date)
        no_of_seat_u_wanna_book = req_Json['no_of_seat_u_wanna_book']
        print(no_of_seat_u_wanna_book)

        a = Ticket(Name,A_ge,E_mail,A_adhaar_no,F_romstation,T_ostation,C_lass,T_rain_no, Fromstation,Tostation,Date,no_of_seat_u_wanna_book)
        a.Booking_Ticket()
        e = a.seat_booking()
        print(str(e))
        

        d = a.Pnrgenerator()
        print(str(d))
        return jsonify({"Your PNR number number is ":  str(d),
                        "no. Of seat you booked" : str(e),
                        "status": True
                        
                                
        })
            

if __name__ == "__main__":
    app.run(debug=True)
