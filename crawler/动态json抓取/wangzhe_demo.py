'''
抓取王者荣耀所有英雄的皮肤
'''
import requests

# 英雄列表
herolist_url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(herolist_url).json()
print(herolist)

# 皮肤图片的url(有规律)
pic_base = 'https://game.gtimg.cn/images/yxzj/img201606/heroimg/{}/{}-smallskin-{}.jpg'

for hero in herolist:
    for i in range(9):
        url = pic_base.format(hero['ename'], hero['ename'], i)
        res = requests.get(url)
        # print(type(res.status_code), res.status_code)
        if res.status_code != 200:
            continue
        pic_name = 'pic-{}-{}.jpg'.format(hero['cname'], i)
        file = open('王者英雄皮肤/' + pic_name, 'wb')
        file.write(res.content)
        file.close()
