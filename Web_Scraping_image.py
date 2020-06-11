from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.passiton.com/inspirational-quotes")
url_html = BeautifulSoup(page.content,"html.parser")
#print(url_html)

items = url_html.find(class_ = "container")

#print(items)
#sub_items = url_html.find_all("div", class_="col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top")
#print(sub_items[0])

for div in url_html.find_all("div", class_="col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"):
    #print(div)
    for img1 in div.find_all("img"):
        print()
        quotes = [img1["alt"]]
        print(quotes)
