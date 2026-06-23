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
    amount_entry.delete(0, tk.END)
    category_combobox.set('')
    date_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)

load_expenses()
root = tk.Tk()
root.title("Expense Entry")
root.geometry("320x250")
root.config(padx=20, pady=20)
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
add_button = tk.Button(root, text="Add Expense", command=add_expense, width=15)
add_button.grid(row=4, column=0, columnspan=2, pady=20)
root.mainloop()