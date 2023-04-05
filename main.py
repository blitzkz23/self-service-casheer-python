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
    current_user = None

    is_input_valid = False
    while not is_input_valid:
        answer = input("Input your answer (1/2) ")
        if answer == "1":
            current_user = login(db)
            print(f'cok {current_user}')
            is_input_valid = True
        elif answer == "2":
            register(db)
            is_input_valid = True
        else:
            print("Input Anda salah, silahkan pilih antara Login(1) atau Register(2).")   

    print(f'cok 2 {current_user.email}')


if __name__ == "__main__":
    main()