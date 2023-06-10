import tkinter as tk
from tkinter import messagebox

class Transaction:
    def _init_(self, name, amount):
        self.name = name
        self.amount = amount

class KhatabookApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Khatabook App")

        # Create and configure your GUI elements
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack()

        self.record_button = tk.Button(self, text="Record", command=self.record_transaction)
        self.record_button.pack()

        self.transactions_text = tk.Text(self)
        self.transactions_text.pack()

        self.transactions = []  # Store recorded transactions

        self.load_transactions()  # Load transactions from file
        self.update_transactions_text()  # Update the transactions text display

        self.selected_transaction = None  # Track selected transaction for editing

        self.edit_button = tk.Button(self, text="Edit", command=self.edit_transaction)
        self.edit_button.pack()

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_transaction)
        self.delete_button.pack()

        self.protocol("WM_DELETE_WINDOW", self.save_transactions)  # Save transactions to file on app exit

    def record_transaction(self):
        name = self.name_entry.get()
        amount = self.amount_entry.get()

        # Validate input
        if name and amount:
            try:
                amount = float(amount)  # Convert amount to a float
                transaction = Transaction(name, amount)

                # Add the transaction to the list
                self.transactions.append(transaction)

                # Clear the entry fields
                self.name_entry.delete(0, tk.END)
                self.amount_entry.delete(0, tk.END)

                # Update the transactions text display
                self.update_transactions_text()
            except ValueError:
                self.show_error("Invalid amount. Please enter a valid number.")
        else:
            self.show_error("Please fill in both name and amount fields.")

    def update_transactions_text(self):
        # Clear the existing text in the transactions text widget
        self.transactions_text.delete("1.0", tk.END)

        # Iterate through the transactions and display them in the text widget
        for i, transaction in enumerate(self.transactions, start=1):
            transaction_info = f"{i}. Name: {transaction.name}\tAmount: {transaction.amount}"
            self.transactions_text.insert(tk.END, transaction_info + "\n")
            
            def edit_transaction(self):
        selected_index = self.get_selected_index()
        if selected_index is not None:
            self.selected_transaction = self.transactions[selected_index]

            # Set the name and amount in the entry fields for editing
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_transaction.name)
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(tk.END, self.selected_transaction.amount)

    def delete_transaction(self):
        selected_index = self.get_selected_index()
        if selected_index is not None:
            # Remove the selected transaction from the list
            del self.transactions[selected_index]

            # Clear the selection
            self.selected_transaction = None

            # Clear the entry fields
            self.name_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)

            # Update the transactions text display
            self.update_transactions_text()

    def get_selected_index(self):
        selected_text = self.transactions_text.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            selected_index = int(selected_text.split(".")[0]) - 1
            return selected_index
        return None

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def save_transactions(self):
        with open("transactions.txt", "w") as file:
            for transaction in self.transactions:
                file.write(f"{transaction.name},{transaction.amount}\n")

    def load_transactions(self):
        try:
            with open("transactions.txt", "r") as file:
                for line in file:
                    name, amount = line.strip().split(",")
                    transaction = Transaction(name, float(amount))
                    self.transactions.append(transaction)
        except FileNotFoundError:
            pass


if _name_ == "_main_":
    app = KhatabookApp()
    app.mainloop()
    
    # Add this code after the `load_transactions` method in Part 2

def sort_by_name(self):
    self.transactions.sort(key=lambda transaction: transaction.name)
    self.update_transactions_text()

def sort_by_amount(self):
    self.transactions.sort(key=lambda transaction: transaction.amount)
    self.update_transactions_text()

def filter_transactions(self):
    filtered_transactions = []
    # Implement filtering logic based on the selected criteria (name or amount range)
    # Append the filtered transactions to the `filtered_transactions` list
    # Update the `self.transactions` list with the filtered transactions
    # Call `self.update_transactions_text()` to display the filtered transactions

def search_transactions(self):
    search_query = self.search_entry.get()
    if search_query:
        matched_transactions = []
        # Implement search logic to find transactions that match the search query
        # Append the matched transactions to the `matched_transactions` list
        # Update the `self.transactions` list with the matched transactions
        # Call `self.update_transactions_text()` to display the matched transactions

def export_transactions(self):
    file_path = "transactions.csv"  # Set the desired file path and format
    with open(file_path, "w") as file:
        # Implement the logic to write transactions to a CSV or Excel file
        pass

def import_transactions(self):
    file_path = "transactions.csv"  # Set the file path from where to import transactions
    with open(file_path, "r") as file:
        # Implement the logic to read transactions from a CSV or Excel file
        pass
    
    # Add this code after the methods in Part 3

def authenticate(self):
    username = self.username_entry.get()
    password = self.password_entry.get()

    # Implement the logic to validate the entered credentials
    # If the credentials are valid, grant access to the app
    # Otherwise, display an error message or take appropriate action

def change_theme(self):
    # Implement the logic to change the app's theme
    # You can explore Tkinter's theming capabilities and apply the desired theme

class KhatabookApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Khatabook App")

        # ... Rest of the code ...

        # Additional GUI elements for advanced features
        self.sort_name_button = tk.Button(self, text="Sort by Name", command=self.sort_by_name)
        self.sort_name_button.pack()

        self.sort_amount_button = tk.Button(self, text="Sort by Amount", command=self.sort_by_amount)
        self.sort_amount_button.pack()

        self.filter_button = tk.Button(self, text="Filter", command=self.filter_transactions)
        self.filter_button.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.search_transactions)
        self.search_button.pack()

        self.export_button = tk.Button(self, text="Export", command=self.export_transactions)
        self.export_button.pack()

        self.import_button = tk.Button(self, text="Import", command=self.import_transactions)
        self.import_button.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.authenticate)
        self.login_button.pack()

        self.theme_button = tk.Button(self, text="Change Theme", command=self.change_theme)
        self.theme_button.pack()
        
        # Add this code after the methods in Part 4

class KhatabookApp(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Khatabook App")

        # ... Rest of the code ...

    def save_transactions(self):
        with open("transactions.txt", "w") as file:
            for transaction in self.transactions:
                file.write(f"{transaction.name},{transaction.amount}\n")

    def load_transactions(self):
        try:
            with open("transactions.txt", "r") as file:
                for line in file:
                    name, amount = line.strip().split(",")
                    transaction = Transaction(name, float(amount))
                    self.transactions.append(transaction)
        except FileNotFoundError:
            pass

        self.update_transactions_text()

    def update_transactions_text(self):
        # ... Rest of the code ...

        # Apply any additional filtering or sorting on the transactions before displaying them

if _name_ == "_main_":
    app = KhatabookApp()
    app.mainloop()