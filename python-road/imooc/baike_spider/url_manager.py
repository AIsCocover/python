# -*- coding:utf-8 -*-
# url_manager.py

class UrlManager(object) :
    # 初始化url管理器 new_urls存还未访问过的url old_urls存已经访问过的url  set()可以去重
    def __init__(self) :
        self.new_urls = set()
        self.old_urls = set()

    # 添加新的单个url
    def add_new_url(self, url) :
        if url is None :
            return
        if url not in self.new_urls and url not in self.old_urls :
            self.new_urls.add(url)

    # 添加新的多个url
    def add_new_urls(self, urls) :
        if urls is None or len(urls) == 0 :
            return
        for url in urls :
            self.add_new_url(url)

    # 是否还有未访问过的url
    def has_new_url(self) :
        return len(self.new_urls) != 0

    # 获取还未访问过的url
    def get_new_url(self) :
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
