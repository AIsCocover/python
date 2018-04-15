# 简易python爬虫

## 确定目标

### 百度百科Python词条相关词条网页--标题和简介(1000条)

## 分析目标

### 入口页 : http://baike.baidu.com/item/Python

### URL格式

#### 词条页面URL

##### http://baike.baidu.com/item/......

### 数据格式

#### 标题

##### <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1></dd>

#### 简介

##### <div class="lemma-summary">......</div>

### 页面编码

#### utf-8

## 编写代码

### 主文件Main

#### spider_main.py

### URL管理器URLManager

#### url_manager.py

### 网页下载器HtmlDownloader

#### html_downloader.py

### 网页解析器HtmlParser

#### html_parser.py

### 网页制作器HtmlOutputer

#### html_outputer.py

### html文件

#### output.html

## 执行爬虫
