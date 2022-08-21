import requests
# import browser_cookie3
from bs4 import BeautifulSoup



views_list = []
src_list = []
title_list = []

headers = {
    # 'Connection': 'close',
    'Cookie':'_ga_035Y5V78G7=GS1.1.1659787934.7.1.1659787951.0; _ga=GA1.1.488399047.1658852273; RQ0=449e68ef86c18834b28f4ef04bece85d; wordpress_logged_in_04a99aa7758f858f70ccfd0c61f580b5=appleD%7C1660232971%7C3szKIX2a3NEdiLORwk29qSzszUyGW5ByVvkSOYRlOip%7C806aab364b3de512b1a746ce495ab6bcea20b106a169df9dcbe5817c6b68381e',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'
}

def save(text):
    fileOb = open('gett2.txt', 'w', encoding='utf-8')
    fileOb.write(text)

def get_all():
    src1 = "https://www.acgdv.com/page"
    for i in range(100,352):

        src2 = "/"+str(i)+"/"
        a_src = src1 + src2

        # 自动获取chrome cookie
        # cj = browser_cookie3.chrome()
        # text = requests.get(a_src, cookies=cj).text
        # print(a_src)
        text = requests.get(a_src, headers=headers).text
        # print(text)
        soup = BeautifulSoup(text, 'lxml')
        # print("4"+soup)
        # 爬 class='views'的span标签
        span_list = soup.find_all('span', class_='views')
        # print(span_list)
        for j in span_list:
            if(j.text[-1]=='+'):
                views_list.append(j.text[1:-2])
            else:
                views_list.append(j.text[1:-1])

        # 爬 属性itemprop=url的 a标签
        a_list = soup.find_all("a", {"itemprop": {"url"}, "rel": {"bookmark"}})
        # 获取a标签中的 title和href属性
        for j in a_list:
            title = j.attrs['title']
            src = j.attrs['href']
            title_list.append(title)
            src_list.append(src)
    # print(views_list)

    ## 保存到文件 要把数组转换成string
    # 筛选出 适合的view
    # 1: >=10  2: [8.8,10) 3:[8,8.8)  4：[7,8)
    fileOb = open('Get2_2.word', 'w', encoding='utf-8')
    for i in range(0,len(views_list)):
        if(float(views_list[i])>=7.0 and float(views_list[i])<8) :
            res = title_list[i] + ":" + views_list[i] + " -> " + src_list[i]
            fileOb.write(str(res)+"\n")
    fileOb.close()

if __name__ == "__main__":
    src = "https://www.acgdv.com/page/3/"
    response = requests.get(src,headers=headers)
    text = response.text
    # content = response.content

    # cj = browser_cookie3.chrome()
    # text = requests.get(src, cookies=cj).text

    # print(text)
    # save(text)

    # soup = BeautifulSoup(response.text,'lxml')
    get_all()


