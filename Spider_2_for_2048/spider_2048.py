
import time

import requests
from bs4 import BeautifulSoup

views_list = []
src_list = []
title_list = []

headers = {
    # 'Connection': 'close',
    'Cookie': 'zh_choose=n; PHPSESSID=sigju88l2o9a2f1011qmm4e9r5; TDC_itoken=1348855191:1619163262; a22e7_winduser=VVYGVwkGVjlVDFFWBQwGVl0NVVQCVwACVVEBAwVRUFpUVFQIVVdTBzEHVVMCUgpXDFsB; a22e7_ck_info=/	; TDC_itoken=1348855191:1619163262; a22e7_readlog=,8640493,8640492,904093,8640398,8641683,8144421,8321833,8591128,7098841,; a22e7_threadlog=,136,3,271,180,; a22e7_ol_offset=112618; a22e7_lastpos=other; a22e7_lastvisit=136	1670608890	/2048/post.php?action=modify&fid=180&tid=8725039&pid=tpc&article=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}



def get_all():
    # https://bbs.linkshar.com/2048/thread.php?fid-180-page-1.html
    src1 = "https://bbs.linkshar.com/2048/thread.php?"

    fileOb = open('../Spider_2_for_2048/result.word', 'w', encoding='utf-8')
    cnt = 0
    for i in range(1, 5000):
        print("now page is:" + str(i))
        src2 = "fid-180-page-" + str(i) + ".html"
        a_src = src1 + src2
        response = None
        while True:
            try:
              response = requests.get(a_src, headers=headers, timeout=(3, 10))
              break
            except:
              time.sleep(5)

        # response = requests.get(a_src, headers=headers, timeout=(3, 10))

        response.encoding = 'utf-8'
        text = response.text

        # print(text)
        soup = BeautifulSoup(text, 'lxml')

        # 爬 class='views'的span标签
        label_list = soup.find_all('a', class_='subject')
        for j in label_list:
            # https://bbs.linkshar.com/2048/
            label_str = j.string
            if (label_str is None): continue
            if (label_str.find('VAM') != -1):
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

    time.sleep(5*3600)
    get_all()
