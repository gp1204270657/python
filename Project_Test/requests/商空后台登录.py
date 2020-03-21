#coding=utf-8
import requests
#登录地址
url="http://shop.mwee.cn/msk/api/shop.login"
#验证码地址
# url_version="https://auth.mwee.cn/picture/getPicture?code=9HsVXllJRQqUBaDW8AVKag-Z-Z"

session=requests.Session()

data={
    "access-token": "27bkd6kditghefm5ipd66esuv3",
    "page-token": "27bkd6kditghefm5ipd66esuv3",
    "password": "U2FsdGVkX1/G5MYjQl8mq/fpRSUWa4ruXNaM5lLaztU=",
    "picCode": "dxpf",
    "remember": "2",
    "type": "1",
    "username": "mwtydadmin"
}
# r=requests.post(url=url,data=data.,cookies=r_cookies)
r=session.post(url=url,data=data)
r2=session.get("http://shop.mwee.cn/bmanage/index")
print(r2.text)
