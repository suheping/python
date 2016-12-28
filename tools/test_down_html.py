# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: test_down_html.py
@time: 2016/12/14 8:49
"""
from urllib import request
import re
# from xml import etree

def getHtml(url):
    # pass
    page = request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    content_p = r'<div class="x-content"([\s\S]*)<div id="the-promos"'
    url_p = r'0014316089557264a6b348958f449949df42a6d3a2e542c000/(.*)">'
    # 取得URL
    url_reg = re.compile(url_p)
    url_list = re.findall(url_reg,str(html))
    # return html,url_list
    # 取得内容
    content_reg = re.compile(content_p)
    content_list = re.findall(content_reg, str(html))
    return content_list[0],url_list


def savefile(data,x):
    path = 'e:/outpath/' + str(x) + '.html'
    fs = open(path,'w',encoding='utf-8')
    fs.write(data)
    fs.close()

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    first_url = 'http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/'
    x = 0
    data = getHtml(first_url)
    savefile(data[0],x)
    # print(data[1])
    list1 = data[1]
    list1 = set(list1)
    for i in list1:
        x = x + 1
        print('第 ' + str(x) + ' 次保存页面')
        url = first_url + i
        print('url :  ' + url)
        data = getHtml(url)
        savefile(data[0],x)
