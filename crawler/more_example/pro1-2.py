# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:07:50 2019

@author: guojige
"""
# 15. 导入相关包
from bs4 import BeautifulSoup
import requests
import json

# 16. headers设置
headers1 = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
               'Accept - Encoding':'gzip, deflate',
               'Accept-Language':'zh-Hans-CN, zh-Hans; q=0.5',
               'Connection':'Keep-Alive',
               'Host':'fjdj.fjsen.com',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'}

# 17. 打开json文件获得第二级链接地址
with open('info.json','r',encoding='utf-8') as file:
    infos = json.load(file)    
print(infos)

base = 'http://fjdj.fjsen.com/'

# 18 对排行榜中的每个子链接进行处理
for item in infos:
    # 例如对 平潭综合试验区区直机关 中的所有内容进行处理
    # 19. 抓取数据
    print("抓取", item['title'], item['url'])
    res = requests.get(item['url'], headers=headers1)
    res.encoding = 'utf-8'
    print(res.content)
    # 20. bs页面解析
    bs = BeautifulSoup(res.content, "html.parser")
    # 21. 获取第三级链接地址信息
    uls = bs.find_all(name="ul", attrs={"class":"list_lb"})
    print(len(uls))
    for ul in uls:
        lis = ul.find_all("li")
        for li in lis:
            # 22 第三级链接的地址，党建的实际内容保存
            print("时间:",li.span.text)
            print("标题:",li.a.text)
            print("链接:",base+li.a.attrs['href'])
            # 23. 学生独立完成，根据上述链接地址，下载党建内容
            # 这个可以参考 biqukan.py 小说下载 
            
    # 第二级链接地址，其实有多个
    pages = bs.find(name='div', attrs={'id':'displaypagenum'})
    print(pages['totalcount'])
    #http://fjdj.fjsen.com/node_171900.htm 
    #http://fjdj.fjsen.com/node_171900_5.htm
    
    break


  