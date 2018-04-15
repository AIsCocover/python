#! E:\codeprojects\python\pythonEveryDay\011
# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，
# 当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

words_filter = set()

with open('filtered.txt','r') as file :
    for words in file :
        words_filter.add(words.strip())

while True :
    inp = input()
    if inp == 'exit' :
        break
    if inp in words_filter :
        print ('Freedom')
    else :
        print ('Human Rights')
# 只能判断当输入与敏感词完全相同时的敏感词
