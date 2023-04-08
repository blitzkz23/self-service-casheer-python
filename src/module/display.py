"""
This module provide functionality that are related to display/print some stuff.
"""

from tabulate import tabulate

def show_welcome_menu():
    """
    This function shows the initial welcome greeting menu on the self service cashier program.
    """
    
    print("---------- WELCOME TO YOUKOSO JAPARI STORE ----------")
    print("-----            SELF CASHIER SYSTEM            -----")
    print("-----------------------------------------------------")
    print("\n Main Menu")
    print("------------")
    print("Do you already have an account?")
    print("1. Login \n2. Register")
    print("-----------------------------------------------------")

def show_transaction_menu():
    """
    This function shows menu for the transaction related stuffs.
    """

    print("------------------------------------------------------")
    print("Apa yang ingin kamu lakukan? silahkan pilih menu di bawah.")
    print("1. Masukkan barang yang ingin dibeli")
    print("2. Perbarui daftar barang")
    print("3. Hapus barang dari keranjang")
    print("4. Batalkan transaksi")
    print("5. Lihat pesanan")
    print("6. Check out pesanan")
    print("7. Lihat pesanan yang telah di-check out")
    print("8. Keluar dari program")
    print("------------------------------------------------------")

def show_order(order: dict):
    table = []
    for item_name, item_info in order.items():
        qty = int(item_info["qty"])
        price = float(item_info["price"])
        total = qty * price
        table.append([item_name, qty, price, total])

    headers = ["Item Name", "Qty", "Price", "Total"]
    print("Order Anda saat ini: ")
    print(tabulate(table, headers = headers, tablefmt="grid"))

def show_checkout_order(order: dict):
    table = []
    for item_name, item_info in order.items():
        qty = int(item_info["qty"])
        price = float(item_info["price"])
        total = float(item_info["total"])
        discount = int(item_info["disc"])
        after_disc = float(item_info["after_disc"])
        table.append([item_name, qty, price, total, discount, after_disc])

    headers = ["Item Name", "Qty", "Price", "Total", "Discount (%)", "Price After Disc"]
    print(tabulate(table, headers = headers, tablefmt="grid"))