from sqlalchemy import text
from db.connection import conn


def create_user(userFname, userLname, email, phone, role, passwordHash):

    sql = text("""
        INSERT INTO users
            (userFname, userLname, email, phone, role, passwordHash)
        VALUES
            (:userFname, :userLname, :email, :phone, :role, :passwordHash)
    """)

    params = {
        "userFname": userFname,
        "userLname": userLname,
        "email": email,
        "phone": phone,
        "role": role,
        "passwordHash": passwordHash
    }

    with conn.session as session:
        session.execute(sql, params)
        session.commit()

def check_existing_user(email):

    
    result = conn.query("Select 1 from users where email = :email", params={"email" : email})
    return not result.empty()


def get_user_by_email(email):
    result = conn.query("Select passwordhash from users where email = :email", params={"email" : email})
    if result.empty:
        return None

    return result.iloc[0]["passwordhash"]
    # userId int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    # userFname varchar NOT NULL,
    # userLname varchar NOT NULL,
    # email varchar NOT NULL UNIQUE,
    # phone varchar,
    # role varchar NOT NULL,
    # passwordHash varchar NOT NULL,
    # createdAt timestamp DEFAULT now(),
    # deleted boolean DEFAULT false