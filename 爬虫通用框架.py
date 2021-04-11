import requests
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[0:1000]
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://www.coursehero.com/file/p71cusk/Utility-has-a-standard-deviation-of-40-percent-and-the-return-on-the-Commodity/"
    print(getHTMLText(url))