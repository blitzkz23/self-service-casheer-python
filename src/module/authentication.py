"""
This module provide functionality that connect User"s account to database.
"""
from sqlalchemy.orm import Session
from ..entity.user import User

def register(db: Session):
    """
    This function will take argument input from user and commit it to database if provided input is valid.
    
    Args:
    - email (str): user email address
    - name (str): user name
    - password (str): user password
    """

    # Validate user input
    is_input_valid = False
    while not is_input_valid:
        # Take user input
        name = input("Siapa nama Anda? ")
        email = input("Masukkan email: ")
        password = input("Masukkan password: (min 6 karakter) ")

        is_input_valid = validate_register_input(email, name, password)

    user = User(email, name, password)
    db.add(user)
    db.commit()

    user = db.query(User).filter(User.email == email, User.password == password).first()
    print("Anda telah berhasil terdaftar.  Silahkan masuk")
    login(db)

def validate_register_input(email: str, name: str, password: str) -> bool:
    """
    Validates user input for registration.

    Args:
    - email (str): user email address
    - name (str): user name
    - password (str): user password

    Returns:
    - bool: True if user input is valid, False otherwise
    """

    if not email or not name or not password:
        print("--- ERROR: Semua data harus diisi. Mohon ulangi ---")
        return False

    if len(name) > 30:
        print("--- ERROR: Nama tidak boleh lebih dari 30 karakter ---")
        return False

    if len(email) > 50:
        print("--- ERROR: Email tidak boleh lebih dari 50 karakter ---")
        return False

    if len(password) < 6 or len(password) > 25:
        print("--- ERROR: Password minimal 6 karakter dan maksimal 25 karakter ---")
        return False
    
    if not "@" in email or not "." in email:
        print("--- ERROR: Format e-mail tidak valid ---")
        return False

    return True

    

def login(db: Session):
    """
    This function will take argument input from user and check if the existing user is on database, if yes then login success.
    """