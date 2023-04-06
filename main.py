from sqlalchemy.orm import Session
from sqlalchemy import select
from src.database.conn import engine, get_db
from src.module.display import *
from src.module.authentication import *
from src.module.transaction import *

def main():
    # Initalize db connection
    db = next(get_db())

    # Display welcome menu
    show_welcome_menu()

    # User authentication
    # current_user = None

    # is_input_valid = False
    # while not is_input_valid:

    #     # Ask user input
    #     answer = input("Masukkan jawaban Anda (1/2) \n> ")
    #     if answer == "1":
    #         current_user = login(db)
    #         is_input_valid = True
    #     elif answer == "2":
    #         register(db)
    #         is_input_valid = True
    #     else:
    #         print("Input Anda salah, silahkan pilih antara Login(1) atau Register(2).")   

    # Create empty dictionary to store order temporarily
    order = {} 

    # Transaction related section
    is_transaction_done = False
    while not is_transaction_done:

        # Display transaction menu
        show_transaction_menu()
        menu_choice = input("Pilihan menu (1-5) \n> ")
        if menu_choice == "1":
            # Add item
            while True:
                print("-----------------------------------------------------")
                order = add_item(order)
                print("--- Order telah ditambahkan! ---")
                print("Order Anda saat ini: ")
                show_order(order)
                print("")
                input_again = input("Mau menambahkan lagi? (y/n) \n> ")
                if input_again.lower() == 'y':
                    continue
                else:
                    break
        elif menu_choice == "2":
            # Update item
            print("Order Anda saat ini: ")
            show_order(order)
        elif menu_choice == "3":
            # delete_item()
            print("Hello world")
        elif menu_choice == "4":
            # reset_transaction()
            print("Hello world")
        elif menu_choice == "5":
            # check_order()
            print("Hello world")
        elif menu_choice == "6":
            # check_out()
            print("Hello world")
        else:
            # exit_program()
            print("Hello world")

        



if __name__ == "__main__":
    main()