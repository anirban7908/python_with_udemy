import smtplib
import datetime as dt
import random
my_email = "dummy1email.for.practice@gmail.com"
password = "tznlptgbjjdlygxn"

def send_mail(quote):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="anirban.choudhury.7908@gmail.com", 
            msg=f"Subject: Quote \n\n {quote}"
        )

with open("quotes.txt", "r") as file:
    content = file.readlines()

    
selected_content = random.choice(content)
now = dt.datetime.now()
week_day = now.weekday()

if week_day == 0:
    send_mail(selected_content)
else:
    print(week_day)