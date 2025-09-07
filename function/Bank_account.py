"""
💳 Simple Banking System in Python
-----------------------------------
This script demonstrates a basic banking system
with functionalities to create accounts, deposit,
withdraw, transfer funds, and display account details.

Author: Soheil A-Yamini
"""

# -----------------------------
# Account Creation
# -----------------------------
def create_account(account_number, account_holder, balance=0):
    """Create a new account with given details."""
    return {
        "account_number": account_number,
        "account_holder": account_holder,
        "balance": balance
    }


# -----------------------------
# Deposit Function
# -----------------------------
def deposit(account, amount):
    """Deposit money into the account."""
    account["balance"] += amount
    print(f"{amount} deposited into account {account['account_number']}. "
          f"New balance: {account['balance']}")


# -----------------------------
# Withdraw Function
# -----------------------------
def withdraw(account, amount):
    """
    Withdraw money from the account.
    Includes error handling for insufficient funds.
    """
    if account["balance"] >= amount:
        account["balance"] -= amount
        print(f"Withdrawn {amount} from account {account['account_number']}. "
              f"Remaining balance: {account['balance']}")
    else:
        print(f"Insufficient funds in account {account['account_number']}")


# -----------------------------
# Transfer Function
# -----------------------------
def transfer(source_account, target_account, amount):
    """Transfer money from one account to another."""
    if source_account["balance"] >= amount:
        withdraw(source_account, amount)
        deposit(target_account, amount)
        print(f"Transferred {amount} from account {source_account['account_number']} "
              f"to account {target_account['account_number']}.")
    else:
        print(f"Insufficient funds in account {source_account['account_number']}")


# -----------------------------
# Display Function
# -----------------------------
def display(account):
    """Display account details."""
    print(f"Account: {account['account_number']} | "
          f"Holder: {account['account_holder']}")


# -----------------------------
# Main Demo
# -----------------------------
if __name__ == "__main__":
    # Create two accounts
    acc1 = create_account("123456", "Alice", 1000)
    acc2 = create_account("789012", "Bob", 500)

    # Perform some transactions
    deposit(acc1, 200)
    withdraw(acc1, 100)
    transfer(acc1, acc2, 300)

    # Final account details
    print("\n📊 Account details after transactions:")
    display(acc1)
    display(acc2)