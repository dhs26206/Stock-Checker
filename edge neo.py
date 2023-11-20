import requests
from bs4 import BeautifulSoup as bs
import webbrowser,time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edge/96.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}
link="https://www.flipkart.com/search?q=edge+40+neo&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_7_0_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_7_0_na_na_na&as-pos=7&as-type=HISTORY&suggestionId=edge+40+neo%7CMobiles&requestId=5a244f4a-e88c-4f16-a9af-8ffec1acf553&p%5B%5D=facets.internal_storage%255B%255D%3D128%2B-%2B255.9%2BGB"
link2="https://www.flipkart.com/search?q=moto+g54&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D15000&p%5B%5D=facets.ram%255B%255D%3D8%2BGB%2Band%2BAbove"

page = requests.get(link2,headers=headers)
soup = bs(page.content, 'html.parser')
spans_with_bg_class = soup.find_all('span', class_='u05wbu')
spans = soup.find_all('span', class_='_192laR')

def check(link):
    page = requests.get(link,headers=headers)
    soup = bs(page.content, 'html.parser')
    coming = soup.find_all('span', class_='u05wbu')
    spans = soup.find_all('span', class_='_192laR')
    
    if len(coming)+len(spans)<3:
        webbrowser.open(link)
        yt=input("Do it again")
    else:
        print("Working")

while True:
    check(link)
    time.sleep(2)
    
    
