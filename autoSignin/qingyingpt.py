#encoding=utf-8
#created by wz in 2016.10.16

#Add this script in your cron daemon(in linux) and get your qingyingpt bonus increased automatically!

import requests

def main(username,password):
    url='http://pt.hit.edu.cn/takelogin.php'
    data={
        "username":username,
        "password":password,
        "returnto":""
    }
    s=requests.session()
    r=s.post(url,data=data)

    url='http://pt.hit.edu.cn/take_signin_bonus.php'
    header={"Referer":"https://pt.hit.edu.cn/index.php"}
    r=s.get(url,params=header)
    print r.status_code
    if r.content=='-1':
        url='https://pt.hit.edu.cn/take_signin_bonus.php?redate=1'
        rr=s.get(url)

if __name__=='__main__':
    print 'start qingyingpt singin'
    main('','')
