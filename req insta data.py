import requests
p=input("user id:")
p="https://www.instagram.com/"+p+"/"
req=requests.get(p)
print(req.text)
