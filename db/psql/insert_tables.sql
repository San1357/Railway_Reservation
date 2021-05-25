--insert into pnr_store table

insert into pnr_store (pnr_no, status, pnrpresentstatus) values (7934082101, 'confirmed', 'yes'),(9274018223, 'confirmed','yes'), (9274072413, 'Not confirmed', 'No'), (7932632202, 'Not confirmed', 'No');


---insert user_details table 

insert into user_details (passenger_uid, name, age, email, aadhaar_no) values (uuid_generate_v4(), 'jeet', 19, 'jeet105@gmail.com', 1491041);


--insert into train_details table 


insert into train_details (t_id, from_station, to_station, train_no, total_seats, avail_seats, train_schedule)
values (uuid_generate_v4(), 'Pune', 'Gorakhpur', 12345, 200, 19, '{GORAKHPUR_JN,BASTI,GONDA,BARABANKI,LUCKNOW,KANPUR_CENTRAL,JHANSI,BHOPAL,ITARSI,BHUSAVAL,MANMAD,AHMADNAGAR,PUNE_JN}'),
(uuid_generate_v4, 'Mumbai', 'Gorakhpur', 500129, 180, 59, '{LOKMANYATILAK,BHUSAVAL,ITARSI,BHOPAL,JHANSI,ORAI,POKHRAYAN,KANPUR_CENTRAL,AISHBAGH,BADSHAHNAGAR,GONDA,BASTI,KHALILABAD,GORAKHPUR}');


--insert into pnr_details table


insert into pnr_details (pnr_id, pnr_number) values (uuid_generate_v4(), 1612344455854958);

