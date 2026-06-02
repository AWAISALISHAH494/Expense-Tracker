import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    title = input("Enter expense title: ").strip()
    amount = input("Enter amount: ").strip()

    if not title or not amount:
        print("Invalid input")
        return

    try:
        amount = float(amount)
    except:
        print("Amount must be a number")
        return

    expense = {
        "title": title,
        "amount": amount,
        "date": str(datetime.now().date())
    }

    expenses.append(expense)
    print("Expense added")

def view_expenses(expenses):
    if not expenses:
        print("No expenses found")
        return

    print("\n==================== EXPENSES ====================")
    total = 0

    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['title']} | {e['amount']} | {e['date']}")
        total += e["amount"]

    print("==================================================")
    print("Total:", total)

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return

    try:
        num = int(input("Enter number to delete: "))
        if 1 <= num <= len(expenses):
            removed = expenses.pop(num - 1)
            print("Deleted:", removed["title"])
        else:
            print("Invalid number")
    except:
        print("Invalid input")

def search_expense(expenses):
    keyword = input("Enter keyword: ").strip().lower()
    results = []

    for e in expenses:
        if keyword in e["title"].lower():
            results.append(e)

    if not results:
        print("No matching expenses")
        return

    print("\nResults:")
    for e in results:
        print(e["title"], e["amount"], e["date"])

def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            search_expense(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Saved and exited")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()