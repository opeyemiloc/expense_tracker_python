#importing neccessary libraries
import uuid
from datetime import datetime, timezone



#implementing expense class section
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow().replace(tzinfo=timezone.utc)
        self.updated_at = self.created_at
        print("\nyour expense has been created sucessfully.")

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)
        print("\nyour expense value has been updated sucessfully.")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


#implementing expensedatabase class
class ExpenseDatabase:
    def __init__(self):
        self.expenses = []
        print("\nExpense database created successfully.")

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("\nExpense added successfully")

    def remove_expense(self, expense_id):
            for expense in self.expenses:
                if expense.id == expense_id:
                    self.expenses.remove(expense)
                    print(f"Expense with ID {expense_id} removed successfully.")
                    return 
            print(f"Expense with ID {expense_id} not found.")
         
    def get_expense_by_id(self, expense_id):
        matching_expenses = [expense for expense in self.expenses if expense.id == expense_id]
        if not matching_expenses:
            print(f"\nNo expenses found with ID '{expense_id}'.")
        else:
            print(f"\nMatching expenses with ID '{expense_id}':")
            for expense in matching_expenses:
                print(f"ID: {expense.id}, Amount: {expense.amount}, Title: {expense.title}")
        return matching_expenses
    
    def get_expenses_by_title(self, expense_title):
        matching_expenses = [expense for expense in self.expenses if expense.title == expense_title]
        if not matching_expenses:
            print(f"\nNo expenses found with title '{expense_title}'.")
        else:
            print(f"\nMatching expenses with title '{expense_title}':")
            for expense in matching_expenses:
                print(f"ID: {expense.id}, Amount: {expense.amount}, Title: {expense.title}")
        return matching_expenses

    def to_dict(self):
        print("\nCreating dictionary...")
        result = [expense.to_dict() for expense in self.expenses]
        print("Database as Dict:")
        print("\nShowing current stored expenses")
        for entry in result:
            print(entry)
            print("\n")
        return result



