import requests
import pandas as pd
from get_home.get_home_module import send_gmail
from django.http import HttpResponse
import time
    

def get_homes(request):  # request 인수 추가
    url = "https://soco.seoul.go.kr/youth/pgm/home/yohome/bbsListJson.json"
    
    body = {
        "accept":"application/json, text/javascript, */*; q=0.01",
        "connection":"keep-alive",
        "content-length":"74",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "bbsId": "BMSR00015",
        "pageIndex":1
    }
    while True:
      res = requests.post(url, data=body)
      res_json = res.json()
      resultList = res_json.get("resultList", [])
      df = pd.DataFrame(resultList)
      df=df[["nttSj", "optn1", "optn4"]]
      df.columns = ["공고명", "모집시작일", "모집마감일"]
      cur_time = time.strftime("%Y-%m-%d", time.gmtime(time.time() + 9 * 3600))
      if cur_time in df:
      # if cur_time not in df:  #test
          return send_gmail(df)
      else:
         day = 24 * 60 * 60
         time.sleep(day)

      
      
