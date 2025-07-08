import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
from datetime import datetime

url="https://www.asahi.com/?iref=pc_gnavi&_klpuid=GwKq2LGpnkQhX6L36mXkc"
res=requests.get(url)
res.encoding=res.apparent_encoding
soup=BeautifulSoup(res.text)

contents=soup.find_all("div",class_="l-section p-genre")
rows=[]
for content in contents:
    boxes = content.find_all("div", class_="c-articleModule p-listModule__item")
    for box in boxes:        
        title = box.find("h2", class_="c-articleModule__title")
        time = box.find("time")
        rows.append([
            title.text.strip() if title else "",
            time.text.strip() if time else ""
        ])
#date 
now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
rows.append(["scraped at", now, ""])
rows.append(["-----------------------"]) 

#CSV output
with open ("asahi_articles.csv", "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "time"])
    writer.writerows(rows)