
import requests
import time
from bs4 import BeautifulSoup
import webbrowser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edge/96.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}
url1="https://www.flipkart.com/motorola-edge-40-neo-caneel-bay-128-gb/p/itm122f351a3a2a3"
def Check(url):
  response = requests.get(url, headers=headers)
  
# Check if the request was successful
  if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Use the CSS selector to select the desired div
    div = soup.select_one("#container > div > div._2c7YLP.UtUXW0._6t1WkM._3HqJxg > div._1YokD2._2GoDe3 > div._1YokD2._3Mn1Gg.col-8-12 > div:nth-child(4) > div._16FRp0")
    print(div)
    # Check if the div is present
    if div:
        print("The div is present on the webpage.")
    else:
        webbrowser.open(url)
        y=input("Do it gain")
  else:
      print("Failed to retrieve the webpage. Status code:", 
    response.status_code)

while(True):
    Check(url1)
    time.sleep(2)
