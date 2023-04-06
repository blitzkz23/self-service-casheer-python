"""
This module provide functionality related to transaction on main program
"""

def ask_item_input():
    """
    Prompt the user for information about an item to add to an order.

    Returns:
        A tuple containing the name, quantity, and price of the item as entered by the user.
    """
    item_name = input("Masukkan nama barang: ")
    qty = int(input("Masukkan jumlah barang yang ingin dipesan: "))
    price = float(input("Masukkan harga per barang: "))

    input_dict = {
        item_name: {
            "qty": qty,
            "price": price
        }
    }

    print(input_dict)
    return input_dict

def add_order(order: dict, item_name: str, qty: int, price: float):
    """
    Add an item to the given order dictionary.

    Args:
        order (dict): The dictionary representing the order to add the item to.
        item_name (str): The name of the item to add.
        qty (int): The quantity of the item to add.
        price (float): The price of the item to add.

    Returns:
        None
    """
