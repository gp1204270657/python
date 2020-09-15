import requests
import json
url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=2330f4ce-434b-4fd0-bba3-17bb612e88be"

json={
  "msgtype": "text",
  "text": {
    "content": "hello,我是渣渣辉"
  }
}
def test():
    res=requests.post(url,json=json)
    return res

if __name__ == '__main__':

    test()