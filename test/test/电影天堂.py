import requests
import re

#获取主界面html代码
domain="https://dytt89.com/"
resp=requests.get(domain, verify=False)
resp.encoding='gb2312'

child_hreflist=[]

obj1=re.compile(r'2022必看热片.*?<ul>(?P<test>.*?)</ul>',re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3=re.compile(r'◎片　　名　(?P<movie_name>.*?)<br />'
                r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)"',re.S)

result1=obj1.search(resp.text)
context=result1.group('test')
result2=obj2.finditer(context)

for it in result2:
    child_href=domain+it.group('href').strip('/')
    child_hreflist.append(child_href)

for href in child_hreflist:
    child_resp=requests.get(href,verify=False)
    child_resp.encoding='gb2312'
    result3=obj3.finditer(child_resp.text)
    for it in result3:
        print(it.group('movie_name')+"\n"+it.group('download'))


