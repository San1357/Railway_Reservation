-- Creation of pnr_store table 
create table if not exists pnr_store(
    pnr_no numeric(30) NOT NULL,
    status varchar(30) NOT NULL,
    pnrpresentstatus varchar(20) NOT NULL
);



-- Creation of passenger_details table
create table if not exists passenger_details(
    name varchar(30) NOT NULL,
    email varchar(40) NOT NULL UNIQUE,
    age  int NOT NULL,
    aadhaar_no int UNIQUE NOT NULL,
    fromstation varchar(30) NOT NULL,
    tostation varchar(20) NOT NULL,
    class varchar(20) NOT NULL,
    train_no int NOT NULL,
    pnr_number bigint NOT NULL
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