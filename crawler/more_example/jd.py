import requests
from lxml import etree
from urllib.parse import quote
import time
import csv

# https://www.jianshu.com/p/2cdaf1b4ec11

#定义函数抓取每页前30条商品信息
def crow_first(n):
    #构造每一页的url变化
    url = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page='.format(quote("手机"))
    ref = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={1}&cid2=653&cid3=655&page=3&s=58&click=0'.format(quote("手机"),quote("手机"))

    url=url+str(2*n-1)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            #'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
            'scheme': 'https',
            'referer': ref,
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
             }
    r = requests.get(url, headers=head)
    #指定编码方式，不然会出现乱码
    r.encoding='utf-8'
    #print(r.text)
    html1 = etree.HTML(r.text)
    #定位到每一个商品标签li
    datas=html1.xpath('//li[contains(@class,"gl-item")]')
    #print(len(datas))  # 30个li
    #将抓取的结果保存到本地CSV文件中
    with open('JD_Phone.csv','a',newline='',encoding='utf-8')as f:
        write=csv.writer(f)
        for data in datas:
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            #p_comment = data.xpath('div/div[contains(@class,"p-commit")]/strong/a/@href')
            p_comment = data.xpath('div/div[contains(@class,"p-commit")]/strong/a/text()')
            #  [contains(@id,”ma”) and contains(@id,”in”)]
            #p_comment = data.xpath('div/div[contains(@class,"p-commit) and contains(@data-done, "1")]/strong/a/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')
            
            #这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
                #xpath('string(.)')用来解析混夹在几个标签中的文本
            print("first:",p_price, p_comment, p_name)
            #write.writerow([p_name[0],p_price[0],p_comment[0]])
     #f.close()
#定义函数抓取每页后30条商品信息
def crow_last(n):
    #获取当前的Unix时间戳，并且保留小数点后5位
    a=time.time()
    b='%.5f'%a
    
    url = 'https://search.jd.com/s_new.php?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={1}&cid2=653&cid3=655&page='.format(quote("手机"),quote("手机"))
    ref = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={1}&cid2=653&cid3=655&page=3&s=58&click=0'.format(quote("手机"),quote("手机"))
    
    url=url+str(2*n)+'&s='+str(48*n-20)+'&scrolling=y&log_id='+str(b)
    head={'authority': 'search.jd.com',
    'method': 'GET',
    #'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA',
    'scheme':'https',
    'referer': ref,
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
     }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    
    with open('JD_Phone.csv','a',newline='',encoding='utf-8')as f:
        write=csv.writer(f)
        for data in datas:
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            #p_comment = data.xpath('div/div[5]/strong/a/text()')
            p_comment = data.xpath('div/div[contains(@class,"p-commit")]/strong/a/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')
            
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
            print("last:", p_price, p_comment, p_name)
            #write.writerow([p_name[0].xpath('string(.)'),p_price[0],p_comment[0]])
    #f.close()
 
 
if __name__=='__main__':
    for i in range(1,2):
        #下面的print函数主要是为了方便查看当前抓到第几页了
        print('***************************************************')
        try:
            print('   First_Page:   ' + str(i))
            crow_first(i)
            print('   Finish')
        except Exception as e:
            print(e)
        print('------------------')
        try:
            print('   Last_Page:   ' + str(i))
            crow_last(i)
            print('   Finish')
        except Exception as e:
            print(e)