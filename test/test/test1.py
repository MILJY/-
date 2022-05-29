import csv
import requests
import re
url="https://movie.douban.com/top250"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}
param={
    "start": 0,
    "filter": ""
}
resp=requests.get(url, headers=headers,params=param)
text=resp.text
obj=re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<br>(?P<year>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
               r'.*?<span>(?P<num>.*?)人评价</span>',re.S)
result=obj.finditer(text)
f=open("data.csv", mode='w', encoding='utf-8', newline='')
fwrite=csv.writer(f)
for it in result:
    dic=it.groupdict()
    dic['year']=dic['year'].strip()
    fwrite.writerow(dic.values())
f.close()
resp.close()
print("over!")