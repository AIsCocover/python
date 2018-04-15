#! E:\codeprojects\python\pythonEveryDay\014
# 第 0014 题： 纯文本文件 student.txt为学生信息, 将所有学生信息写到 student.xls 文件中

import json, xlwt

def load_data(filePath) :                               #  将文件内容使用json转换为python字典格式
    file = open(filePath,'r')
    return json.load(file)

def write_data_to_excel(data) :                    # 字典data写入Excel
    xls = xlwt.Workbook()                               # 创建excel
    sheet = xls.add_sheet('student')                 # 创建excel页

    for i in range(len(data)) :                           #  遍历字典data
        sheet.write(i,0,i+1)                                 # 写入序号1、2、3
        json_data = data[str(i+1)]                       # 读取字典data中key为'1'、'2'、'3'对应的值

        for j in range(len(json_data)) :                # 将各个value的值分别输入excel中
            sheet.write(i,j+1,json_data[j])

    xls.save('student.xls')                                 # 保存excel文件 

if __name__=="__main__":
    data = load_data('student.txt')
    write_data_to_excel(data)
    
