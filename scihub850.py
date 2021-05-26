
# http://libgen.rs/scimag/repository_torrent/

# 地址：
# 固定地址：http://libgen.rs/scimag/repository_torrent/
# 變化部分：sm_”000“00000-”000“99999.torrent
# 引號部分，000~851，000~851，前後相同

# wget http://libgen.rs/scimag/repository_torrent/sm_85100000-85199999.torrent

import os, time # 系统库
from subprocess import call
import re  # 正则表达式 提取页面关键信息
import requests  # 提交网络请求
from bs4 import BeautifulSoup  # 解析网页格式
import bs4
import scrapy  # 网络爬虫框架



# requests 方法
def getzhongzi(url):
# zhognzi = requests.get(url)
    # path = "C:\\Users\\Frankly\\Developer"
    path = "/home/frankly/Developer/"
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
        r = requests.get(url,headers)
        print(r.status_code)
        print(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("file save successful")
    except:
        print("{} 下載失敗".format(url))



# wget 方法
def wgetzhongzi(url):
    try:
        call('wget ' + url, shell=True)
        # print("successful")
    except:
        print("{} 下載失敗".format(url))



# 獲取種子地址
for i in range(000,852):
    if i < 10:
        # print(i)
        url = "http://libgen.rs/scimag/repository_torrent/sm_00{}00000-00{}99999.torrent".format(i, i)
    elif i<100:
        # print(i)
        url = "http://libgen.rs/scimag/repository_torrent/sm_0{}00000-0{}99999.torrent".format(i, i)
    else:
        # print(i)
        url = "http://libgen.rs/scimag/repository_torrent/sm_{}00000-{}99999.torrent".format(i, i)
    # print(url)
    wgetzhongzi(url)
    # getzhongzi(url)
    time.sleep(0.1)
