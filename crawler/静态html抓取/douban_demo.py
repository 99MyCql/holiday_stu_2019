import requests
from lxml import etree

url = 'https://www.douban.com/doulist/1798248/'

res = requests.get(url)
res.encoding = 'utf-8'
html = etree.HTML(res.text)

article = html.xpath('//*[@id="content"]/div/div[1]')
print(article)

movies = article[0].xpath('.//div[@class="doulist-item"]')
print(movies)

file = open('历届奥斯卡最佳动画长片(2002——2019).txt', 'w', encoding='utf-8')
for movie in movies:
    title = movie.xpath('.//div[@class="title"]/a/text()')
    print(title)
    file.write('标题:')
    for i in title:
        file.write(i.replace(' ', '').replace('\n', ''))
    file.write('\n')
    
    abstract = movie.xpath('.//div[@class="abstract"]/text()')
    print(abstract)
    file.write('摘要:')
    for i in abstract:
        file.write(i.replace(' ', '').replace('\n', ''))
        file.write('\n')

    rating = movie.xpath('.//div[@class="rating"]/span[2]/text()')
    print(rating)
    file.write('评分:' + rating[0] + '\n')

    video_list = movie.xpath('.//div[@class="doulist-video-items"]/a') # 可播放的
    file.write('可播放平台:')
    for video in video_list:
        print(video.xpath('./text()'))
        file.write(video.xpath('./text()')[0] + ' ')
    file.write('\n\n')

    img_src = movie.xpath('.//div[@class="post"]/a/img/@src')
    print(img_src)

file.close()