import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs4
import requests
from pprint import pprint as pp
import smtplib

# List of amazon urls

# URL_LISTS = ["https://appbrewery.github.io/instant_pot/"]

# ================================= Env variables ==========================
load_dotenv()
smtp_email = os.getenv('SMTP_ADDRESS')
from_email = os.getenv('FROM_EMAIL_ADDRESS')
to_email = os.getenv('TO_EMAIL_ADDRESSES')
password = os.getenv('EMAIL_PASSWORD')
# print(from_email)
# print(to_email[0])
# print(password)
# exit()
# ============================== Helper functions ============================
def send_email(title, price):
    '''This function will send email to the email addresses provided in the env file'''
    print("Email sending start!")
    body = f"{title} from amazon is now available in {price}"
    with smtplib.SMTP(smtp_email, 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=f"Subject: Low Price for your product. \n\n {body.encode('utf-8')}"
        )
    print("\nEmail sending end!")


# ================================= Web Scraping Amazon ===================================


# amazon_dummy_url = "https://appbrewery.github.io/instant_pot/"
amazon_product_url = "https://www.amazon.in/Stanley-70-379E-Finish-Spanner-8-Piece/dp/B00ICIKIIG/ref=sr_1_43?_encoding=UTF8&content-id=amzn1.sym.2eab8373-f2e6-4b01-97aa-c5592db6ec60&dib=eyJ2IjoiMSJ9.XIeGaeSMmVMsCd2w9N2m-oKhSHmGla8dG6t3uuGi9pADcGbHscTMA2SM-a0YidTD0jVynwg9pVZOTZrBenKCUyvY00QDIwYiaRUxRkoRc0LrIdHHU3iFcDeLo409DZRc3lWoE9PZmZXHqfl0J7QsKVmUnNa_353kHRpVf0GsxgYOGagbIJyxsEY90TSyx5HYFAYxMAg6ZKqpZKUQR9NAVXwJBCpNXzcRMoLUOmbDwNvktVJyqZnNq8kf073h6CmE8Wr3CDCIxqyZcOW0O7O4RBEtAS-9UKkhGjcC3N8TONA.DcYfj_NtrmqeuXW3b52cErD7yFAo_aUTjsNm7_y5z70&dib_tag=se&pd_rd_r=652fa3f2-1e1c-4469-b3f7-9b779a650ff8&pd_rd_w=W5OSS&pd_rd_wg=WfxxB&qid=1783964622&refinements=p_36%3A3444810031%2Cp_72%3A1318476031&s=kitchen&sr=1-43&xpid=RIaTyV81mxVnv&th=1"

headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0"
}
response = requests.get(amazon_product_url, headers=headers)
response.raise_for_status()

raw_website = response.text

soup = bs4(raw_website, "html.parser")



raw_product_title = soup.find('span', id="productTitle")
product_title = " ".join(raw_product_title.text.split())


raw_price = soup.find("span", class_="a-offscreen").text
product_price = raw_price.replace("₹", "").strip()

# raw_product_image = soup.find(id="landingImage")
# product_image_src = raw_product_image.get("src")
# print(product_image_src)
# exit()
if float(product_price) < float(400):
    print(f'Low price found for {product_title}: {product_price}! \n Sending email now... \n')
    send_email(product_title, product_price)


