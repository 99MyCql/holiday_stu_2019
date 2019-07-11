# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:04:25 2019

@author: guojige
"""
# 1.导入相关包
from bs4 import BeautifulSoup
import requests

# 2. 用户代理设置
# 扩展，使用用户代理池、IP代理池
# 第一级链接地址 
url = 'http://fjdj.fjsen.com/'
headers1 = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'Host':'fjdj.fjsen.com',  # 这里注意，Host为网站首页
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}
res = requests.get(url, headers=headers1)
res.encoding = 'utf-8'
html = res.content
#print(html)

# 3. 解析，可以bs，也可用xpath
bs = BeautifulSoup(html, 'html.parser')

# 4. 选择   信息刊用排行榜
lm3 = bs.find("div", attrs={'class':'lm-3'})
print(lm3.text)

# 5. div lm-3  下面的 div ph
ph = bs.find("div", attrs={'class':'ph'})
ph2 = ph.next_sibling  # 兄弟
#print(ph, ph2)

# 6. 或者直接查找  ui  paihang ->  所有 li
paihang = bs.find(name='ul', attrs={'id':'paihang'})
#print(paihang)
lis  = paihang.find_all(name='li')
print(len(lis))   # 输出为0
#  则这部分内容是空的， js

# 查看 script,结果为
#  $.getJSON('http://api.media.fjsen.com/n/api.php?act=getbypid&pid=169514&limit=6&jsoncallback=?'
# 在浏览器 network-> js  找到该url，然后通过headers获取详细地址
#http://api.media.fjsen.com/n/api.php?act=getbypid&pid=169514&limit=6&jsoncallback=jQuery19103439815077136912_1559960667102&_=1559960667103

# 综上说明，子连接是通过js异步加载的，可通过找到相应的json文件获取

# 7. json的连接地址。
urljson = 'http://api.media.fjsen.com/n/api.php?act=getbypid&pid=169514&limit=6&jsoncallback=jQuery19103439815077136912_1559960667102&_=1559960667103'


# 8. 抓取json的headers
headers2 = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'Host':'api.media.fjsen.com',  # # 这里注意，Host 这些信息根据观察浏览器headers得来
               'Referer': 'http://fjdj.fjsen.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

# 9.抓包
import json

res = requests.get(urljson, headers=headers2)
print(res.status_code)
res.encoding = 'utf-8'

# 10. 取出 json文件开头部分和末尾部分
text = res.text.lstrip('jQuery19103439815077136912_1559960667102(')
text = text.rstrip(')') 
#print(text)

# 11. 将json文件转换为字典结构
items = json.loads(text)
#print(items)

# 12. 基本url+子连接，得到新的网址，{}是占位符
newurl = url+"node_{}.htm"

info = []

# 13. 从字典中取出关键信息，名称和url
for item in items:
    title = item['nodename']
    eurl = newurl.format(item['nid'])
    #print(title, eurl)
    info.append({"title":title, "url":eurl})
    
print(info)
# 14. 保存到文件中，以便进行内容下载
with open('info.json','w',encoding='utf-8') as file:
    json.dump(info,file)

