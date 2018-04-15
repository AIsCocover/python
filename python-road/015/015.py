#! E:\codeprojects\python\pythonEveryDay\015
# 第 0015 题： 纯文本文件 city.txt为城市信息, 将所有城市信息写到 city.xls 文件中
# 与014.py相同解法

import json, xlwt

def load_data(filePath) :
    file = open(filePath,'r')
    return json.load(file)

def write_data_to_excel(data) :
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('city')

    for i in range(len(data)) :
        sheet.write(i,0,i+1)
        json_data = data[str(i+1)]
        sheet.write(i,1,json_data)

    xls.save('city.xls')

if __name__=="__main__" :
    data = load_data('city.txt')
    write_data_to_excel(data)
