#! E:\codeprojects\python\pythonEveryDay\001
# encoding utf-8
'''第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？'''

__author__ = 'AIsCocover'

import random, string

Dictionary = string.ascii_uppercase + string.digits             # Dictionary 中保存code中所有可能的字符
codeAmount = 200                                                           # code的总个数
codeLength = 10                                                               # code的长度
codeResult = []                                                                # 保存所有code

for i in range(codeAmount) :                                                      # 200个code
    code = ' '.join((random.choice(Dictionary) for j in range(codeLength)))      # 编辑每个code
    if code not in codeResult :
        codeResult.append(code)                                          # 将符合条件的code放入codeResult

print (len(codeResult))
print (codeResult)
