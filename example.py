#importing the classes created from the expense.py file 
from expense import Expense
from expense import ExpenseDatabase

#creating instances of expenses
expense1 = Expense("Phone", 350000)
expense2 = Expense("airpod", 50000)
expense3 = Expense("Headphones", 15000)
expense4 = Expense("Laptop", 750000)

#updating an expense values
expense3.update(title="Jbl speaker",amount=46000)
expense1.update(amount=450000)

#initializing the database
expense_db = ExpenseDatabase()

# Adding each expense to the database
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)
expense_db.add_expense(expense3)
expense_db.add_expense(expense4)

# Getting the Database as a List of Dictionaries
database_as_dict = expense_db.to_dict()


# Getting Expenses by Title and ID
expenses_by_title = expense_db.get_expenses_by_title("airpod")
expenses_by_id = expense_db.get_expense_by_id(expense3.id)

# Removing an Expense from the Database
expense_db.remove_expense(expense1.id)

# getting an updated expense database list after removal of an item
database_as_dict = expense_db.to_dict()