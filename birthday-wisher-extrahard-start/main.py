##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import glob

def fetch_letter():
    letters = glob.glob("letter_templates/*.txt")
    if letters:
        chosen_letter = random.choice(letters)
    
    return chosen_letter

def create_letter(letter):
    with open(letter, "r") as file:
        letter_content = file.readlines()

        if "[NAME]" in letter_content:
            

bday_data = pandas.read_csv("birthdays.csv")
bday_dict = bday_data.to_dict(orient="records")
# print(bday_dict)

today = dt.datetime.now()
current_month = today.month
current_day = today.day


bday_persons = []

for data in bday_dict:
    # print(current_month)
    # print(data['month'])
    # print(current_day)
    # print(data['day'])
    if current_month == int(data['month']) and current_day == int(data['day']):
        details = {
            "name": data['name'],
            "email": data['email'],
        }
        bday_persons.append(details)

if bday_persons != None:
    letter = fetch_letter()
    print(letter)

