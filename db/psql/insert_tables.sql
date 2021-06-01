-- insert user_details table
insert into user_details (passenger_uid, name, age, email, aadhaar_no) values ('88c85148-40fe-4367-889a-d73ca60c89ab', 'jeet', 19, 'jeet105@gmail.com', 1491041);

-- insert into train_details table
insert into train_details (t_id, from_station, to_station, train_no, total_seats, avail_seats, train_schedule)
values ('4d19ae9d-0944-4eed-8072-2b0c084e300c', 'Pune', 'Gorakhpur', 12345, 200, 19, '{GORAKHPUR_JN,BASTI,GONDA,BARABANKI,LUCKNOW,KANPUR_CENTRAL,JHANSI,BHOPAL,ITARSI,BHUSAVAL,MANMAD,AHMADNAGAR,PUNE_JN}'),
('09aa103f-bbda-434e-96dd-2de98623b82f', 'Mumbai', 'Gorakhpur', 500129, 180, 59, '{LOKMANYATILAK,BHUSAVAL,ITARSI,BHOPAL,JHANSI,ORAI,POKHRAYAN,KANPUR_CENTRAL,AISHBAGH,BADSHAHNAGAR,GONDA,BASTI,KHALILABAD,GORAKHPUR}');


-- insert into pnr_details table
insert into pnr_details (pnr_id, pnr_number) values ('32dcd511-56bc-418f-b7a3-fa337eca2062', 1612344455854958);

-- insert into booking_details table

insert into booking_details (passenger_uid, t_id, pnr_id) values ('88c85148-40fe-4367-889a-d73ca60c89ab', '4d19ae9d-0944-4eed-8072-2b0c084e300c', '32dcd511-56bc-418f-b7a3-fa337eca2062');
