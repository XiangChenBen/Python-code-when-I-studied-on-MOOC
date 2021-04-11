import requests
import os
url = "http://img0.imgtn.bdimg.com/it/u=3027344830,1524599412&fm=26&gp=0.jpg"
root = "C://Users//BenBen//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exsits(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")