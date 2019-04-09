from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

all_divs = soup.find_all('span', attrs={'class': 'num2'})
date_span = soup.find('span', attrs={'id': 'time3'})

date = [span.string for span in date_span]

res = [span.string for span in all_divs]
res.append(date[0])
for i in res:
    print(i)
