import tkinter as tk
from tkinter import messagebox, ttk
import os
import json
import matplotlib.pyplot as plt
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.expense_data = defaultdict(list)
        self.load_data()

        # GUI Elements
        self.amount_var = tk.StringVar()
        self.desc_var = tk.StringVar()
        self.category_var = tk.StringVar()

        # Frame for input
        input_frame = ttk.LabelFrame(root, text="Add New Expense", padding=(10, 10))
        input_frame.grid(row=0, column=0, padx=10, pady=10)

        ttk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.amount_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        ttk.Entry(input_frame, textvariable=self.desc_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        categories = ["Food", "Transportation", "Entertainment", "Others"]
        ttk.Combobox(input_frame, textvariable=self.category_var, values=categories).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(input_frame, text="Add Expense", command=self.add_expense).grid(row=3, column=1, padx=5, pady=10, sticky=tk.E)

        # Frame for display and analysis
        display_frame = ttk.LabelFrame(root, text="Expenses", padding=(10, 10))
        display_frame.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.tree = ttk.Treeview(display_frame, columns=("Amount", "Description", "Category"), show='headings')
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Category", text="Category")
        self.tree.grid(row=0, column=0, sticky="nsew")
        display_frame.grid_rowconfigure(0, weight=1)
        display_frame.grid_columnconfigure(0, weight=1)

        self.update_display()

        # Analysis Frame
        analysis_frame = ttk.LabelFrame(root, text="Data Analysis", padding=(10, 10))
        analysis_frame.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        ttk.Button(analysis_frame, text="Show Monthly Summary", command=self.show_summary).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(analysis_frame, text="Show Category-wise Expenditure", command=self.show_category_wise).grid(row=0, column=1, padx=5, pady=5)

    def add_expense(self):
        amount = self.amount_var.get().strip()
        description = self.desc_var.get().strip()
        category = self.category_var.get().strip()

        if not amount or not description or not category:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning("Input Error", "Amount must be a number")
            return

        expense = {"amount": amount, "description": description, "category": category}
        self.expense_data[category].append(expense)
        self.save_data()
        self.update_display()
        self.clear_inputs()

    def clear_inputs(self):
        self.amount_var.set("")
        self.desc_var.set("")
        self.category_var.set("")

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for category, expenses in self.expense_data.items():
            for expense in expenses:
                self.tree.insert("", "end", values=(expense['amount'], expense['description'], category))

    def save_data(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expense_data, file, indent=4)

    def load_data(self):
        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expense_data = defaultdict(list, json.load(file))

    def show_summary(self):
        monthly_total = sum(expense['amount'] for expenses in self.expense_data.values() for expense in expenses)
        messagebox.showinfo("Monthly Summary", f"Total Expenses: {monthly_total}")

    def show_category_wise(self):
        categories = list(self.expense_data.keys())
        amounts = [sum(expense['amount'] for expense in self.expense_data[category]) for category in categories]

        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.title("Category-wise Expenditure")
        plt.xlabel("Category")
        plt.ylabel("Total Amount")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
