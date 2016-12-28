# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: test_video_download.py
@time: 2016/12/14 16:56
"""
from urllib import request

import re

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    page = request.urlopen('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431611988455689d4c116b2c4ed6aec000776c00ed52000')
    html = page.read()
    html = html.decode('utf-8')
    # <source src = "http://asklxf.coding.me/liaoxuefeng/v/python/first-py-code.mp4" >
    video_p = 'source src="(.*)mp4">'
    video_reg = re.compile(video_p)
    video = re.findall(video_reg,str(html))
    video_url = video[0] + 'mp4'
    request.urlretrieve(video,'e:/444.mp4')

