from sqlalchemy.orm import Session
from sqlalchemy import select
from src.module.display import *
from src.module.authentication import *
from src.entity.user import User
from src.database.conn import engine, get_db

def main():
    # Initalize db connection
    db = next(get_db())

    # Initialize welcome menu
    welcome_menu()

    # User authentication
    is_input_valid = False
    while not is_input_valid:
        answer = input("Input your answer (1/2) ")
        if answer == "1":
            login()
            is_input_valid = True
        elif answer == "2":
            register()
            is_input_valid = True
        else:
            print("Invalid input. Please only select either login (1) or register (2).")

    # Try db connection
    new_user = User(email="john@gmail.com", name="johddn", password="www")

    db.add(new_user)

    db.commit()

    user = db.query(User).filter_by(name="john").first()

    print(f'namamu {user.name}')

    db.close


if __name__ == "__main__":
    main()