from sqlalchemy import text
from db.connection import conn


    # ContactId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
    # fName VARCHAR not null, 
    # lName VARCHAR not null, 
    # email varchar not null,
    # phone varchar,
    # acctId int REFERENCES Accounts (acctid),
    # statusId int REFERENCES status(statusid),
    # addressID int REFERENCES addresses(addressId),
    # created_at TIMESTAMP DEFAULT now(),
    # deleted BOOLEAN DEFAULT FALSE
def create_contact(fName,lName,email,phone=None,acctId=None,statusId=None,addressID=None):

    sql = text("""
        INSERT INTO contacts(fName,lName,email,phone,acctId,statusId,addressID)
        VALUES
            (
            :fName,
            :lName,
            :email,
            :phone,
            :acctId,
            :statusId,
            :addressID)
                        
        RETURNING contactid
    """)

    params = {
        "fName" : fName,
        "lName" : lName,
        "email" : email,
        "phone" : phone,
        "acctId" : acctId,
        "statusId" : statusId,
        "addressID" : addressID
    }

    with conn.session as session:
        contact_id= session.execute(sql, params).scalar_one()
        session.commit()
    return contact_id

def get_accounts(
    created_start=None,
    created_end=None,
    status_id=None,
    company_search=None
):
    sql = """
        SELECT
            a.acctid,
            a.company,
            a.statusid,
            s.status,
            a.created_at
        FROM accounts a
        LEFT JOIN status s
            ON s.statusid = a.statusid
            AND s.statustype = 'acc'
    """

    conditions = ["a.deleted = false"]
    params = {}

    if created_start is not None:
        conditions.append("a.created_at >= :created_start")
        params["created_start"] = created_start

    if created_end is not None:
        conditions.append("a.created_at <= :created_end")
        params["created_end"] = created_end

    if status_id is not None:
        conditions.append("a.statusid = :status_id")
        params["status_id"] = status_id

    if company_search:
        conditions.append("a.company ILIKE :company_search")
        params["company_search"] = f"%{company_search}%"

    sql += " WHERE " + " AND ".join(conditions)
    sql += " ORDER BY a.company"

    return conn.query(sql, params=params, ttl=0)
def get_account(account_id):
    result = conn.query(
        """
        SELECT
            a.acctid,
            a.company,
            a.primarycontactid,
            a.statusid,
            s.status,
            a.created_at,
            ad.addressid,
            ad.address,
            ad.city,
            ad.state,
            ad.zip
        FROM accounts a
        LEFT JOIN status s
            ON s.statusid = a.statusid
            AND s.statustype = 'acc'
        LEFT JOIN addresses ad
            ON ad.addressid = a.addressid
            AND ad.deleted = false
        WHERE a.acctid = :account_id
          AND a.deleted = false
        """,
        params={"account_id": account_id},
        ttl=0
    )

    if result.empty:
        return None

    return result.iloc[0]
