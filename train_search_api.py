from flask import Flask, request, jsonify
from train_search import Search


app = Flask(__name__)


@app.route('/')
def hel_lo():
    print("Welcome To Train Search Bar!!")


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

        a = Search(from_station, to_station, date)
        a._train_search()
        v = a.get_train_details()
        t = a.train_schedule()
        print(v)
        return jsonify({"Your Details are": v, "Train Schedule are": t})


if __name__ == "__main__":
    app.run(debug=True)
