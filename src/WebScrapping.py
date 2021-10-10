from bs4 import BeautifulSoup
import requests
import datetime

now = datetime.datetime.now()
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

class Scrapper:
    def get(self, coin_name):
        page = requests.get(
            "https://google.com/search?q=site%3Acoinmarketcap.com+" + coin_name + ", headers=headers")
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find_all("h3")

scrapper = Scrapper()
print("Enter the coin's name")
coin_name = input()
print ("Latest information in market " + str(now) + ": \n")
res = scrapper.get(coin_name)
for i in res:
    print(i.parent.parent.parent.parent.get_text())