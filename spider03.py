# # -*- coding: UTF-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re
import time

url = 'https://www.zhihu.com/question/22918070'
html = request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all(
    'img', 'origin_image zh-lightbox-thumb', src=re.compile(r'.jpg$'))

path = r'./img'
for link in links:
    print(link.attrs['src'])
    request.urlretrieve(link.attrs['src'], path+'\%s.jpg' % time.time())
