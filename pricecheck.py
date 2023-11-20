import requests
from bs4 import BeautifulSoup as bs
import webbrowser,time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edge/96.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}
def Tracker1(link):  
    page = requests.get(link,headers=headers)
    soup = bs(page.content, 'html.parser')

    price=soup.find('div',class_='_30jeq3 _16Jk6d')
    rate = str(price.text)
    d=''
    for i in rate:
      if i.isdigit() == True:
        d+=i
    if int(d)<500:
        webbrowser.open(link)
        inty=input("Do it again :")
    else:
      print("Mehenga ",d)
link="https://www.flipkart.com/havells-bt5301-trimmer-100-min-runtime-20-length-settings/p/itm907e3f01dba63"
while True:
    Tracker1(link)
    time.sleep(2)
    
