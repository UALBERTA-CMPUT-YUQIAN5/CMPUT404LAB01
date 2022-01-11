import requests

print(requests.__version__)

#r = requests.get('http://google.com/')
r= requests.get("https://raw.githubusercontent.com/yuqian5/CMPUT404LAB01/master/request_version.py")

print(r)
print(r.text)
