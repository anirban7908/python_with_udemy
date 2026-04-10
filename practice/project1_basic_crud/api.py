def handle_post(data):
    """
    data = {
        "name": "John",
        "age": 25,
        "salary": 5000.50,
        "is_active": True,
        "notes": None
    }
    """
    from db import insert_user
    insert_user(data)