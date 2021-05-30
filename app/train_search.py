from database import Database


class Search():
    def __init__(self):
        self.db = Database()

    def train_search(self, from_station, to_station, date):

        self.from_station = from_station
        self.to_station = to_station
        self.date = date
        self.info = []
        print("FROM: ", self.from_station)
        print("TO: ", self.to_station)
        print("Date: ", self.date)

        search_list = []
        search_list.append(self.from_station)
        search_list.append(self.to_station)
        search_list.append(self.date)
        print("search_list:", search_list)
        
        self.train_details_info = self.db.get_all_from_train_details(self.from_station, self.to_station)

        print(self.train_details_info)
        print(type(self.train_details_info))
        print(type(self.train_details_info[0]))
        print(type(self.train_details_info[1]))
        print(type(self.train_details_info[2]))
        print(type(self.train_details_info[3]))
        print(type(self.train_details_info[4]))
        print(type(self.train_details_info[5]))
        print("t_id", self.train_details_info[0])
        print("from station:", self.train_details_info[1])
        print("to station:", self.train_details_info[2])
        print("train no: ", self.train_details_info[3])
        print("total no of seat:", self.train_details_info[4])
        print("available seat: ", self.train_details_info[5])

    def get_train_details(self):

        if self.train_details_info is not None:
            if self.train_details_info[1] == self.from_station and self.train_details_info[2] == self.to_station:
                print("** Here is your Train detail **")
                print("Train_Id:", self.train_details_info[0])
                print("Train NO:", self.train_details_info[3])
                print("Total Seats are:", self.train_details_info[4])
                print("Available Seats are:", self.train_details_info[5])
                result = {
                    "Train_Id": self.train_details_info[0],
                    "Train_No": self.train_details_info[3],
                    "Total Seats are": self.train_details_info[4],
                    "Available Seats are": self.train_details_info[5]}
                return result
            else:
                print(
                    "sorry either the info is not available in our database or either you typed wrong")

    def train_schedule(self):

        if self.train_details_info is not None:
            if self.train_details_info[1] == self. from_station and self.train_details_info[2] == self.to_station:
                print("** Train Schedule **")
                results = self.train_details_info[6]
                print(results)
                print(type(results))
                for i in results:
                    print(i)
                return results


if __name__ == "__main__":
    print("---------------Class Init started---------------")
    search_train_object = Search()
    print("---------------train_Search()--------------")
    search_train_object.train_search("gkp", "pune", "12-03-2021")
    print("---------------get_train_Details()--------------")
    search_train_object.get_train_details()
    print("---------------Train_Schedule()--------------")
    search_train_object.train_schedule()
