--insert into pnr_store table

insert into pnr_store (pnr_no, status, pnrpresentstatus) values (7934082101, 'confirmed', 'yes'),(9274018223, 'confirmed','yes'), (9274072413, 'Not confirmed', 'No'), (7932632202, 'Not confirmed', 'No');


---insert passenger_details table 

insert into passenger_details (name, email, age, aadhaar_no, fromstation, tostation, class, train_no, pnr_number)values('jeet', 'jeet105@gmail.com', 19, 1491041, 'Noida', 'Gorakhpur', 'General', 12110, 1619860423842848);

--insert into traindetail table 


insert into traindetail (fromstation, tostation, train_no, train_name, total_seat, avail_seat, trainschedule)
values ('Gorakhpur',	'Pune',	1000409, 'PuneGorakhpurSpecial', 200, 2, '{GORAKHPUR_JN,BASTI,GONDA,BARABANKI,LUCKNOW,KANPUR_CENTRAL,JHANSI,BHOPAL,ITARSI,BHUSAVAL,MANMAD,AHMADNAGAR,PUNE_JN}'),
('Noida', 'Gorakhpur', 12110, 'NoidaGorakhpurSpecial', 155, 22,	'{NEW_DELHI,KANPUR_CENTRAL,BADSHAHNAGAR,GORAKHPUR,DEORIA_SADAR,SIWAN,CHHAPRA,SONPUR,HAJIPUR,MUZAFFARPUR,SAMASTIPUR,DARBHANGA}'),
('Gorakhpur', 'Pune', 12345, 'PuneGorakhpurSpecial', 200, 19, '{GORAKHPUR_JN,BASTI,GONDA,BARABANKI,LUCKNOW,KANPUR_CENTRAL,JHANSI,BHOPAL,ITARSI,BHUSAVAL,MANMAD,AHMADNAGAR,PUNE_JN}'),
('Mumbai', 'Gorakhpur', 500129, 'MombaiGorakhpurSpecial', 180, 59, '{LOKMANYATILAK,BHUSAVAL,ITARSI,BHOPAL,JHANSI,ORAI,POKHRAYAN,KANPUR_CENTRAL,AISHBAGH,BADSHAHNAGAR,GONDA,BASTI,KHALILABAD,GORAKHPUR}'),
('Noida', 'Pune', 12323, 'PuneNoidaSpecial', 192, 19, '{NIZAMUDDIN,MATHURA,AGRA,GWALIOR,JHANSI,BHOPAL,ITARSI,BHUSAVAL,MANMAD,KOPARGAON,PUNE}'),
('Mumbai', 'Pune', 125423, 'MombaipuneSpecial', 163, 23, '{LOKMANYATILAK,THANE,KALYAN,PUNE}'),
('Mumbai', 'Noida', 125943, 'MombaiNoidaSpecial' ,110, 45, '{BANDRA_TERMINUS,BORIVALI,VAPI,SURAT,VADODARA,GODHRA,BHAWANI_MANDI,KOTA,MATHURA,H_NIZAMUDDIN,NEW_DELHI}');
