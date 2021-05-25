-- Creation of pnr_store table 
create table if not exists pnr_store(
    pnr_no numeric(30) NOT NULL,
    status varchar(30) NOT NULL,
    pnrpresentstatus varchar(20) NOT NULL
);



-- Creation of user_details table
create table if not exists user_details(
    passenger_uid uuid NOT NULL primary key, 
    name varchar(30) NOT NULL,
    age  int NOT NULL,
    email varchar(40) NOT NULL UNIQUE,
    aadhaar_no int UNIQUE NOT NULL
);

-- Creation of train_detail table
create table if not exists traindetail(
    fromstation varchar(20) NOT NULL,
    tostation varchar(20) NOT NULL,
    train_no int NOT NULL,
    train_name varchar(50),
    total_seat int NOT NULL,
    avail_seat int NOT NULL,
    trainschedule TEXT
);