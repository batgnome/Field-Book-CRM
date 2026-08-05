CREATE TABLE Users(
    userId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    userFname varchar NOT NULL,
    userLname varchar NOT NULL,
    email varchar NOT NULL UNIQUE,
    phone varchar,
    role varchar NOT NULL,
    passwordHash varchar NOT NULL,
    createdAt timestamp DEFAULT now(),
    deleted boolean DEFAULT false
);
create TABLE status(
    statusID int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    status varchar,
    statusType varchar
);

insert into status(status, statusType) 
values ('tentative', 'acc'),
       ('lead', 'acc'),
       ('active', 'acc'),
       ('contract', 'acc'),
       ('inactive', 'acc'),
       ('active', 'con'),
       ('contract', 'con'),
       ('inactive', 'con'),
       ('active', 'cot'),
       ('process', 'cot'),
       ('inactive', 'cot'),
       ('active', 'lea'),
       ('inactive', 'lea');
create table AddressTypes(
    addressTypeId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    addressType varchar
);
create table Addresses(
    AddressId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    addressTypeId int REFERENCES AddressTypes( addressTypeId),
    address varchar,
    city varchar,
    state varchar,
    zip varchar,
    created_at TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE
);
create table Accounts(
    acctId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    company VARCHAR not null, 
    primaryContactId int,
    statusId int REFERENCES status(statusid),
    addressID int REFERENCES addresses(addressId),
    created_at TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE

);

create table Contacts(
    ContactId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    fName VARCHAR not null, 
    lName VARCHAR not null, 
    email varchar not null,
    phone varchar,
    acctId int REFERENCES Accounts (acctid),
    statusId int REFERENCES status(statusid),
    addressID int REFERENCES addresses(addressId),
    created_at TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE
    );

ALTER TABLE Accounts ADD CONSTRAINT fk_primary_contact 
    FOREIGN KEY (primaryContactId) REFERENCES Contacts(contactId);


create table Contracts(
    contractId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    acctId int REFERENCES Accounts(acctId) not null,
    primaryContactid int REFERENCES Contacts(contactid) not null,
    salesPersonID int REFERENCES Users(userId) not null,
    contractType varchar,
    amount NUMERIC(12,2),
    subscriptionType varchar,
    statusId int REFERENCES status(statusid),
    startDate TIMESTAMP,
    endDate TIMESTAMP,
    createdAt TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE

);
create table Leads(
    leadId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    source varchar not null,
    statusId int REFERENCES status(statusid),
    convertedAcctId int REFERENCES accounts(acctid) null,
    contactId int REFERENCES contacts(contactId) null,
    createdAt TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE
);
create table Activities(
    actId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    userId int REFERENCES users(userid) not null,
    acctId int REFERENCES accounts(acctid) null,
    contractId int REFERENCES contracts(contractid) null,
    activityType varchar,
    notes varchar,
    createdAt TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE
    
);
create table contractStageHistory(
    contrStHistId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    contractId int REFERENCES contracts(contractId) not null,
    fromStatus int REFERENCES status(statusid),
    toStatus int REFERENCES status(statusid),
    changedAt TIMESTAMP,
    changedByID int REFERENCES users(userid),
    createdAt TIMESTAMP DEFAULT now(),
    deleted BOOLEAN DEFAULT FALSE
);