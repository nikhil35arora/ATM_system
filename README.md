# ATM System Simulator 💳

A professional, modular Python-based ATM simulation that handles banking operations with persistent data storage. This system allows users to manage their finances through a clean command-line interface, ensuring all transactions are logged and balances are updated in real-time.

---

## 🌟 Key Features

### 🏦 Core Banking Operations
* **Balance Inquiry**: Check your current account balance instantly.
* **Secure Deposits**: Add funds to your account with automated transaction logging.
* **Smart Withdrawals**: Includes logic to prevent overdrawing and validates withdrawal amounts.
* **Detailed Statements**: View a complete history of your deposits and withdrawals with precise timestamps.

### 🛠️ Technical Highlights
* **Persistent Storage**: Uses a JSON-based "database" (`atm_data.json`) so your balance and history are saved even after closing the program.
* **Modular Architecture**: Organized into specific Python modules for high maintainability and readability.
* **Error Handling**: Built-in validation for invalid inputs and non-numeric entries.

---

## 📁 Project Structure

The application is divided into specialized modules to ensure clean code standards:

| File | Description |
| :--- | :--- |
| **`main.py`** | The entry point containing the main menu and user interaction logic. |
| **`storage.py`** | Manages data persistence, including loading and saving to the JSON file. |
| **`deposit_money.py`** | Handles the logic for adding funds and updating the ledger. |
| **`withdraw_money.py`** | Manages withdrawals, ensuring sufficient funds are available. |
| **`display_balance.py`** | Simple utility to fetch and format the current balance. |
| **`statement.py`** | Generates a formatted list of all past transactions. |
| **`atm_data.json`** | The data file storing the current balance and transaction strings. |

---

## 🚀 How to Run

### 1. Prerequisites
Ensure you have **Python 3.x** installed on your system.

### 2. Launch the Application
Navigate to the project folder in your terminal and run:
```bash
python main.py
```

### 3. Usage
Once the menu appears, choose an option (**1-5**) to:
1.  **Display Balance**: See your current funds.
2.  **Deposit Money**: Enter an amount to add to your balance.
3.  **Withdraw Money**: Enter an amount to take out.
4.  **Statement**: Review your transaction history.
5.  **Exit**: Securely close the application.

---

## 📊 Data Preview
Your data is stored securely in `atm_data.json`. An example of the saved data structure:
```json
{
  "balance": 20070.0,
  "transactions": [
    "2026-04-23 00:54:05 - Deposit: +$50000.00",
    "2026-04-23 00:54:22 - Withdraw: -$30000.00"
  ]
}
```

---

## 🛡️ Security & Validation
* **Amount Validation**: The system ensures you cannot deposit or withdraw negative amounts.
* **Input Safety**: Uses `try-except` blocks to prevent the program from crashing if a user enters text instead of numbers.
* **Fund Integrity**: Withdrawals are automatically blocked if the requested amount exceeds the available balance.
