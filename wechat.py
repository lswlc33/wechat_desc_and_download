# 本脚本包括获取版本列表和版本更新日志
# 还包括查找下载链接

import requests
from lxml import etree
import download_links

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


def get_list():
    # 获取版本列表
    response = requests.get('https://weixin.qq.com/cgi-bin/readtemplate?lang=zh_CN&t=weixin_faq_list',
                            headers=headers).text
    x_root = etree.HTML(response)
    x_version_list = x_root.xpath('/html/body/div/div[3]/div[1]/div[2]/section[1]/ul/li')

    version_list = []  # 存放结果

    for version_info in x_version_list:
        # 取出链接,版本,时间
        link = "https://weixin.qq.com/" + version_info.xpath('./a/@href')[0]
        version = version_info.xpath('./a/span[1]/text()')[0]
        time = version_info.xpath('./a/span[2]/text()')[0]
        version_list.append([version, time, link])

    return version_list


def get_desc(desc_link):
    # 获取版本更新日志
    desc = ""

    response = requests.get(url=desc_link, headers=headers).text
    x_root = etree.HTML(response)
    x_h4_list = x_root.xpath('//*[@id="page_center"]/h4')

    for h4 in x_h4_list:
        text = h4.xpath('./text()')

        desc += "{}\n".format(text[0])

    desc += "{}\n".format(1)

    return desc


def search_for_download_link(ver):
    download_link = ''
    links_32 = download_links.links_32
    links_64 = download_links.links_64

    # 查找下载链接
    # 低版本-找不到-找得到
    # 找32位
    # 找64位



    return download_link


if __name__ == '__main__':
    print(get_desc("https://weixin.qq.com/cgi-bin/readtemplate?"
                   "lang=zh_CN&t=page/faq/android/7015/index&faq=android_7015"))
