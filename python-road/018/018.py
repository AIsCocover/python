#! E:\codeprojects\python\pythonEveryDay\018
# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
'''
<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!-- 
	城市信息
-->
{
	"1" : "上海",
	"2" : "北京",
	"3" : "成都"
}
</citys>
</root>
'''
# 提取xls文件
# 打包文件内容
# 构建xml
# 将打包好的文件放入xml中
# 保存文件
#
import xlrd
try :
    import xml.etree.cElementTree as ET
except :
    import xml.etree.ElementTree as ET

def get_excel_data(xlsname) :
    xls = xlrd.open_workbook(xlsname)
    return xls

def get_xls_content(xls) :
    sheet = xls.sheet_by_index(0)
    content = {}

    for i in range(sheet.nrows) :
        key = sheet.row(i)[0].value
        if type(key) == float :
            key = (int)(key)
        key = str(key)
        value = str(sheet.row(i)[1].value)
        content[key] = value

    return content

def write_content_to_xml(content) :
    tree = ET.ElementTree()
    root = ET.Element('root')
    tree._setroot(root)

    note = ET.Element('citys')
    note.text = str(content)
    root.append(note)

    tree.write('city.xml','utf-8')

def main() :
    xls = get_excel_data('city.xls')
    content = get_xls_content(xls)
    write_content_to_xml(content)

if __name__=="__main__" :
    main()
    
    
