from requests_html import HTMLSession
session=HTMLSession()
url='http://www.zzuli.edu.cn/'
r=session.get(url)
print(r.html.html)