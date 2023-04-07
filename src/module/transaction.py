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