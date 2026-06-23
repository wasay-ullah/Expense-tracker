import tkinter as tk
from tkinter import ttk
import json
import os

expenses = []


def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)


def load_expenses():
    global expenses
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as f:
            expenses = json.load(f)


def update_total():
    """Calculates the sum of all expenses and updates the total label."""
    total = 0.0
    for expense in expenses:
        try:
            # Convert string amount to float. Ignores invalid text entries.
            total += float(expense["amount"])
        except ValueError:
            pass

    # Update the label text
    total_label.config(text=f"Total Expenses: Rs. {total:.2f}")


def add_expense():
    amount = amount_entry.get()
    category = category_combobox.get()
    date = date_entry.get()
    notes = notes_entry.get()

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "notes": notes
    }

    expenses.append(expense)
    save_expenses()
    expense_table.insert("", tk.END, values=(date, category, amount, notes))

    # Update the total label
    update_total()

    # Clear the fields after adding
    amount_entry.delete(0, tk.END)
    category_combobox.set('')
    date_entry.delete(0, tk.END)
    date_entry.insert(0, "YYYY-MM-DD")
    notes_entry.delete(0, tk.END)


def delete_expense():
    """Deletes the selected row from the UI, the list, and the JSON file."""
    selected_item = expense_table.selection()

    # If nothing is selected, do nothing
    if not selected_item:
        return

    # Get the specific item clicked
    item = selected_item[0]

    # Get the row index in the Treeview to match our expenses list
    index = expense_table.index(item)

    # 1. Remove from the underlying list
    del expenses[index]

    # 2. Remove from the visual Treeview table
    expense_table.delete(item)

    # 3. Save the updated list to JSON
    save_expenses()

    # 4. Update the total label
    update_total()


# Load data into memory on startup
load_expenses()

# --- Main Window Setup ---
root = tk.Tk()
root.title("Expense Entry")
root.geometry("500x500")  # Slightly taller to fit the total label
root.config(padx=20, pady=20)

# --- Form Fields ---
tk.Label(root, text="Amount:").grid(row=0, column=0, sticky="w", pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Category:").grid(row=1, column=0, sticky="w", pady=5)
categories = ["Food", "Transport", "Utilities", "Entertainment", "Shopping", "Other"]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.grid(row=1, column=1, pady=5)

tk.Label(root, text="Date:").grid(row=2, column=0, sticky="w", pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1, pady=5)
date_entry.insert(0, "YYYY-MM-DD")

tk.Label(root, text="Notes:").grid(row=3, column=0, sticky="w", pady=5)
notes_entry = tk.Entry(root)
notes_entry.grid(row=3, column=1, pady=5)

# --- Buttons ---
# Reorganized into row 4 next to each other
add_button = tk.Button(root, text="Add Expense", command=add_expense, width=15)
add_button.grid(row=4, column=0, pady=15)

delete_button = tk.Button(root, text="Delete Selected", command=delete_expense, width=15)
delete_button.grid(row=4, column=1, pady=15)

# --- Table Setup ---
columns = ("date", "category", "amount", "notes")
expense_table = ttk.Treeview(root, columns=columns, show="headings", height=8)
expense_table.heading("date", text="Date")
expense_table.heading("category", text="Category")
expense_table.heading("amount", text="Amount")
expense_table.heading("notes", text="Notes")

expense_table.column("date", width=90, anchor="center")
expense_table.column("category", width=100, anchor="center")
expense_table.column("amount", width=80, anchor="e")
expense_table.column("notes", width=170, anchor="w")

expense_table.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")
root.grid_columnconfigure(1, weight=1)

# --- Total Expenses Label ---
total_label = tk.Label(root, text="Total Expenses: Rs. 0.00", font=("Arial", 12, "bold"))
total_label.grid(row=6, column=0, columnspan=2, pady=5)


# --- Populate Data & Initialize Total ---
def populate_table():
    for expense in expenses:
        expense_table.insert("", tk.END, values=(
            expense.get("date", ""),
            expense.get("category", ""),
            expense.get("amount", ""),
            expense.get("notes", "")
        ))


# Fill the table and calculate initial totals before starting
populate_table()
update_total()

# Run the application
root.mainloop()