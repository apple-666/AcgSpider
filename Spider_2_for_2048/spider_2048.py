import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

views_list = []
src_list = []
title_list = []

headers = {
    # 'Connection': 'close',
    'Cookie': 'zh_choose=n; a22e7_jobpop=0; a22e7_winduser=VVYGVwkGVjlVDFFWBQwGVl0NVVQCVwACVVEBAwVRUFpUVFQIVVdTBzEHVVMCUgpXDFsB; a22e7_ck_info=/	; a22e7_readlog=,8725945,; PHPSESSID=0e2o242i5fis30f4h12pirumm4; a22e7_threadlog=,180,; a22e7_ol_offset=125422; a22e7_lastpos=other; a22e7_lastvisit=283	1670650542	/2048/search.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


def get_all():
    # https://bbs.linkshar.com/2048/thread.php?fid-180-page-1.html
    src1 = "https://bbs.linkshar.com/2048/thread.php?"

    search_str = 'HS'
    cnt = 0
    all_label_list = []

    for i in range(1, 300):
        print("now page is:" + str(i))
        src2 = "fid-180-page-" + str(i) + ".html"
        a_src = src1 + src2
        response = None
        while True:
            try:
                response = requests.get(a_src, headers=headers, timeout=3)
                break
            except:
                time.sleep(3)

        # response = requests.get(a_src, headers=headers, timeout=(3, 10))

        response.encoding = 'utf-8'
        text = response.text
        soup = BeautifulSoup(text, 'lxml')

        # 爬 class='views'的span标签
        # label_list = soup.find_all('a', class_='subject')
        # all_label_list += label_list
        all_label_list += soup.find_all('a', class_='subject')

    fileOb = open('../Spider_2_for_2048/result_' + search_str + '.word', 'a+', encoding='utf-8')
    for j in all_label_list:
        # https://bbs.linkshar.com/2048/
        label_str = j.string
        if (label_str is None): continue
        if (label_str.find(search_str) != -1):
            cnt = cnt + 1
            label_href = j['href']
            label_all_href = "https://bbs.linkshar.com/2048/" + label_href
            res = label_str + " -> " + label_all_href
            fileOb.write(str(cnt) + "\n")
            fileOb.write(str(res) + "\n")
    fileOb.close()


if __name__ == "__main__":
    # 测试
    # src = "https://bbs.linkshar.com/2048/thread.php?fid-180-page-1.html"
    # response = requests.get(src,headers=headers)
    # response.encoding = 'utf-8'
    # text = response.text
    # print(text)

    # time.sleep(5*3600)
    get_all()
