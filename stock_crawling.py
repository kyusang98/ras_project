import requests
from bs4 import BeautifulSoup as bs

url = 'https://finance.naver.com/sise/lastsearch2.naver'
response = requests.get(url)
html_text = response.text
html = bs(html_text, 'html.parser')


names=html.select('tr a')
updowns=html.select('tr td span')
#print(names)
#print(updowns)

name_list=[]

for name in names:
    name_list.append(name.text)

dictionary = {}

i=0
for updown in updowns:
    if i%2==1:
       dictionary[name_list[i//2]]=updown.text.replace('\n\t\t\t\t','')
    i+=1    

