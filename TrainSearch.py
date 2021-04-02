
import random 

from flask import Flask, jsonify,request
import math
import psycopg2
import psycopg2.extras

DB_Host = "127.0.0.1"
DB_name = "myfirstdatabase"
DB_user = "postgres"
DB_pass = "ranchi1357"



conn = psycopg2.connect(
    host = DB_Host, database = DB_name, user = DB_user, password = DB_pass)


cur = conn.cursor()


class Search():
    def __init__(self,Fromstation,Tostation,Date):
        self.Fromstation = Fromstation
        self.Tostation = Tostation
        self.Date = Date
        self.info = []
        
        

    def train_Search(self):
        print("FROM: ",self.Fromstation)
        print("TO: ", self.Tostation)
        print("Date: ", self.Date)
        


        #global info

        Ls =[]
        Ls.append(self.Fromstation)
        Ls.append(self.Tostation)
        Ls.append(self.Date)
        print(Ls)
        cur.execute("select * from traindetail where fromstation = %s and tostation = %s",(self.Fromstation,self.Tostation))
        
        self.info = list(cur.fetchone())
        #self.info.append(cur.fetchone())
        
        #self.info(list(cur.fetchone()))
        
        print (self.info)
        print (type(self.info))
        print (self.info[0])
        print(self.info[1])
        print(self.info[2])
        print(self.info[3])
        print(self.info[4])
        print(self.info[5])
        print (type(self.info[0]))
        print(type(self.info[1]))
        print (type(self.info[2]))
        print(type(self.info[3]))
        print (type(self.info[4]))
        print(type(self.info[5]))

    def get_train_Details(self):
        #self.train_Search()

        if self.info is not None:
            if self.info[0] == self.Fromstation and self.info[1] == self.Tostation:
                print("** Here is your Train detail **")
                print ("Train NO:",self.info[2])
                print("Train Name:", self.info[3])
                print("Total Seats are:", self.info[4])
                print("Available Seats are:", self.info[5])
                result = { 
                "Train NO:" : self.info[2],
                "Train Name" : self.info[3],
                "Total Seats are": self.info[4],
                "Available Seats are" : self.info[5]}
                return result
            else:
               print("sorry either the info is not available in our database or either you typed wrong")    
    
    '''def seat_booking(self):
        #self.train_Search()
        
        l = int(input("enter the number of seats u want:"))

        if l <= self.info[5]:
            print("Congratulations!!")
            print("You got ur seats book:",l)
            self.info[5] = self.info[5] - l
            y = cur.execute("update traindetail set avail_seat = %s where fromstation = %s and tostation = %s",(self.info[5],self.Fromstation,self.Tostation))
            conn.commit()
            count = cur.rowcount 
            print (count, "success")
            print("Now, Total no. of Seats available:", self.info[5])
        if l > self.info[5]:
            print("Sorry We don't have this no. of seat available.")
            print("We have only", self.info[5],"no . of seat available. ThankYou!!!") '''   
                 
            
    
    def Train_Schedule(self):
        #self.train_Search()

        if self.info is not None:
            if self.info[0] == self.Fromstation and self.info[1] == self.Tostation: 
                print("** Train Schedule **")
                results = self.info[6]
                print(results)
                print(type(results))
                for i in results:
                    print (i)
                    
                return results




    

#print("---------------Class Init started---------------")
#x = Search("Noida", "Gorakhpur", "12-03-2021")
#print("---------------train_Search()--------------")
#x.train_Search()
#print("---------------get_train_Details()--------------")
#x.get_train_Details()
#print("---------------seat_booking()--------------")
#x.seat_booking()
#print("---------------Train_Schedule()--------------")
#x.Train_Schedule()

#cur.close()
#conn.close()