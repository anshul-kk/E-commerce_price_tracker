import requests
from bs4 import BeautifulSoup
import smtplib
import csv
import datetime
import os
import time



def send_email():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("keshavkekatpure007@gmail.com","cywrjworlyapfsjj")

    subject= "Hey! The prices are affordable"
    body = f"Go and order now at {url} "
    msg = f"Subject:{subject}\n\n\n\n{body}"

    server.sendmail("keshavkekatpure007@gmail.com","keshavkekatpure2002@gmail.com",msg)
    print("email sent")
    server.quit()






url = "https://www.amazon.in/Nikon-20-9MP-Camera-18-140mm-3-5-5-6G/dp/B06Y5RTN1T/ref=sr_1_1?keywords=camera%2Bnikon%2Bd7500&qid=1656773960&sprefix=camera%2Bnikon%2B%2Caps%2C270&sr=8-1&th=1"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}
def check_price_and_log():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(bs.prettify().encode("utf-8"))

    product_title = soup.find(id = "productTitle").get_text()
    product_title = str(product_title)
    product_title = product_title.strip()
    print(product_title.strip())

    ele = soup.find("div", class_="a-section a-spacing-none aok-align-center")
    product_price = ''
    product_price = soup.find("span", class_="a-offscreen").get_text()
    # product_price = bs.find(id = "priceblock_ourprice").get_text()


    product_price = product_price[1:9]
    print(product_price)

    price_float = float(product_price.replace(",",""))
    # print(price_float)


    file_exists = True

    if not os.path.exists("./price.csv"):
        file_exists = False

    with open("price.csv","a") as file:
        writer = csv.writer(file,lineterminator ="\n")
        fields = ["Timestamp","price"]
        
        if not file_exists:
            writer.writerow(fields)

        timestamp = f"{datetime.datetime.date(datetime.datetime.now())},{datetime.datetime.time(datetime.datetime.now())}"
        writer.writerow([timestamp, price_float])
        print("wrote csv data")

    return price_float




while True:
    price = check_price_and_log()
    if(price <= 92000.00):
        send_email()
        break
    time.sleep(43200)
