from database import Database


class Search():
    def __init__(self, from_station, to_station, date):
        self.from_station = from_station
        self.to_station = to_station
        self.date = date
        self.info = []

    def train_search(self):
        print("FROM: ", self.from_station)
        print("TO: ", self.to_station)
        print("Date: ", self.date)

        search_list = []
        search_list.append(self.from_station)
        search_list.append(self.to_station)
        search_list.append(self.date)
        print(search_list)
        db = Database()
        self.traindetail_info = db.get_DB_Train_Details(self.from_station, self.to_station)

        print(self.traindetail_info)
        print(type(self.traindetail_info))
        print("from station:", self.traindetail_info[0])
        print("to station:", self.traindetail_info[1])
        print("train no:", self.traindetail_info[2])
        print("train name : ", self.traindetail_info[3])
        print("total no of seat:", self.traindetail_info[4])
        print("available seat: ", self.traindetail_info[5])
        print(type(self.traindetail_info[0]))
        print(type(self.traindetail_info[1]))
        print(type(self.traindetail_info[2]))
        print(type(self.traindetail_info[3]))
        print(type(self.traindetail_info[4]))
        print(type(self.traindetail_info[5]))

    def get_train_details(self):

        if self.traindetail_info is not None:
            if self.traindetail_info[0] == self.from_station and self.traindetail_info[1] == self.to_station:
                print("** Here is your Train detail **")
                print("Train NO:", self.traindetail_info[2])
                print("Train Name:", self.traindetail_info[3])
                print("Total Seats are:", self.traindetail_info[4])
                print("Available Seats are:", self.traindetail_info[5])
                result = {
                    "TrainNO": self.traindetail_info[2],
                    "Train_Name": self.traindetail_info[3],
                    "Total Seats are": self.traindetail_info[4],
                    "Available Seats are": self.traindetail_info[5]}
                return result
            else:
                print(
                    "sorry either the info is not available in our database or either you typed wrong")

    def train_schedule(self):

        if self.traindetail_info is not None:
            if self.traindetail_info[0] == self. from_station and self.traindetail_info[1] == self.to_station:
                print("** Train Schedule **")
                results = self.traindetail_info[6]
                print(results)
                print(type(results))
                for i in results:
                    print(i)
                return results


'''
print("---------------Class Init started---------------")
search_train_object = Search("Noida", "Gorakhpur", "12-03-2021")
print("---------------train_Search()--------------")
search_train_object.train_search()
print("---------------get_train_Details()--------------")
search_train_object.get_train_details()
print("---------------Train_Schedule()--------------")
search_train_object.train_schedule()
cur.close()
conn.close() '''