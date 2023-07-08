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

V8 = ['https://dldir1.qq.com/weixin/android/weixin800android1840_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin801android1840_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin802android1860_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin803android1880.apk',
      'https://dldir1.qq.com/weixin/android/weixin806android1900.apk',
      'https://dldir1.qq.com/weixin/android/weixin807android1920.apk',
      'https://dldir1.qq.com/weixin/android/weixin809android1940.apk',
      'https://dldir1.qq.com/weixin/android/weixin8010android1961_3.apk',
      'https://dldir1.qq.com/weixin/android/weixin8011android1980_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8014android2000_2.apk',
      'https://dldir1.qq.com/weixin/android/weixin8015android2020_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8016android2040_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8018android2060_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8019android2080_4.apk',
      'https://dldir1.qq.com/weixin/android/weixin8021android2120_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8022android2140_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8023android2160_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8024android2180.apk',
      'https://dldir1.qq.com/weixin/android/weixin8025android2200_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8027android2220_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8028android2240.apk',
      'https://dldir1.qq.com/weixin/android/weixin8030android2260_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8031android2280_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8032android2300_3.apk',
      'https://dldir1.qq.com/weixin/android/weixin8033android2320_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8034android2340_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8035android2360_3.apk',
      'https://dldir1.qq.com/weixin/android/weixin8037android2380_1.apk',
      'https://dldir1.qq.com/weixin/android/weixin8038android2400_1.apk'
      ]

V8_64 = ['https://dldir1.qq.com/weixin/android/weixin800android1840_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin801android1840_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin802android1860_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin803android1880_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin806android1900_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin807android1920_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin809android1940_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin8010android1961_arm64_3.apk',
         'https://dldir1.qq.com/weixin/android/weixin8011android1980_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8014android2000_arm64_2.apk',
         'https://dldir1.qq.com/weixin/android/weixin8015android2020_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8016android2040_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8018android2060_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8019android2080_arm64_4.apk',
         'https://dldir1.qq.com/weixin/android/weixin8021android2120_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8022android2140_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8023android2160_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8024android2180_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin8025android2200_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8027android2220_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8028android2240_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin8030android2260_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8031android2280_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8032android2300_arm64_3.apk',
         'https://dldir1.qq.com/weixin/android/weixin8033android2320_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8034android2340_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8035android2360_arm64_3.apk',
         'https://dldir1.qq.com/weixin/android/weixin8037android2380_arm64_1.apk',
         'https://dldir1.qq.com/weixin/android/weixin8038android2400_arm64_1.apk'
         ]

V7 = ['https://dldir1.qq.com/weixin/android/weixin700android1380.apk',
      'https://dldir1.qq.com/weixin/android/weixin703android1400.apk',
      'https://dldir1.qq.com/weixin/android/weixin704android1420.apk',
      'https://dldir1.qq.com/weixin/android/weixin705android1440.apk',
      'https://dldir1.qq.com/weixin/android/weixin706android1460.apk',
      'https://dldir1.qq.com/weixin/android/weixin706android1480.apk',
      'https://dldir1.qq.com/weixin/android/weixin707android1520.apk',
      'https://dldir1.qq.com/weixin/android/weixin708android1540.apk',
      'https://dldir1.qq.com/weixin/android/weixin709android1560.apk',
      'https://dldir1.qq.com/weixin/android/weixin7010android1580.apk',
      'https://dldir1.qq.com/weixin/android/weixin7011android1600.apk',
      'https://dldir1.qq.com/weixin/android/weixin7012android1620.apk',
      'https://dldir1.qq.com/weixin/android/weixin7013android1640.apk',
      'https://dldir1.qq.com/weixin/android/weixin7014android1660.apk',
      'https://dldir1.qq.com/weixin/android/weixin7015android1680.apk',
      'https://dldir1.qq.com/weixin/android/weixin7016android1700.apk',
      'https://dldir1.qq.com/weixin/android/weixin7017android1720.apk',
      'https://dldir1.qq.com/weixin/android/weixin7018android1740.apk',
      'https://dldir1.qq.com/weixin/android/weixin7019android1760.apk',
      'https://dldir1.qq.com/weixin/android/weixin7020android1780.apk',
      'https://dldir1.qq.com/weixin/android/weixin7021android1800.apk'
      ]

V7_64 = ['https://dldir1.qq.com/weixin/android/weixin709android1560_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7010android1580_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7011android1600_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7012android1620_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7013android1640_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7014android1660_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7015android1680_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7016android1700_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7017android1720_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7018android1740_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7019android1760_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7020android1780_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7021android1800_arm64.apk',
         'https://dldir1.qq.com/weixin/android/weixin7022android1820_arm64_1.apk'
         ]


def check_error_link():
    url_list = [
        V8,
        V8_64,
        V7,
        V7_64
    ]
    result_list = []

    for i in url_list:
        for url in i:
            response = requests.head(url=url, headers=headers)
            if response.status_code != 200:
                # print("error_url " + url)
                result_list.append("error_url " + url)

    # 输出结果
    if len(result_list):
        print("找到{}个错误链接".format(len(result_list)))
        for i in result_list:
            print(i)
    else:
        print("链接全部可用")


def check_update():
    url_list = [
        V8,
        V8_64,
        V7,
        V7_64
    ]
    result_list = []

    # 遍历链接
    for i in url_list:
        for url in i:
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
                    result_list.append(new_url)
                else:
                    # rint("Failed " + new_url)
                    break
    # 输出结果
    if len(result_list):
        print("找到{}个新链接".format(len(result_list)))
        for i in result_list:
            print(i)
    else:
        print("没有找到新的链接")


if __name__ == '__main__':
    check_error_link()
    check_update()
