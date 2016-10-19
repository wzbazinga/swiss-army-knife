#encoding=utf8
#created by wz in 2016.10.16
#run this script(with your username and password) and get your run distance increased in Swjtu!

import requests,time
import base64,random
import json

def main(id,pwd):
    url='http://gxapp.iydsj.com/api/v2/users/66776/running_records/add'
    cipher=base64.b64encode(id+':'+pwd)
    headers={
        "appVersion": "1.2.0",
        #"CustomDeviceId": "2846994D72F85D6DBDA5ECDD0C6236EA",
        #"DeviceId": "358610714658547",
        #"osType": "0",
        #"source": "000049",
        #"uid": "66776",
        "Authorization":"Basic "+cipher
    }
    dis=random.random()*3+2
    dis=(float(int(dis*1000))/1000)
    speed=(6+random.random()*3)
    duringtime=dis*speed*60
    starttime=time.time()*1000
    stoptime=starttime+duringtime
    dis="%.06f"%dis
    speed="%.06f"%speed
    jsonContent={
        "isUpload":"false",
        "totalTime":duringtime,
        "totalDis":dis,
        "speed":speed,
        "stopTime":int(stoptime),
        "startTime":int(starttime),
        "sportType":1,
        "selDistance":2,
        "complete":"true",
        "unCompleteReason":0
    }
    s=requests.Session()
    r=s.post(url,headers=headers,json=jsonContent)
    jsonobj=json.loads(r.content)
    print jsonobj['error']

if __name__=='__main__':
    main('','')#write your username and password there
