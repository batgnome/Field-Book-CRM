from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from db.users import create_user, get_user_by_email
ph = PasswordHasher()

def register_user(userFname, userLname, email, phone, role,password):
    password_hash = ph.hash(password)

    create_user(
        userFname,
        userLname,
        email,
        phone,
        role,
        password_hash
    )
def authenticate(email, password):
    auth_data = get_user_by_email(email)

    if auth_data is None:
        return None
    user,password_hash = auth_data

    try:
        ph.verify(password_hash, password)
        return user
    except VerifyMismatchError:
        return False