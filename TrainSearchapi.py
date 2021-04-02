from flask import Flask,request, jsonify
from TrainSearch import Search
import psycopg2
import psycopg2.extras

app = Flask(__name__)

@app.route('/')
def hel_lo():
    print("Welcome To Train Search Bar!!")

@app.route('/search_api',methods = ['POST'])
def search_api():
    if request.method == "POST":
        req_json = request.json
        FRomstation = req_json['FRomstation']
        print(FRomstation)
        TosTation = req_json['TosTation']
        print(TosTation)
        DAte = req_json['DAte']
        print(DAte)

        a = Search(FRomstation, TosTation, DAte)
        a.train_Search()
        v = a.get_train_Details()
        t = a.Train_Schedule()
        print(v)
        
        return jsonify({"Your Details are": v,
        "Train Schedule are": t })



if __name__ == "__main__":
    app.run(debug=True)