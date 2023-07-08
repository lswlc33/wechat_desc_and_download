# 微信历史版本

> 这是一个能够自动获取微信所有历史版本的更新日志和下载地址的工具 

## 文件介绍
```commandline
wechat_main.py              # 主程序，展示命令行界面 
wechat.py                   # 作为主程序的爬虫后端
get_download_links.py       # 本脚本用于更新下载链接到download_links.py
download_links.py           # 在本文件中通过列表存放版本号和对应下载链接 
check_and_up.py             # 本文件存放了链接处理相关函数
```

## 使用说明
`download_links.py`内置了7.0.0到8.0.38的下载链接  
使用`get_download_links.py`可以更新但同时也会覆盖源文件  
由于`get_download_links.py`效率过低，完全运行结束可能需要半小时  

运行`wechat_main.py`可以检索微信所有已经在官网发布的安卓版本列表  
10个一页在终端展示  
进入可以查看版本发布时间和更新日志和下载链接  
默认展示32位下载链接  
如果有64位版本会自动展示  


