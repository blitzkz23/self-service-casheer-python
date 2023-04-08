"""
This module provide functionality related to transaction on main program
"""
from sqlalchemy.orm import Session
from ..entity.transaction import Transaction

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
    if item_name in order:
        print("--- PEMBERITAHUAN: barang sudah ada di keranjang, silahkan update item untuk mengubah detail barang")
    else:
        order[item_name] = {"qty": qty, "price": price}
        print("--- Order telah ditambahkan! ---")

    return order

def update_item_name(order: dict, prev_name: str, new_name: str):
    """
    Update an item to the given order dictionary.

    Args:
        order (dict): The dictionary representing the order to add the item to.
        prev_name (dict): Previous name of the item
        new_name (dict): New name of the item

    Returns:
        Updated dictionary containing the name, quantity, and price of the item as entered by the user.
    """
    
    # Create new dict with the updated item name
    updated_dict = {
        new_name: {
            "qty": order[prev_name]["qty"],
            "price": order[prev_name]["price"]
        }
    }

    # Del previous item and update order with new dict
    del order[prev_name]
    order.update(updated_dict)

    return order

def update_item_qty(order: dict, item_name: str, new_name: str, new_qty: int):
    """
    Update an item to the given order dictionary.

    Args:
        order (dict): The dictionary representing the order to add the item to.
        item_name (dict): Name of the item
        new_name (dict): New name of the item
        new_qty (dict): Updated qty

    Returns:
        Updated dictionary containing the name, quantity, and price of the item as entered by the user.
    """

    # Check if the item_name as key has been changed
    if item_name not in order:
        order[new_name]["qty"] = new_qty
    else:
        # If not update using old name
        order[item_name]["qty"] = new_qty

    return order

def update_item_price(order: dict, item_name: str, new_name: str, new_price: float):
    """
    Update an item to the given order dictionary.

    Args:
        order (dict): The dictionary representing the order to add the item to.
        item_name (dict): Name of the item
        new_name (dict): New name of the item
        new_price (dict): Updated qty

    Returns:
        Updated dictionary containing the name, quantity, and price of the item as entered by the user.
    """

    # Check if the item_name as key has been changed
    if item_name not in order:
        order[new_name]["price"] = new_price
    else:
        # If not update using old name
        order[item_name]["price"] = new_price

    return order

def delete_item(order: dict, item_name: str):
    """
    Delete an item from the given order dictionary.

    Args:
        order (dict): The dictionary representing the order to delete the item from.
        item_name (str): The name of the item to delete.

    Returns:
        Updated dictionary with the specified item removed.
    """
    
    del order[item_name]
    print("--- Barang telah dihapus ---")

    return order

def reset_transaction(order: dict):
    """
    Reset transaction anew.

    Args:
        order (dict): The dictionary representing the order.
    """
    print("--- Transaksi telah dibatalkan. Keranjang Anda kosong ---")
    
    return order.clear()

def calculate_total_sum(order: dict):
    """
    Calculate total sums of given dictionary

    Args:
        order (dict): The dictionary representing the order.

    Returns:
        total_sum (float): The total sum of transaction price.    
    """
    
    for item in order.values():
        qty = item["qty"]
        price = item["price"]
        item_total = qty * price
        item["total"] = item_total

    return order

def calculate_discount(order: dict):
    """
    Calculate discount percent after certain threshold below.
        1. Total > 200k, 5% disc.
        2. Total > 300k, 6% disc.
        3. Total > 500k, 7% disc.

    Args:
        order (dict): The dictionary representing the order.

    Returns:
        discount_percentage (int): The number of discount percentage.
    """

    for item in order.values():
        total = item["total"]

        if total > 500000:
            item["discount"] = 7
        elif total > 300000:
            item["discount"] = 6
        elif total > 200000:
            item["discount"] = 5
        else:
            item["discount"] = 0

    return order
    
def calculate_price_after_discount(order: dict):
    """
    Calculate the total price after discount.

    Args:
        order (dict): The dictionary representing the order.
    
    Returns:
        price_after_discount (float): The total price after discount.
    """

    for item in order.values():
        total = item["total"]
        discount = item["discount"]

        price_after_discount = total * (1 - (discount / 100))
        item["after_disc"] = price_after_discount

    return order

def insert_to_database(db: Session, order: dict, user_id: int):
    """
    Insert the transaction into database

    Args:
        order (dict): The dictionary representing the order.
    
    Returns:
        db (Session): database's session
        price_after_discount (float): The total price after discount.
        current_user: current logged in user
    """

    try:
        for item_name, item in order.items():
            qty = item["qty"]
            price = item["price"]
            total = item["total"]
            discount = item["discount"]
            after_disc = item["after_disc"]

            transaction = Transaction(user_id, item_name, qty,
                                      price, total, discount, after_disc)
            db.add(transaction)
            db.commit()
            transaction = db.query(Transaction).filter(Transaction.item_name == item_name).first()
            
            print("---------------------------")
            print("--- Checkout berhasil ! ---")
            print("---------------------------")
    except Exception as e:
        db.rollback()
        raise Exception(f"--- ERROR: Gagal melakukan checkout {str(e)} ---")
        