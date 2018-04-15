# -*- coding:utf-8 -*-
# spider_main.py

from baike_spider import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object) :

    # 初始化url管理器、html下载器、html解析器、html输出器
    def __init__(self) :
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    # 主函数
    def craw(self, root_url) :
        # 计数器
        count = 1
        # 往url管理器中添加单个目标URL
        self.urls.add_new_url(root_url)
        # url管理器中是否有还未访问的url
        while self.urls.has_new_url() :
            try :
                # 从url管理器中获取一个还未访问的url，并输出该url的相关信息
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url))
                # 通过html下载器下载该url的html(byte)
                html_cont = self.downloader.download(new_url)
                # 通过html解析器解析得到的html(byte)，获取当前html中的所有可访问的url以及当前html的标题和简介
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 往url管理器中添加多个可访问url
                self.urls.add_new_urls(new_urls)
                # 将获取到的当前html的url、标题和简介缓存到html输出器中
                self.outputer.collect_data(new_data)

                # 计数器
                if count == 10 :
                    break
                
                count += 1

                # 出现异常时，抛出异常信息
            except Exception as e:
                print(e)

        # 将html输出器中存储的数据写入新的html文件中
        self.outputer.output_html()

if __name__ == "__main__" :
    # 目标URL
    root_url = "http://baike.baidu.com/item/Python"
    # 创建主函数对象
    obj_spider = SpiderMain()
    # 调用主函数
    obj_spider.craw(root_url)
