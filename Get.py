from imp import reload

import requests
from bs4 import BeautifulSoup

def getDet(respon):
    result = []
    soup = BeautifulSoup(respon, "lxml")
    # 查找所有class属性为hd的div标签
    span_list = soup.find_all('span', class_='views')
    # 获取每个div中的a中的span（第一个），并获取其文本
    for each in span_list:
        tem = each.text.strip()
        result.append(tem)

    return result

def getAll():
    fileOb = open('all.txt', 'w', encoding='utf-8')
    i = 1
    src = "https://www.acgdv.com/page/"
    for i in range(1,352):
        a_src = src + str(i)+"/"
        text = requests.get(a_src,headers=headers).text
        fileOb.write(text)

    fileOb.close()

headers = {
    'Cookie':'_ga_035Y5V78G7=GS1.1.1659018763.2.1.1659018933.0; _ga=GA1.1.488399047.1658852273; RQ0=7847dd77b0770a858e4c8d6586f20537',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'
}


# response = requests.get("https://www.acgdv.com/page/1/",headers=headers)
# print(response.text)
# soup = BeautifulSoup(response,'lxml')
# print(soup.find_all('span'))
# print(response.headers)
# all_response = getAll()
getAll()

# fileOb = open('all.txt','w',encoding='utf-8')     #打开一个文件，没有就新建一个
# fileOb.write(htmldata)
# fileOb.close()
# ans = getDet(response.text)
# print(ans)
