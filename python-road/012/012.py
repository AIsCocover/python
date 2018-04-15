#! E:\codeprojects\python\pythonEveryDay\012
# 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入
# 敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

import re

def read_file(filename) :                                   # 读取文件
    content = []
    with open(filename,'r') as file :
        for line in file.readlines() :                        # 保存文件每一行内容
            content.append(line.strip())
    return content

def create_regular_expression(content) :           # 自定义正则表达式
    re_string = ''                                                # 初始化时不能有空格
    for line in content :
        re_string += line + '|'                                # 使用 | 分隔
    return re_string[:-1]

def replace_input(cre) :                                    # 检测与替换输入的字符串
    inp = input()
    print (re.sub(cre, '**', inp))                          # 替换 re.sub(...)

filename = 'filtered_words.txt'
content = read_file(filename)
cre = create_regular_expression(content)
replace_input(cre)
