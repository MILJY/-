#!/usr/bin/python
import requests
import init

headers={
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44)  (Immersed/48) WKWebview ZJYXYwebviewbroswer ZJYXYIphone tourCustomer /yunmaapp.NET/2.5.8/0E9337E9-DA97-44BD-82AA-5FBED31C39E0",
    "Cookie": "shiroJID=9c439439-6f08-4381-9c49-15071876cc8c"
}

def setData(name,json):
    data=json
    print(data)
    # data['loginUserId']=init.userId[name]
    # data['uuToken']=init.uuToken[name]
    # data['loginSchoolCode']=init.loginSchoolCode
    # data['loginSchoolName']=init.loginSchoolName
    # data['temperature']=init.temperature
    # data['address']=init.locationInfo
    # data['locationInfo']=init.locationInfo
    # data['longitudeAndLatitude']=init.longitudeAndLatitude
    # requests.packages.urllib3.disable_warnings()
    # resp = requests.post("https://h5.xiaofubao.com/marketing/health/doDetail", headers=headers, data=data,verify=False)
    # print(resp.json())
#/home/user/yixiaoyuan/run.py
#/usr/bin/python3

def getData(userId):
    data={
        "userId": userId,
    }
    requests.packages.urllib3.disable_warnings()
    resp=requests.post("https://h5.xiaofubao.com/marketing/health/getDetail", headers=headers, data=data, verify=False)
    return resp.json()

if __name__=='__main__':
    for name in init.userId:
        json=getData(init.userId[name])
        #print(json)
        if(json['success']==True):
            setData(name,json['data'])
