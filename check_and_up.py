# 检查下载链接可靠性
import re
import requests

headers = {
    'authority': 'weixin.qq.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 '
                  'Safari/537.36 Edg/114.0.1823.67',
}


def check_error_link(url):
    # 返回1是链接正确
    response = requests.head(url=url, headers=headers)
    if response.status_code != 200:
        return 0
    return 1


def check_update(url):
    result = 1
    num = 1

    # 制作新链接
    if re.search(r'_\d+\.apk$', url):
        num = int(re.search(r'(\d+)\.apk$', url).group(1)) + 1
        f_url = url[:-6] + "_{}.apk"
    else:
        f_url = url[:-4] + "_{}.apk"

    # 测试链接
    while result:
        new_url = f_url.format(num)
        result = check_error_link(new_url)
        if result:
            num += 1
            url = new_url
    return url


if __name__ == '__main__':
    print(check_error_link("https://dldir1.qq.com/weixin/android/weixin8019android2080.apk"))
    print(check_update("https://dldir1.qq.com/weixin/android/weixin809android1940.apk"))
