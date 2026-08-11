from sqlalchemy import text
from db.connection import conn



def create_account(company,primaryContactId,statusId,addressID):
 #acctId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
#     company VARCHAR not null, 
#     primaryContactId int,
#     statusId int REFERENCES status(statusid),
#     addressID int REFERENCES addresses(addressId),
#     created_at TIMESTAMP DEFAULT now(),
#     deleted BOOLEAN DEFAULT FALSE
    sql = text("""
        INSERT INTO accounts(company,primaryContactId,statusId,addressID)
        VALUES
            (:company,:primaryContactId,:statusId,:addressID)
                        )
        RETURNING acctid
    """)

    params = {
        "company": company,
        "primaryContactId": primaryContactId,
        "statusId": statusId,
        "addressID": addressID
    }

    with conn.session as session:
        account_id= session.execute(sql, params).scalar_one()
        session.commit()
    return account_id
def get_accounts(created_s,created_e,status,search_company):
    sql = text("""
    select 
    a.company,
    s.status,
    a.created_at 
    from accounts a
    inner join status s on s.statusid = a.statusid and s.statustype = 'acc'
   
""")
    if  created_s != "" or created_e != "" or status != "" or search_company != "" :
         
        sql += """ 
        where 
        """
        if created_s != "" and created_e != "":
            sql += """" a.created_at  >= :created_s and a.created <= :created_e """
        elif created_s != "":
            sql += """" a.created_at  >= :created_s """
        elif created_e != "":
                    sql += """" a.created_at  <= :created_e """
        if status != "":
                    sql += """" s.statusid == :status"""
        if search_company != "":
                    sql += """" a.company like %:search_company%"""
        
        params = {
            "created_s": created_s,
            "created_e": created_e,
            "status": status,
            "search_company": search_company,
        

    }
def get_account(acctid):
      sql = text("""
        select a.company,s.status,a.created_at,ad.address from accounts a
        inner join status s on s.statusid = a.statusid and s.statustype = 'acc'
        inner join addresses ad on ad.addressid = a.addressid
        inner join addressstypes at on at.addressTypeId = ad.addressTypeid and at.addresstype = 'acc' 
        where a.acctid = :acctid
     """)
      params = {
        "acctid": acctid
    }
# insert into status(status, statusType) 
# values ('tentative', 'acc'),
#        ('lead', 'acc'),
#        ('active', 'acc'),
#        ('contract', 'acc'),
#        ('inactive', 'acc'),
#        ('active', 'con'),
#        ('contract', 'con'),
#        ('inactive', 'con'),
#        ('active', 'cot'),
#        ('process', 'cot'),
#        ('inactive', 'cot'),
#        ('active', 'lea'),
#        ('inactive', 'lea');
# create table AddressTypes(
#     addressTypeId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     addressType varchar
# );
# create table Addresses(
#     AddressId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     addressTypeId int REFERENCES AddressTypes( addressTypeId),
#     address varchar,
#     city varchar,
#     state varchar,
#     zip varchar,
#     created_at TIMESTAMP DEFAULT now(),
#     deleted BOOLEAN DEFAULT FALSE
# );
# create table Accounts(
#     acctId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
#     company VARCHAR not null, 
#     primaryContactId int,
#     statusId int REFERENCES status(statusid),
#     addressID int REFERENCES addresses(addressId),
#     created_at TIMESTAMP DEFAULT now(),
#     deleted BOOLEAN DEFAULT FALSE

# );

# create table Contacts(
#     ContactId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
#     fName VARCHAR not null, 
#     lName VARCHAR not null, 
#     email varchar not null,
#     phone varchar,
#     acctId int REFERENCES Accounts (acctid),
#     statusId int REFERENCES status(statusid),
#     addressID int REFERENCES addresses(addressId),
#     created_at TIMESTAMP DEFAULT now(),
#     deleted BOOLEAN DEFAULT FALSE
#     );

# ALTER TABLE Accounts ADD CONSTRAINT fk_primary_contact 
#     FOREIGN KEY (primaryContactId) REFERENCES Contacts(contactId);