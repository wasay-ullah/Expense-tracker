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
    expense_table.insert("",tk.END,values=(date,category,amount,notes))
    # Print the updated list to the console to verify it works
    print(f"--- Expense Added! Total records: {len(expenses)} ---")
    print(expenses, "\n")

    # Clear the fields after adding
    amount_entry.delete(0, tk.END)
    category_combobox.set('')
    date_entry.delete(0, tk.END)
    date_entry.insert(0, "YYYY-MM-DD")
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
root.geometry("500x450")
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
# Run the application
root.mainloop()
