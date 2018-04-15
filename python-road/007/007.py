#! E:\codeprojects\python\pythonEveryDay\007
import re, os

def CountCodeLines(dirPath) :
    if not os.path.isdir(dirPath) :                                                                   # 判断路径是否非法
        return
    
    files = os.listdir(dirPath)                                                                         # 获取dirPath目录下所有文件和目录
    noteExpression = re.compile(r'^#.*')                                                        # 构建正则表达式 匹配以#开头不以换行符结尾的字符串，注意匹配中文有问题，需要做编码转换. 待修改
 #   print (files)
    print ('%s\t%s\t%s\t%s' % ('file', 'total', 'space', 'note'))   
    
    for file in files :                                                                                     # 遍历所有文件
        filePath = os.path.join(dirPath, file)                                                      # 获取当前文件路径
        if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.py' :        # 判断文件是否合法
            with open(filePath, encoding='gbk') as tmp :
                total_lines = 0
                space_lines = 0
                note_lines = 0
                
                for line in tmp.readlines() :                                                           # 遍历当前文件所有行
                    total_lines += 1
                    if line.strip() == ' ' :                                                                # strip()返回一个去除了首尾的空格的字符串
                        space_lines += 1
                        continue
                    note = noteExpression.findall(line.strip())
                    if note :
                        note_lines += 1

                print ('%s\t%d\t%d\t%d' % (file, total_lines, space_lines, note_lines))

CountCodeLines(os.path.dirname(os.path.abspath('007')))
                
