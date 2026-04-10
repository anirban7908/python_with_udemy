print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("What is your age? "))
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Your Ticket price will be $5")
    elif age <= 18:
        print("Your Ticket price will be $7")
    else:
        print("Your Ticket price will be $12")
else:
    print("Sorry you have to grow taller before you can ride.")
