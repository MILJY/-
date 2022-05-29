import requests

data={
    "loginName": "18274813418",
    "password": "NISHIZHUMA520"
}

session=requests.session()

url='https://passport.17k.com/ck/user/login'
resp1=session.post(url, data=data)
#print(resp.cookies)

resp2=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp2.json())


