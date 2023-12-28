# Expense Tracker

Expense Tracker is a simple Python project that uses object-oriented programming (OOP) techniques to track and monitor financial expenses. It is divided into two classes, `Expense` and `ExpenseDatabase`, which allow users to make individual expenses as well as manage a collection of expenses.

## Project Structure

The project contains two python file:

- expense.py file
- example.py file

### expense.py file contains
- Implementation of Expense class
- Implementation ExpenseDatabase class
  
### example.py file contains
- sample code usage

## Requirements

- Python 3.x
- an Integrated Development Environment (IDE) like VSCode

## How to Clone

To clone the repository, use the following command:

```
git clone https://github.com/opeyemiloc/expense_tracker_python.git
```

## How to Run

To run this code, you can follow these general steps using an IDE like VSCode:
**Note:** Visual Studio Code (VSCode) is suggested for convenience and popularity, but you are free to use any IDE you are comfortable with.

### Using an IDE (e.g., VSCode):

1. **Install Python:**
   Make sure you have Python installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Install VSCode:**
   If you don't have VSCode installed, you can download it from the [VSCode website](https://code.visualstudio.com/download).

3. **Open the Project:**
   - Open Visual Studio Code (VSCode).
   - Click on "File" > "Open Folder" and select the folder containing your Python scripts (`expense.py` and `example.py`).

4. **Prepare the Environment:**
   - Create a new empty Python file in the same folder where `expense.py` and `example.py` are located.

5. **Import Classes from `expense.py`:**
   - Open the empty Python file and import the classes created in `expense.py` by adding the following lines:
     ```python
     from expense import Expense
     from expense import ExpenseDatabase
     ```

6. **Use the Classes:**
   - You can now make use of the methods of each class from expense.py in your Python script. Refer to the `example.py` file for a quick guide on how to use the codebase.

7. **Run the Code:**
   - Locate the "Run" button in the toolbar (usually a right-facing triangle or "Run Python File in Terminal") at the top right side of the VSCode interface.
   - Click the "Run" button to execute the code in your new Python script.

8. **Check `example.py` for Usage Information:**
   - For additional information on how to use the codebase, refer to the `example.py` file. It contains sample usage of the classes and methods provided in `expense.py`.

## Example Usage

Here are a few snippets from `example.py` to illustrate how to use the `Expense` and `ExpenseDatabase` classes:

```python
# Importing the classes created from the expense.py file
from expense import Expense
from expense import ExpenseDatabase

# Creating an expense
expense1 = Expense("Phone", 350000)
expense2 = Expense("airpod", 50000)

# Creating an expense database
expense_db = ExpenseDatabase()

# Adding expenses to the database
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)

# Retrieving expenses added to the database
expense_list = expense_db.to_dict()


