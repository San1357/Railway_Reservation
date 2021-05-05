# Railway_Reservation

Note: This Project is still in construction.

This Project is based on Railway Reservation in Python3 language & made with the help of Psql. 
This Project is in Rest Api form . 

What this Project do ?

This Project is on Railway Reservation Which have some basic funtionality like Booking_Ticket,  Cancel_Ticket, Pnr_Generator, 
Train_Search etc.


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



  For more Database Info :

    I have made another Readme  File name " DatabaseCreation.md" where i explain how to create Database(commands) .


Impotant Note : Please follow all Readme file to Run this project (DatabaseCreation.md ,DockerReadme.md) 