#! E:\codeprojects\python\pythonEveryDay\019
# 第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下所示：
'''
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>
'''

import xlrd
try :
    import xml.etree.cElementTree as ET
except :
    import xml.etree.ElementTree as ET

def get_xls_content(xlsname) :
    xls = xlrd.open_workbook(xlsname)
    return xls

def get_xls_data(xls) :
    sheet = xls.sheet_by_index(0)
    data = []

    for i in range(sheet.nrows) :
        tmpdata = []
        for j in range(sheet.ncols) :
            value = sheet.cell(i,j).value
            if type(value) == float :
                value = (int)(value)
            tmpdata.append(value)
        data.append(tmpdata)

    return data

def write_data_in_xml(data) :
    tree = ET.ElementTree()
    root = ET.Element('root')
    tree._setroot(root)

    note = ET.Element('numbers')
    note.text = str(data)
    root.append(note)

    tree.write('numbers.xml','utf-8')

def main() :
    xls = get_xls_content('numbers.xls')
    data = get_xls_data(xls)
    write_data_in_xml(data)

if __name__=="__main__" :
    main()
