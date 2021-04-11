import requests
url = "http://img0.imgtn.bdimg.com/it/u=3027344830,1524599412&fm=26&gp=0.jpg"
path = "C://Windows"
r = requests.get(url)
print(r.status_code)
with open(path,'wb') as f:
    f.write(r.content)
f.close()