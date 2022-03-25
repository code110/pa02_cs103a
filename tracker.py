'''
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''

from transactions import Transaction
from category import Category
import sys

transactions = Transaction('tracker.db')
category = Category('tracker.db')

# here is the menu for the tracker app

menu = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''


def process_choice(choice):
    if choice == '0':
        return
    elif choice == '1':
        cats = category.select_all()
        print_categories(cats)
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.update(rowid, cat)
    elif choice == '4':  # Junhao Wang
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice == '5':  # Junhao Wang
        amount = input("amount: ")
        name = input("category: ")
        date = input("date: ")
        desc = input("description: ")
        trans = {'amount': amount, 'category': name, 'date': date, 'desc': desc}
        transactions.add(trans)
    elif choice == '6':  # Junhao Wang
        rowid = int(input("rowid: "))
        transactions.delete(rowid)
    elif choice == '7':  # Junhao Wang
        trans = transactions.sum_date()
        print_sum_date(trans)
    elif choice == '8':  # Junhao Wang
        trans = transactions.sum_month()
        print_sum_month(trans)
    elif choice == '9':  # Junhao Wang
        trans = transactions.sum_year()
        print_sum_year(trans)
    elif choice == '10':  # Junhao Wang
        trans = transactions.sum_cat()
        print_sum_cat(trans)
    elif choice == '11': # zihao liu
        print(menu)
    else:
        print("invalid choice")

    choice = input("> ")
    return (choice)


def toplevel():
    ''' handle the user's choice '''

    ''' read the command args and process them'''
    print(menu)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')


#
# here are some helper functions
#

def print_transactions(items):
    ''' print the transactions '''
    if len(items) == 0:
        print('no items to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-15s %-30s" % (
        'item #', 'amount', 'category', 'date', 'description'))
    print('-' * 60)
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10s %-10s %-15s %-30s" % values)


def print_sum_date(items):
    print("%-10s %-10s" % ("sum", "date"))
    print('-' * 45)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10s" % values)


def print_sum_month(items):  # Junhao Wang
    print("%-10s %-10s" % ("sum", "month"))
    print('-' * 45)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10s" % values)


def print_sum_year(items):  # Junhao Wang
    print("%-10s %-10s" % ("sum", "year"))
    print('-' * 45)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10s" % values)


def print_sum_cat(items):  # Junhao Wang
    print("%-10s %-10s" % ("sum", "category"))
    print('-' * 45)
    for item in items:
        values = tuple(item.values())
        print("%-10d %-10s" % values)


def print_category(cat):
    print("%-3d %-10s %-30s" % (cat['rowid'], cat['name'], cat['desc']))


def print_categories(cats):
    print("%-3s %-10s %-30s" % ("id", "name", "description"))
    print('-' * 45)
    for cat in cats:
        print_category(cat)


# here is the main call!

toplevel()
