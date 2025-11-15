print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip/100
bill_with_tip = bill+(bill*tip_percent)
total = bill_with_tip/people
round_num = round(total, 2)
print(f"Your total bill with {tip}% of tip is: {round_num}")


