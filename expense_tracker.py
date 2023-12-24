import uuid
from datetime import datetime, timezone

#implementing expense class
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow().replace(tzinfo=timezone.utc)
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow().replace(tzinfo=timezone.utc)

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

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]


# Example usage:

# Creating an Expense
expense1 = Expense("airpod", 500.0)
expense2 = Expense("Power Bank", 1000.0)

# Updating the Expense
expense1.update(amount=60.0)

# Creating an Expense Database
expense_db = ExpenseDatabase()

# Adding Expenses to the Database
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)
expense_db.add_expense(Expense("Phone", 15000.0))
expense_db.add_expense(Expense("Laptop", 20000.0))

# Removing an Expense from the Database
expense_db.remove_expense(expense1.id)

# Getting an Expense by ID
retrieved_expense = expense_db.get_expense_by_id(expense_db.expenses[2].id)

# Getting Expenses by Title
expenses_by_title = expense_db.get_expenses_by_title("Power Bank")

# Getting the Database as a List of Dictionaries
database_as_dict = expense_db.to_dict()

# Printing the results
print("Retrieved Expense by id:")
print(retrieved_expense.to_dict() if retrieved_expense else "Expense not found")

print("\nExpenses by Title:")
for expense in expenses_by_title:
    print(expense.to_dict())

print("\nDatabase as Dict:")
for entry in database_as_dict:
    print(entry)