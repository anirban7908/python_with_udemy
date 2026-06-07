import datetime as dt
import pandas
import random
import glob
import smtplib

EMAIL = "dummy1email.for.practice@gmail.com"
PASSWORD = "tznlptgbjjdlygxn"

today = dt.datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today_tuple in birthdays_dict:
    letter_count = len(glob.glob("letter_templates/*.txt"))
    bday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, letter_count)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=bday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n {contents}",
        )
