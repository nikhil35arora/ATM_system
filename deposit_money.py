from datetime import datetime

from storage import load_data, save_data


def deposit_money(amount):
    if amount <= 0:
        print("Deposit amount must be greater than 0.")
        return

    data = load_data()
    data["balance"] += amount
    data["transactions"].append(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposit: +Rs. {amount:.2f}"
    )
    save_data(data)
    print(f"Deposit successful. New Balance: Rs. {data['balance']:.2f}")
