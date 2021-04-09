import psycopg2
import psycopg2.extras

DB_Host = "127.0.0.1"
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"

conn = psycopg2.connect(
    host=DB_Host, database=DB_name, user=DB_user, password=DB_pass)


cur = conn.cursor()


class Search():
    def __init__(self, from_station, to_station, date):
        self.from_station = from_station
        self.to_station = to_station
        self.date = date
        self.info = []

    def _train_search(self):
        print("FROM: ", self.from_station)
        print("TO: ", self.to_station)
        print("Date: ", self.date)

        Ls = []
        Ls.append(self.from_station)
        Ls.append(self.to_station)
        Ls.append(self.date)
        print(Ls)

        cur.execute(
            "select * from traindetail where fromstation=%s and tostation=%s",
            (self.from_station, self.to_station))
        self.info = list(cur.fetchone())

        print(self.info)
        print(type(self.info))
        print(self.info[0])
        print(self.info[1])
        print(self.info[2])
        print(self.info[3])
        print(self.info[4])
        print(self.info[5])
        print(type(self.info[0]))
        print(type(self.info[1]))
        print(type(self.info[2]))
        print(type(self.info[3]))
        print(type(self.info[4]))
        print(type(self.info[5]))

    def get_train_details(self):

        if self.info is not None:
            if self.info[0] == self.from_station and self.info[1] == self.to_station:
                print("** Here is your Train detail **")
                print("Train NO:", self.info[2])
                print("Train Name:", self.info[3])
                print("Total Seats are:", self.info[4])
                print("Available Seats are:", self.info[5])
                result = {
                    "TrainNO": self.info[2],
                    "Train_Name": self.info[3],
                    "Total Seats are": self.info[4],
                    "Available Seats are": self.info[5]}
                return result
            else:
                print(
                    "sorry either the info is not available in our database or either you typed wrong")

    def train_schedule(self):

        if self.info is not None:
            if self.info[0] == self. from_station and self.info[1] == self.to_station:
                print("** Train Schedule **")
                results = self.info[6]
                print(results)
                print(type(results))
                for i in results:
                    print(i)
                return results


print("---------------Class Init started---------------")
x = Search("Noida", "Gorakhpur", "12-03-2021")
print("---------------train_Search()--------------")
x._train_search()
print("---------------get_train_Details()--------------")
x.get_train_details()
print("---------------Train_Schedule()--------------")
x.train_schedule()
'''
cur.close()
conn.close() '''
