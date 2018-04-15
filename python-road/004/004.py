#! E:\codeprojects\python\pythonEveryDay\004
# **第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

file = open('test.txt','r')                                             # 打开文件test.txt 该文件保存在本文件所在目录下
content = file.read()                                                    # 将文件内容读入content中
    
regularExpression = re.compile(r'\b\w+\w\b')              # 创建正则表达式
words = regularExpression.findall(content)                   # 按照正则表达式把匹配到的结果存入words中 

dictionary = dict()                                                       # dictionary用来存放各个单词的出现次数

for word in words :                                                      # 遍历dictionary并记录各个单词的出现次数
    if word in dictionary :
        dictionary[word] += 1
    else :
        dictionary[word] = 1

for key,value in dictionary.items() :                               # 输出各个单词的出现次数
    print ('%s: %s' % (key, value))

file.close()                                                                    # 关闭文件
