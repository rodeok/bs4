import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = "https://www.amazon.com/Apple-Mini-Chip-256GB-Storage/dp/B08TDNXTVK/ref=sr_1_1?crid=3K1Y6SW8XS7C0&keywords=mac+mini&qid=1663876353&sprefix=mac+minii%2Caps%2C1670&sr=8-1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id = "productTitle")
   
    price = soup.find(id = "priceblock_ourprice")
    # converted_price = float(price[0:5])
    converted_price = [0,5]
    converted_price.sort()

    # if (converted_price < 1.700):
    #         send_mail()
    for price in converted_price:
        if price in converted_price:
           print(price)
           send_mail()
    print(converted_price)
    print(title.strip())   

    if (converted_price < 1.700):
        send_mail()     
def send_mail():
    server = smtplib.SMTP_SSL("smtp.gmail.com") 
    # server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("nationx22@gmail.com", "kqrrnyfwlbivvgcm")
    subject ="Price fell down"
    body = "Check the amazon Link" + URL
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "nationx22@gmail.com"
        "nationx23@gmail.com",
        msg
    )
    print("Email sent")
    server.quit()
while(True):
    check_price()
    time.sleep(60*60)