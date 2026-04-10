def create_user_flow():
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

    from api import handle_post
    handle_post(data)

def menu():
    print("1. Create User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")

    choice = input("Enter choice: ")

    if choice == "1":
        create_user_flow()

    elif choice == "2":
        from db import get_users
        print(get_users())

    elif choice == "3":
        user_id = int(input("Enter ID: "))
        name = input("Enter new name: ")

        from db import update_user
        update_user(user_id, name)

    elif choice == "4":
        user_id = int(input("Enter ID: "))

        from db import delete_user
        delete_user(user_id)

if __name__ == "__main__":
    from db import create_table
    create_table()

    while True:
        menu()
        will_continue = input("Want to continue? (Y/N) ").lower()
        if will_continue == 'n':
            exit() 