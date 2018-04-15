#! E:\codeprojects\python\pythonEveryDay\013
# 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
# http://tieba.baidu.com/p/2166231880

import urllib.request, re

def get_html(url) :
    tmp = urllib.request.urlopen(url)
    html = tmp.read()
    return html

def get_images(html) :
    imgRe = re.compile(r'src="(.*?\.jpg)" bdwater=')
    html = html.decode('utf-8')
    imgLists = imgRe.findall(html)

    i = 0
    for imgurl in imgLists :
        urllib.request.urlretrieve(imgurl, '%s.jpg' % i)
        i += 1
html = get_html('http://tieba.baidu.com/p/2166231880')
print (get_images(html))
