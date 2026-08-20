from sqlalchemy import text
from db.connection import conn



def create_account(company,primaryContactId=None,statusId=None,addressID=None):
    primaryContactId = primaryContactId or None
    statusId = statusId or None
    addressID = addressID or None
    sql = text("""
        INSERT INTO accounts(company,primaryContactId,statusId,addressID)
        VALUES
            (:company,:primaryContactId,:statusId,:addressID)
                        
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

def get_accounts(
    created_start=None,
    created_end=None,
    status_id=None,
    company_search=None,
    archived=False
):
    sql = """
       SELECT
            a.acctid,
            a.company,
            a.statusid,
            s.status,
            a.created_at,
            Case when a.deleted then 'archived' else 'active'  end as archived
        FROM accounts a
        LEFT JOIN status s
            ON s.statusid = a.statusid
            AND s.statustype = 'acc'
      
        
    """
    if  not archived:
        conditions = ["a.deleted = false"]
    else:
        conditions = ["a.deleted = true"]
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

def get_account(account_id, archived=False):
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
            ad.zip,
            c.fname,
            c.lname
        FROM accounts a
        LEFT JOIN status s
            ON s.statusid = a.statusid
            AND s.statustype = 'acc'
        LEFT JOIN addresses ad
            ON ad.addressid = a.addressid
            AND ad.deleted = false
        LEFT JOIN contacts c 
            ON c.contactid = a.primarycontactid
        WHERE a.acctid = :account_id
          AND a.deleted = false
        """,
        params={"account_id": account_id},
        ttl=0
    )

    if result.empty:
        return None
    
    return result.iloc[0]

def delete_account(acctid):
    sql = text("""
        UPDATE accounts
        SET deleted = true
        WHERE acctid = :acctid
    """)

    with conn.session as session:
        session.execute(sql, {"acctid": acctid})
        session.commit()

def update_account(acctid, company,primaryContactId=None,statusId=None,addressID=None):
    sql = text("""
        UPDATE accounts
        SET company = :company, 
        primaryContactId= :primaryContactId,
        statusId = :statusId,
        addressID = :addressID
        WHERE acctid = :acctid
    """)

    with conn.session as session:
        session.execute(sql, {"acctid": acctid,
                            "company" :company,
                            "primaryContactId" :primaryContactId,
                            "statusId" :statusId,
                            "addressID" :addressID})
        session.commit()
