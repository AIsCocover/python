#! E:\codeprojects\python\pythonEveryDay\017
# 第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
# 如下所示：
'''
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''

import xlrd
try :
    import xml.etree.cElementTree as ET
except :
    import xml.etree.ElementTree as ET

def open_excel(excelName) :
    return xlrd.open_workbook(excelName)

def get_excel_data(xls) :
    data = {}
    sheet = xls.sheet_by_index(0)

    for i in range(sheet.nrows) :
        key = str((int)(sheet.row(i)[0].value))
        value = []
        for j in range(1,sheet.ncols) :
            content = sheet.cell(i,j).value
            if type(content) == float :
                content = (int)(content)
            value.append(content)
        data['%s' % key] = value
    return data

def write_to_xml(data) :
    tree = ET.ElementTree()
    root = ET.Element('root')
    tree._setroot(root)

    note = ET.Element('students')
    note.text = str(data)
    root.append(note)

    tree.write('student.xml','utf-8')

def main() :
    xls = open_excel('student.xls')
    data = get_excel_data(xls)
    write_to_xml(data)

if __name__=="__main__" :
    main()
