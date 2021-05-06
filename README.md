# Railway_Reservation

Note: This Project is still in construction.

This Project is based on Railway Reservation in Python3 language & made with the help of Psql. 
This Project is in Rest Api form . 

What this Project do ?

This Project is on Railway Reservation Which have some basic funtionality like Booking_Ticket,  Cancel_Ticket, Pnr_Generator, Train_Search etc.


1)  book_ticket.py :

    It will take your basic detail like name, age, email, Aadhaar_no, From_station, To_Station, & no.of_seat_you_wanna_book etc.
    And then It will store these  detail into database  named traininfo after that it will fetch to other database named as Traindetail
    & which will check ur seat availability status . If it is available no. of seat you needed  then, it will book your seat & generate
    a 11 digit Pnr number which will be store in traininfo database.

2) book_ticket_api.py :

   Added Rest api to the Booktiicket4.py functionality.     

3) train_search.py: 

   What this Funtionality do is ? This will Provides you list of train_Detail , Train_Schedule etc . You have to provide some detail like 
   Fromstation, ToStation, & Date and then it will fetches the database named Train_detail then  matches your condition in database if it is there then Provides you Train_detail(like Train_No, Train_Name, Total_Seats, No_Of_Seats_available,Train_Schedule) thats it.


4) train_search_api.py :

   Added Rest Api in TrainSearch.py functionality.



5) cancel_ticket.py :

   This functionality is Cancel The Passenger's Ticket by giving PNR Number. You just have to give valid PNR Number then it will fetches
   the Pnr Number In database named TrainInfo & it will delete the Row of that Pnr Number.
   After that You will get message like "Your Ticket Is Cancel". 


6) cancel_ticket_api.py:

    Added Rest api To Cancel_Ticket.py functionality. 


7) pnr_status.py :
   
   It will just check Your Pnr Number. Means It will show the  status of PNR number like It is Valid or not, Confirmed or not, Present or not.


Some more Informations : 

!!! About Database !!!
I have create 3 databases Named PassengerInfo, Train_Detail, Pnr_store .


1)  passenger_details Database :
    
    It holds the records of Passenger detail(like name, age, email, adhaar_no,.... , Pnr_number)
    

2)  Train_Detail Database : 
    
    It holds the record of List Of Train & schedule .


3)  Pnr_store Database :

    It store the information like Status of Pnr Confirmed , Not Confirmed.


``

How TO Run this project :
step1 : open your Terminal
        $ ctrl + alt + T

step2 : git clone this project (by this command):

        $ git clone https://github.com/San1357/Railway_Reservation.git

step3 : Now run the docker-compose file

        $ docker-compose up --build 
        
        what this command do & give:

            * this command will  build image through dockerfile 

            * & Run the flask with database connection together
            
            * it will give u localhost like this http://0.0.0.0:5000
        
            * it will give u mesage like database system is ready to accept connection( which means you can now connect the database.)
            
            * Now I connect the database in pgadmin by entering connection details like (host, database name, user_name, & password( this thing you can found on docker-compose.yml file)).

step4 : exit the container 
        
        $ docker-compose down 

Note: if you want to run some other files you have to make changes in dockerfile :
       - In line 22 changes the filename with your filename which you want to run that's it .
         After that Repeat the step1, step2 & step3
 