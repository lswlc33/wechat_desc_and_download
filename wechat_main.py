# 这是个微信更新日志查看工具

import os
import msvcrt

from wechat import *


def section_choose(section_list, key, page):
    length = len(section_list)
    c_key = key
    all_page = length // 10
    if length % 10 != 0:
        all_page += 1
    c_page = page % all_page
    c_num = c_key + c_page * 10

    os.system('cls')
    print("请键入↑↓←→来切换或翻页,ENTER来选择\n")

    for i in range(c_page * 10, (c_page + 1) * 10):
        if i >= len(section_list):
            pass
        else:
            ver = section_list[i][0]
            time = section_list[i][1][1:-1]
            if i % 10 == c_key % 10:
                print(" \033[1m\033[7m{}. \t 版本: {} \t 发布时间: {}\033[0m".format(i + 1, ver, time))
            else:
                print("{}. \t版本: {} \t发布时间: {}".format(i + 1, ver, time))

    print("\n当前页数:{}\t共{}页".format(c_page + 1, all_page))

    while True:
        key = ord(msvcrt.getch())
        if key == 224:  # Special key
            arrow_key = ord(msvcrt.getch())
            if arrow_key == 72:  # Up arrow
                section_choose(ver_list, c_key - 1, c_page)
            elif arrow_key == 80:  # Down arrow
                section_choose(ver_list, c_key + 1, c_page)
            elif arrow_key == 77:  # Right arrow
                section_choose(ver_list, c_key, c_page + 1)
            elif arrow_key == 75:  # Left arrow
                section_choose(ver_list, c_key, c_page - 1)
        elif key == 13:  # Enter key
            if c_num >= len(section_list):
                os.system("cls")
                print("\n你没有选择任何选项！\n")
                os.system("pause")
                break
            ver_desc = get_desc(section_list[c_num][2])
            os.system("cls")
            print("当前版本:{}  发布时间:{}\n"
                  "更新日志:\n\n"
                  "{}\n"
                  "{}\n"
                  .format(section_list[c_num][0],
                          section_list[c_num][1][1:-1],
                          ver_desc,
                          search_for_download_link(section_list[c_num][2])))
            os.system("pause")
        section_choose(ver_list, c_key, c_page)


def print_download_link(text, link):
    text = text
    url = link
    os.system('cls')
    out = f'下载地址:\033]8;;{url}\033\\点击下载\033]8;;\033\\'
    print(out)


if __name__ == '__main__':
    ver_list = get_list()
    section_choose(ver_list, 0, 0)
