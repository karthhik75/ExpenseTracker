import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create expenses table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS expenses (
             id INTEGER PRIMARY KEY,
             name TEXT,
             category TEXT,
             amount REAL,
             date TEXT)''')

# Commit and close the connection
conn.commit()
def add_expense(name, category, amount, date):
    with conn:
        c.execute("INSERT INTO expenses (name, category, amount, date) VALUES (?, ?, ?, ?)", 
                  (name, category, amount, date))
        print(f"Added expense: {name} - {amount} - {category} - {date}")
from tabulate import tabulate

def view_expenses():
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Category", "Amount", "Date"], tablefmt="grid"))
    else:
        print("No expenses found.")
def delete_expense(expense_id):
    with conn:
        c.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        print(f"Deleted expense with ID: {expense_id}")

if __name__ == "__main__":
    menu()
