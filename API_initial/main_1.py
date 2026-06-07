import requests
from datetime import datetime
import smtplib
import time

EMAIL = "dummy1email.for.practice@gmail.com"
PASSWORD = "tznlptgbjjdlygxn"

MY_LAT = 22.471497
MY_LNG = 88.421999


def check_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and MY_LNG <= iss_longitude <= MY_LNG + 5
    ):
        return True
    else:
        return False


def is_night():
    params = {"lat": MY_LAT, "lng": MY_LNG, "formatted": 0}

    sun_times_resp = requests.get(
        url="https://api.sunrise-sunset.org/json", params=params
    )
    sun_times_resp.raise_for_status()

    sun_data = sun_times_resp.json()

    time_now = datetime.now().hour
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False
    
while True:
    time.sleep(60)
    if check_iss_position() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(EMAIL, PASSWORD)
            conn.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject: Look in the SKY👆\n\nThe ISS is above you in the SKY!!🌃"
            )
    else:
        print("Try Again☹️")