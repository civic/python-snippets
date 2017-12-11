import requests
from bs4 import BeautifulSoup

res = requests.get('https://python.civic-apps.com/scraping-example1.html')

soup = BeautifulSoup(res.content, 'html.parser')

# li要素を検索してtext要素を出力
for elm in soup.find_all('li'):
    print(elm.string)

# 最初のli要素のtextを取得
print(soup.find('li').string)       # findは最初の要素のみ
print(soup.find_all('li')[0].string)  


# id指定でフィルタ
print("id指定でフィルタ")
for elm in soup.find('div', id='main').find_all('li'):
    print(elm.string)
for elm in soup.select('div#main li'):
    print(elm.string)

# class指定でフィルタ
print("class指定でフィルタ")
for elm in soup.find('div', id='main').find_all('li', class_='even'):
    print(elm.string)
for elm in soup.select('div#main li.even'):
    print(elm.string)

# 属性指定でフィルタ
print("属性指定でフィルタ")
for elm in soup.find('div', id='main').find_all('li', data='3'):
    print(elm.string)
for elm in soup.find('div', id='main').find_all('li', attrs={'data':'3'}):  #上記の汎用版
    print(elm.string)
for elm in soup.select('div#main li[data="3"]'):
    print(elm.string)

# 直下の子要素指定でフィルタ
print("直下の子要素指定でフィルタ")
print(soup.find('div', id='main').div)   #bbbな子要素も含まれる

print(soup.select_one('div#main > div'))

# 属性取得
print("属性取得")
for elm in soup.find_all('li'):
    print(elm['data'])
for elm in soup.select('li::attr(data)'):
    print(elm)
