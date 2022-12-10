# python3.6环境
import browser_cookie3

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'
}


if __name__ == '__main__':
    # 自动获取cookie
    url = 'https://www.acgdv.com/page/2/'

    cj = browser_cookie3.chrome(domain_name='www.acgdv.com')
    r = requests.get(url,cookies=cj).text
    print(r)
