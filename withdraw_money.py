from datetime import datetime

from storage import load_data, save_data


def withdraw_money(amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
        return

    data = load_data()
    if amount > data["balance"]:
        print("Insufficient funds.")
        return

    data["balance"] -= amount
    data["transactions"].append(
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdraw: -Rs. {amount:.2f}"
    )
    save_data(data)
    print(f"Withdrawal successful. New Balance: Rs. {data['balance']:.2f}")
