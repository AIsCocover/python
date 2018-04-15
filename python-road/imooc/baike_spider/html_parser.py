# -*- coding:utf-8 -*-
# html_parser.py

from bs4 import BeautifulSoup
import re, urllib.parse

class HtmlParser(object) :
    # 获取该html中所有可访问的url set形式保存在new_urls中并返回该变量
    def _get_new_urls(self, page_url, soup) :
        new_urls = set()
        #/item/............
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links :
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取当前html的url、标题和简介 字典形式保存在res_data中并返回该变量
    def _get_new_data(self, page_url, soup) :
        res_data = {}

        # 获取当前html的url
        res_data['url'] = page_url

        # 获取当前html的标题 以下为通过查看目标网页的源码得到的标题的样例
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # 获取当前html的简介 以下为通过查看目标网页的源码得到的简介的样例
        # <div class="lemma-summary" label-module="lammaSummary">....</div>
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析html(byte)文件
    def parse(self, page_url, html_cont) :
        if page_url is None or html_cont is None :
            return

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
