import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup

views_list = []
src_list = []
title_list = []

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'zh_choose=n; a22e7_winduser=VVYGVwkGVjlVDFFWBQwGVl0NVVQCVwACVVEBAwVRUFpUVFQIVVdTBzEHVVMCUgpXDFsB; a22e7_ck_info=/	; a22e7_lastpos=F180; a22e7_threadlog=,280,180,; a22e7_lastvisit=0	1670692476	/2048/thread.php?fid-180-page-1.html; a22e7_ol_offset=105731'
}


def get_all():
    # https://bbs.linkshar.com/2048/thread.php?fid-180-page-1.html
    src1 = "https://bbs.linkshar.com/2048/thread.php?"

    # 1,全部的3d 视频：
    #     有 3d          没有 彩漫 VAM
    in_filter = ['3d', '3D']
    nin_filter = ['VAM', '全彩', '图集', '漫画', '篇', '章', '画集', '~', '-', '写真集', '图',
                  '3D乱伦', '3D淫母', '3D伦理', '3D淫妻', '【3D】', '[3D]', 'P/', 'p/']  # p是章节的意思

    # 2,(优先)国动漫 ：
    # 有 国漫/游戏同人 国漫 游戏同人 HS
    # 没有 VAM 全彩
    # in_filter = ['国漫/游戏同人', '国漫', 'HS', '游戏同人']
    # nin_filter = ['VAM', '全彩', '图集', '漫画', 'P/', 'p/']  # p是章节的意思
    #  if(any(i in label_str for i in in_filter) and any(i in label_str for i in nin_filter) is not True):

    # 3,有CV的3d视频
    #
    search_str = 'all_3d'
    cnt = 227
    st_page = 55
    to_page = 5136

    uqi_list = []  # 防止重复列表

    fileOb = open('../Spider_2_for_2048/result_' + search_str + '.word', 'a+', encoding='utf-8')
    session = requests.Session()
    for i in range(st_page, to_page):
        print("now page is:" + str(i) + "   当前共有:" + str(cnt) + " 条成功链接")

        src2 = "fid-180-page-" + str(i) + ".html"
        a_src = src1 + src2
        response = None
        while True:
            try:
                response = session.get(a_src, headers=headers)
                break
            except:
                time.sleep(3)

        # response = requests.get(a_src, headers=headers, timeout=(3, 10))

        response.encoding = 'utf-8'
        text = response.text
        soup = BeautifulSoup(text, 'lxml')

        # while True:
        #     try:
        #         fileOb = open('../Spider_2_for_2048/result_' + search_str + '.word', 'a+', encoding='utf-8')
        #         break
        #     except:
        #         print("等10s再打开文件")
        #         time.sleep(10)

        # 爬 class='views'的span标签
        label_list = soup.find_all('a', class_='subject')
        # all_label_list += label_list
        # all_label_list += soup.find_all('a', class_='subject')

        for j in label_list:
            # https://bbs.linkshar.com/2048/
            label_str = j.string
            if (label_str is None): continue
            # if (label_str.find(search_str) != -1):
            if (any(i in label_str for i in in_filter) and any(i in label_str for i in nin_filter) is not True):
                if (label_str in uqi_list): continue  # 去重
                uqi_list.append(label_str)

                cnt = cnt + 1
                label_href = j['href']
                label_all_href = "https://bbs.linkshar.com/2048/" + label_href
                res = label_str + " -> " + label_all_href
                fileOb.write(str(cnt) + "\n")
                fileOb.write(str(res) + "\n")
        fileOb.flush()
    fileOb.close()


if __name__ == "__main__":
    # 测试
    # src = "https://bbs.linkshar.com/2048/thread.php?fid-180-page-1.html"
    # response = requests.get(src, headers=headers)
    # response.encoding = 'utf-8'
    # text = response.text
    # print(text)

    # time.sleep(5*3600)
    get_all()
