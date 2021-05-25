--insert into pnr_store table

insert into pnr_store (pnr_no, status, pnrpresentstatus) values (7934082101, 'confirmed', 'yes'),(9274018223, 'confirmed','yes'), (9274072413, 'Not confirmed', 'No'), (7932632202, 'Not confirmed', 'No');


---insert user_details table 

insert into user_details (passenger_uid, name, age, email, aadhaar_no) values (uuid_generate_v4(), 'jeet', 19, 'jeet105@gmail.com', 1491041);
