import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,"html.parser")

print(soup.title)
print(soup.a.name)
print(soup.a.parent.name)

tag = soup.a
print(tag.attrs)
print(tag.attrs['class'])
print(tag.attrs['href'])

print(soup.a)
print(soup.a.string)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))

#print(soup.prettify())
