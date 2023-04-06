"""
This module provide functionality related to transaction on main program
"""

def ask_item_input():
    """
    Prompt the user for information about an item to add to an order.

    Returns:
        The name, quantity, and price of the item as entered by the user.
    """
    while True:
        try:
            item_name = input("1. Masukkan nama barang: ")
            qty = int(input("2. Masukkan jumlah barang yang ingin dipesan: "))
            price = float(input("3. Masukkan harga per barang: "))
            if qty <= 0 or price < 0:
                print("--- ERROR: Jumlah harus lebih dari 0 dan harga harus positif.  Mohon ulangi ---")
            else:
                return item_name, qty, price
        except ValueError:
            print("--- ERROR: Masukkan harus berupa angka.  Mohon ulangi ---")

def add_item(order: dict):
    """
    Add an item to the given order dictionary.

    Args:
        order (dict): The dictionary representing the order to add the item to.

    Returns:
        A dictionary containing the name, quantity, and price of the item as entered by the user.
    """

    # Prompt for user input
    item_name, qty, price = ask_item_input()
    order[item_name] = {"qty": qty, "price": price}

    return order
