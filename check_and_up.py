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
    response = requests.head(url=url, headers=headers)
    if response.status_code != 200:
        # print("error_url " + url)
        return 0
    return 1


def check_update(url):
    r_code = 200
    num = 1

    # 制作新链接
    if re.search(r'_\d+\.apk$', url):
        num = int(re.search(r'(\d+)\.apk$', url).group(1)) + 1
        url = url[:-6] + "_{}.apk"
    else:
        url = url[:-4] + "_{}.apk"

    # 测试链接
    while r_code == 200:
        new_url = url.format(num)
        r_code = requests.head(url=new_url, headers=headers).status_code
        if r_code == 200:
            num += 1
            # print("Succeed " + new_url)
            return new_url
        else:
            # print("Failed " + new_url)
            return 0


if __name__ == '__main__':
    pass
