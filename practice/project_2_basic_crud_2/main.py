from db import Storage
db = Storage()

def create_user():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))
    is_active = input("Active (yes/no): ") == "yes"
    notes = input("Notes (optional): ") or None

    data = {
        "name": name,
        "age": age,
        "salary": salary,
        "is_active": is_active,
        "notes": notes
    }

    insert_user = db.insert_user(data)
    return insert_user

def update_user():
    user_id = input("Enter user id: ")
    col_name = input("Enter feild name: ")
    col_val = int(input("Enter feild value: "))

    data = {
        "col_name": col_name,
        "col_val": col_val,
    }

    update_user = db.update_user(user_id, data)
    return update_user



def _main_flow():
    print("1. Create User")
    print("2. View Users")
    print("5. View User By user data: name, id")
    print("4. Update User")
    print("5. Delete User")

    choice = input("Enter choice(1,2,3,4): ")

    match choice:
        case "1":
            print(create_user())
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case _: #default
            print("Please select between 1 - 4.")
            exit()

if __name__ == "__main__":
    print("Welcome to USER inventory!")
    _main_flow()
    db.create_table()