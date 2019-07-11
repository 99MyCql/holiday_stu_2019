# python3爬虫进阶之构建自己的代理池
# https://blog.csdn.net/wwq114/article/details/88254296
# 
# 



import requests
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
    }




url = 'http://www.xicidaili.com/nn'
response = requests.get(url,headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')
ip_list = soup.find(id='ip_list').find_all('tr')
for i in range(1, len(ip_list)):
    ip_info = ip_list[i]
    tds = ip_info.find_all('td')
    ip = tds[1].text + ':' + tds[2].text
    print(ip)


# 验证
import requests, json, re, random, time
from bs4 import BeautifulSoup


def loadPage(url, headers):
    req = requests.get(url, headers=headers)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    ip_list = soup.find(id='ip_list').find_all('tr')
    for i in range(1, len(ip_list)):
        ip_info = ip_list[i]
        tds = ip_info.find_all('td')
        ip = tds[1].text + ':' + tds[2].text
        # 验证ip是否可用
        if verify_IP(ip, headers):
            # 将可用ip存入文件
            dir_file = open("ip_records.txt", 'a', encoding="utf-8")
            dir_file.write(ip + "\n")
            dir_file.close()
            time.sleep(5)

def verify_IP(ip, headers):
    proxies = {"http": ip}
    url = "http://www.baidu.com/"
    try:
        req = requests.get(url, headers=headers, proxies=proxies, timeout=3)
        if req.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print("IP" + ip + "不可用 :")
        print(e)
        return False


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
    }
    url = 'http://www.xicidaili.com/nn'
    loadPage(url,headers)   