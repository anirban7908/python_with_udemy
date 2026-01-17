from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def pick_an_operation():
    operations = """"
    +
    -
    *
    /
    """
    operation_selected = input(f"Pick an operation {operations}: ")
    return  operation_selected

operation_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    print(logo)
    first_num = float(input('Please enter your first number: '))
    should_cont = True

    while should_cont:
        for symbol in operation_dict:
            print(symbol)
        operation_symbol = input(f"Pick a symbol: ")
        second_num = float(input('Please enter your next number: '))
        answer = operation_dict[operation_symbol](first_num,second_num)
        print(f"{first_num} {operation_symbol} {second_num} = {answer}")

        choice = input(f"Type 'y' to continue calculation with {answer} or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            first_num = answer
        else:
            should_cont = False
            print("\n" * 20)
            calculator()

calculator()