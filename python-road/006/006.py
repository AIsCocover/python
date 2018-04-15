#!E:\codeprojects\python\pythonEveryDay\006
# **第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免
# 分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import re, os

dirPath = os.path.dirname(os.path.abspath('006.py'))                                        # 获取当前文件所在目录
files = os.listdir(dirPath)                                                                                # 获取当前目录下所有文件和目录
regularExpression = re.compile(r'\b\w+\w?\b')                                               # 构建正则表达式

for file in files :                                                                                             # 遍历所有文件
    filePath = os.path.join(dirPath, file)                                                              # 获取每个文件的绝对路径
    if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.txt' :               # 判断file是否为.txt文件
        with open(filePath) as tmp :                                                                     # 打开文件file
            content = tmp.read()                                                                            # 读取文件内容
            words = regularExpression.findall(content)                                           # 将各个单词存入words中
            dictionary = dict()                                                                              # 新建字典

            for word in words :                                                                             # 统计各个单词出现的次数
                if word in ['a','an','the','to','for','of'] :
                    continue
                if word in dictionary :
                    dictionary[word] += 1
                else :
                    dictionary[word] = 1
            dictionary = sorted(dictionary.items(), key = lambda t: t[1], reverse=True)     # 按照dictionary的value(t[1])将dictionary从大到小排序
            print ('file: %s -> the most frequently word is: %s' % (file, dictionary[0]))    # 输出当前文件内出现最多的单词以及出现次数
            
