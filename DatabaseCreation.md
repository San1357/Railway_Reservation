In this Railway Reservation Project. I created  databases like Passengerdetail, Traindetail, PnrStore.
I created databases in Psql using PgAdmin4 browser(on Server).

pgAdmin ?

 * How to install pgAdmin4 you can follow this link: https://www.youtube.com/watch?v=Z0G7dhc36Ao  . 
 * Follow his 3 step (viz client ==> Server) cause it will be little easy & more comfortable than others.




--> Passenger_details Database : It store the detail of every Passenger like name, email, age, train_no, TrainName,
                               from/tostation, aadhaar_no, & pnr_number etc 


--> Traindetail Database : It store the Train Detail means List of Train.  like Train_no , Train_name, 
                           from/to station, Total_seat, Available Seat & List of TrainSchedule.

                
-->  PnrStore Database : It store the Pnr Detail like PnrNumber, Status, PnrPresentStatus.


General Commands for Psql :

1) How To Create Table in Psql:

     $ CREATE TABLE table_Name (
        column1 datatype(length) column_contraint,
        column2 datatype(length) column_contraint,
        column3 datatype(length) column_contraint,
        table_constraints
        );

2) How to INSERT Value in Table :

     $ INSERT INTO table_Name(column1, column2, …)
       VALUES (value1, value2, …);


3) How to see table :

     $ select * from tableName


** Now Some commands you might be needed :

4) How To delete Row from Table :

    $ delete from tableName
    where condition;

5) How to Update or modify data in a table:

    $ UPDATE table_name
      SET column1 = value1,
      column2 = value2,
      ...
      WHERE condition;

This is the commands i used while i was creating Databases Table. 
    

