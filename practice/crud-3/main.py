from connection import DbConnection
from datetime import datetime


def operation():
    print("Press 1 for view users")
    print("Press 2 for add user")
    print("Press 3 for update user")
    print("Press 4 for delete user")
    print("Press 5 for exit")
    user_choice = input("Please choose a operation: ")
    return user_choice


while True:
    user_choice = operation()

    try:
        choice = int(user_choice)
        pass
    except ValueError:
        print("invalid input.")

