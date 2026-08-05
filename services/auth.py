from argon2 import PasswordHasher
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
    user = get_user_by_email(email)

    if user is None:
        return False
    try:
        ph.verify(user.passwordHash, password)
        return True
    except VerifyMisMatchError:
        return False