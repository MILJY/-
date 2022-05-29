import requests
from bs4 import BeautifulSoup
import time

url="https://www.umeitu.com/bizhitupian/weimeibizhi/"

resp=requests.get(url)
resp.encoding='utf-8'

main_page=BeautifulSoup(resp.text, "html.parser")
result=main_page.find("ul",class_="pic-list after").find_all("a")

for it in result:
    child_href='https://www.umeitu.com'+it.get('href')
    child_resp=requests.get(child_href)
    child_resp.encoding='utf-8'
    child_page_text=child_resp.text
    child_page=BeautifulSoup(child_page_text,"html.parser")
    img=child_page.find("div",class_="ImageBody").find("img")
    src=img.get("src")
    img_resp=requests.get(src)
    img_name=src.split("/")[-1]
    with open("img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)
    print(img_name)
    time.sleep(1)


