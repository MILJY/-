import requests

first_url="https://www.pearvideo.com/video_1757328"
vid=first_url.split('_')[-1]
second_url=f"https://www.pearvideo.com/videoStatus.jsp?contId={vid}&mrd=0.6240469995677524"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
    "Referer": first_url
}

resp=requests.get(second_url,headers=headers)
dic=resp.json()

systemTime=dic['systemTime']
srcUrl=dic['videoInfo']['videos']['srcUrl']
srcUrl=srcUrl.replace(systemTime,f"cont-{vid}")

video_name=srcUrl.split("/")[-1]
video_resp=requests.get(srcUrl)
with open("img/"+video_name,mode="wb") as f:
    f.write(video_resp.content)
f.close()

