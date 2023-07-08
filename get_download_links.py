# 暴力获取微信7~8大版本的最新小版本
# 耗时比较长,可能要半小时
# 结果最后将在终端呈现（划掉）
# 最后结果将在download_links.py呈现
import pprint
from datetime import datetime
from check_and_up import *

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
    result = check_error_link(the_url)
    c_time = datetime.now().strftime("[%H:%M:%S]")

    if result:
        the_url = check_update(the_url)
        global result_list
        result_list[v1] = the_url
        print("succeed")
        print(c_time + " " + str(result) + " " + the_url)
        return 1
    else:
        print(c_time + " " + str(result) + " " + the_url)
        return 0


def run():
    def run_get_link(start_ver, end_ver, start_ver_code):
        c_ver_code = start_ver_code
        for i in range(start_ver, end_ver):
            for j in range(c_ver_code, c_ver_code + 81):
                r = get(i, j)
                if r:
                    c_ver_code = j
                    pass

    # 这里是查找范围
    run_get_link(700, 710, 1380)
    # run_get_link(7010, 7023, 1580)
    # run_get_link(800, 810, 1840)
    # run_get_link(8010, 8039, 1960)

    with open('download_links.py', 'w') as file:
        file.write("links = [\n")
        for key, value in result_list.items():
            file.write(f"    ['{key}', '{value}'],\n")
        file.write("]\n")


if __name__ == '__main__':
    run()
