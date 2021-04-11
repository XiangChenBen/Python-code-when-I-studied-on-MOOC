import requests
def getHTMLText(url):
    keyword = "Python"
    try:
        kv = {'q':keyword}
        r = requests.get(url,params = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[0:5000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "http://www.so.com/s"
    print(getHTMLText(url))