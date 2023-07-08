# 暴力获取微信7~8大版本的最新小版本
# 耗时比较长,
# 结果最后将在终端呈现

import requests, re
from datetime import datetime


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
url = 'https://dldir1.qq.com/weixin/android/weixin{}android{}.apk'
result_list = {}


def get(v1, v2):
    the_url = url.format(v1, v2)
    response = requests.head(url=the_url, headers=headers)
    result = str(response.status_code)
    c_time = datetime.now().strftime("[%H:%M:%S]")

    if response.status_code == 200:
        the_url = check_update(the_url)

        global result_list
        result_list[v1] = the_url
        print("succeed")
        print(c_time + " " + result + " " + the_url)
        return 1
    else:
        print(c_time + " " + result + " " + the_url)
        return 0


def check_update(the_url):
    r_code = 200
    num = 1
    c_url = the_url
    # 制作新链接
    if re.search(r'_\d+\.apk$', the_url):
        num = int(re.search(r'(\d+)\.apk$', the_url).group(1)) + 1
        url1 = the_url[:-6] + "_{}.apk"
    else:
        url1 = the_url[:-4] + "_{}.apk"

    # 测试链接
    while r_code == 200:
        new_url = url1.format(num)
        r_code = requests.head(url=new_url, headers=headers).status_code
        if r_code == 200:
            num += 1
            c_url = new_url
        else:
            break

    return c_url


def run():
    def run_get_link(start_ver, end_ver, start_ver_code):
        c_ver_code = start_ver_code
        for i in range(start_ver, end_ver):
            for j in range(c_ver_code, c_ver_code + 81):
                r = get(i, j)
                if r:
                    c_ver_code = j
                    pass

    run_get_link(700, 710, 1380)
    run_get_link(7010, 7023, 1580)
    run_get_link(800, 810, 1840)
    run_get_link(8010, 8039, 1960)

    print("结果来咯")
    for i in result_list:
        print(i, result_list[i])


if __name__ == '__main__':
    run()
