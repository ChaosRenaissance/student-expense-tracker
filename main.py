import csv
from collections import defaultdict


def load_expenses(file_path):
    expenses = []

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["amount"] = float(row["amount"])
            expenses.append(row)

    return expenses


def summarize_expenses(expenses):
    total = 0
    category_totals = defaultdict(float)

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        total += amount
        category_totals[category] += amount

    return total, category_totals


def print_summary(total, category_totals):
    print("Monthly Expense Summary")
    print("-----------------------")
    print(f"Total spending: ${total:.2f}")
    print()
    print("By category:")

    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")


def main():
    file_path = "expenses.csv"

    expenses = load_expenses(file_path)
    total, category_totals = summarize_expenses(expenses)
    print_summary(total, category_totals)


if __name__ == "__main__":
    main()
