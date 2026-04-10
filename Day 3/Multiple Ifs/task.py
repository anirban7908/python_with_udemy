print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets: $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets: $7")
    else:
        bill = 12
        print("Adult tickets: $12")

    want_photos = input("Do you want photos? y for Yes and n for No. ")
    if want_photos == 'y':
        print(f"Your total bill is: {bill + 3} ")
    else:
        print(f"Your total bill is: {bill} ")
else:
    print("Sorry you have to grow taller before you can ride.")
