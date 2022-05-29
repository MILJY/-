# from urllib.request import urlopen
#
# url="http://www.baidu.com"
# resp=urlopen(url)
#
# with open("mybaidu.html",mode="w",encoding="utf-8") as f:
#     f.write(resp.read().decode("utf-8"))
# print("over!")

import requests
# url='https://www.baidu.com/s?wd=薛之谦'
# dic={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
# }
# resp=requests.get(url, headers=dic)
# resp.encoding="utf-8"
# print(resp.text)

# url='https://fanyi.baidu.com/sug'
# s=input("输入查询的英文单词")
# dat={
#     "kw": s
# }
# resp=requests.post(url, data=dat)
# print(resp.json())

url="https://movie.douban.com/j/chart/top_list"
param={
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"
}
resp=requests.get(url=url, params=param, headers=headers)
print(resp.json())
resp.close()