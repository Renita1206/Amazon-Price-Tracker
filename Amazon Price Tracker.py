import requests
from bs4 import BeautifulSoup
import smtplib

def checkPrice():
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    url="https://www.amazon.in/Logitech-Lightspeed-Wireless-Gaming-Mouse/dp/B07G98H6PM/ref=psdc_1375415031_t2_B019OB663A"
    page=requests.get(url, headers=header)
    soup=BeautifulSoup(page.content, 'html.parser')
    price=soup.find(id='priceblock_dealprice').get_text().strip()[1:]
    price=price.replace(',','')
    price=float(price)
    if(price<2000):
        sendMail(price)
    print("Logitech G402 Mouse: ",price)

def sendMail(p):
    server=smtplib.SMTP('smtp.gmail.com', 587) # to establish server connection
    server.ehlo() # establishes connection between email servers
    server.starttls() # for encryption
    server.ehlo()
    server.login('bluecoder1206@gmail.com','###')
    subject="Logitech G402 Mouse"
    body="Check Amazon now!!! \n Price is"+str(p)+"\n https://www.amazon.in/Logitech-Lightspeed-Wireless-Gaming-Mouse/dp/B07G98H6PM/ref=psdc_1375415031_t2_B019OB663A"
    message=f"Subject: {subject}\n\n{body}"
    server.sendmail('bluecoder1206@gmail.com', 'rrenita1206@gmail.com', message)
    server.quit()
    print("Mail sent")

checkPrice()
