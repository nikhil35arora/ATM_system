from storage import load_data


def display_balance():
    data = load_data()
    print(f"Current Balance: Rs. {data['balance']:.2f}")
