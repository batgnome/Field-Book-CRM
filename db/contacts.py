from sqlalchemy import text
from db.connection import conn

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

def get_contacts():
    sql = """
        SELECT
            c.contactid,
            c.fname,
            c.lname,
            c.email
        FROM contacts c
        where c.acctid is null
    """


    return conn.query(sql, ttl=0)
def contact_id(contact_id):
    result = conn.query(
        """
        SELECT
            c.contactid,
            c.fname,
            c.lname,
            c.email,
            c.acctid,
            a.company,
            s.status,
            a.created_at,
            ad.addressid,
            ad.address,
            ad.city,
            ad.state,
            ad.zip
        FROM contacts c
        LEFT JOIN status s
            ON s.statusid = c.statusid
            AND s.statustype = 'cont'
        LEFT JOIN addresses ad
            ON ad.addressid = c.addressid
            AND ad.deleted = false
        LEFT JOIN accounts a on a.primarycontactid = c.contactid
        WHERE a.acctid = :account_id
          AND a.deleted = false
        """,
        params={"contact_id": contact_id},
        ttl=0
    )

    if result.empty:
        return None

    return result.iloc[0]
