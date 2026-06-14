import tkinter as tk
from tkinter import ttk

# --- Data Storage ---
expenses = []


def add_expense():
    # Retrieve the data from the fields
    amount = amount_entry.get()
    category = category_combobox.get()
    date = date_entry.get()
    notes = notes_entry.get()

    # Bundle the data into a dictionary
    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "notes": notes
    }

    # Append the new expense to our list
    expenses.append(expense)

    # Print the updated list to the console to verify it works
    print(f"--- Expense Added! Total records: {len(expenses)} ---")
    print(expenses, "\n")

    # Clear the fields after adding
    amount_entry.delete(0, tk.END)
    category_combobox.set('')
    date_entry.delete(0, tk.END)
    notes_entry.delete(0, tk.END)


# --- Main Window Setup ---
root = tk.Tk()
root.title("Expense Entry")
root.geometry("320x250")
root.config(padx=20, pady=20)

# --- Form Fields ---

# 1. Amount
tk.Label(root, text="Amount:").grid(row=0, column=0, sticky="w", pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, pady=5)

# 2. Category (Using Combobox)
tk.Label(root, text="Category:").grid(row=1, column=0, sticky="w", pady=5)
categories = ["Food", "Transport", "Utilities", "Entertainment", "Shopping", "Other"]
category_combobox = ttk.Combobox(root, values=categories)
category_combobox.grid(row=1, column=1, pady=5)

# 3. Date
tk.Label(root, text="Date:").grid(row=2, column=0, sticky="w", pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1, pady=5)
date_entry.insert(0, "YYYY-MM-DD")  # Placeholder text

# 4. Notes
tk.Label(root, text="Notes:").grid(row=3, column=0, sticky="w", pady=5)
notes_entry = tk.Entry(root)
notes_entry.grid(row=3, column=1, pady=5)

# --- Add Expense Button ---
add_button = tk.Button(root, text="Add Expense", command=add_expense, width=15)
add_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()