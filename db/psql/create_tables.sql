-- creating extension for uuid_generate_v4()
create extension if not exists "uuid-ossp";

-- Creation of user_details table
create table if not exists user_details(
    passenger_uid uuid NOT NULL primary key,
    name varchar(30) NOT NULL,
    age  int NOT NULL,
    email varchar(40) NOT NULL UNIQUE,
    aadhaar_no int UNIQUE NOT NULL
);

-- Creation of train_detail table
create table if not exists train_details(
    t_id uuid NOT NULL primary key,
    from_station varchar(30) NOT NULL,
    to_station varchar(30) NOT NULL,
    train_no int NOT NULL,
    total_seats int NOT NULL,
    avail_seats int NOT NULL,
    train_schedule TEXT
);

--Creation of pnr_details table
create table if not exists pnr_details(
    pnr_id uuid NOT NULL primary key,
    pnr_number bigint NOT NULL UNIQUE
);

--Creation of booking_details table
create table if not exists booking_details(
    passenger_uid uuid REFERENCES user_details(passenger_uid),
    t_id uuid REFERENCES train_details(t_id),
    pnr_id uuid REFERENCES pnr_details(pnr_id)
);
