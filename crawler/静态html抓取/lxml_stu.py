import requests
from lxml import etree

# selector: body > div.wrapper > div > div > div.herolist-box > div.herolist-content > ul > li:nth-child(1)
# JSPath: document.querySelector("body > div.wrapper > div > div > div.herolist-box > div.herolist-content > ul > li:nth-child(1)")
# XPath: /html/body/div[3]/div/div/div[2]/div[2]/ul/li[1]

user_agent = 'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)'
headers = {'User-Agent': user_agent}

url = 'https://go.hao123.com'
res = requests.get(url, headers=headers)

html = etree.HTML(res.text)

# 网页f12查询元素时，右键元素可复制XPATH

# /text() 获取元素的内容
price = html.xpath('/html/body/div[3]/div/div[4]/div[2]/div[1]/div[1]/a[1]/span[1]/text()')
print(price[0])

# // 表示全局搜索
tejia = html.xpath("//div[@class='tejia-air-wrapper']")
print(tejia)

# .// 表示对所有子元素搜索
tejias = tejia[0].xpath('.//div[@class="tejia-air"]')
print(tejias)

for i in tejias:
    a = i.xpath('.//a')
    for j in a:
        # 获取元素的属性
        fromto = j.xpath('./@alog-text')
        price = j.xpath('.//span[@class="tickets-price"]/text()')
        print(fromto, price)