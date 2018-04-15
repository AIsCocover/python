#! E:\codeprojects\python\pythonEveryDay\016
# 第 0016 题： 纯文本文件 numbers.txt, 里面的内容，写到 numbers.xls 文件中

import json, xlwt

def load_data(filePath) :
    file = open(filePath,'r')
    return json.load(file)

def write_data_to_excel(data) :
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('numbers')

    for i in range(len(data)) :
        json_data = data[i]
        for j in range(len(json_data)) :
            sheet.write(i, j, json_data[j])

    xls.save('numbers.xls')

if __name__=="__main__" :
    data = load_data('numbers.txt')
    write_data_to_excel(data)
