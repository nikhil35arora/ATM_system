from storage import load_data


def show_statement():
    data = load_data()
    transactions = data["transactions"]

    if not transactions:
        print("No transactions yet.")
        return

    print("\nTransaction Statement:")
    for entry in transactions:
        print(entry)
