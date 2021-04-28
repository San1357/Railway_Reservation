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

        train_search_object = Search(from_station, to_station, date)
        train_search_object.train_search()
        detail_of_train = train_search_object.get_train_details()
        schedule_of_train = train_search_object.train_schedule()
        print(detail_of_train)
        return jsonify({"Your Details are": detail_of_train, "Train Schedule are": schedule_of_train})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
