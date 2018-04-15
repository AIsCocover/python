# -*- coding:utf-8 -*-
# html_downloader.py

import urllib.request

class HtmlDownLoader(object) :

    # 下载url对应的网页的html，并以byte形式返回
    def download(self, url) :
        if url is None :
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200 :
            return None

        return response.read()
