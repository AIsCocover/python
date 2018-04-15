# -*- coding:utf-8 -*-
# html_outputer.py

class HtmlOutputer(object) :
    # 初始化数据缓存器 datas
    def __init__(self) :
        self.datas = []

    # 将数据缓存到datas中
    def collect_data(self, data) :
        if data is None :
            return
        self.datas.append(data)

    # 将数据缓存器中的数据存放到指定的html文件中
    def output_html(self) :
        fout = open('output.html', 'w', encoding='utf-8')

        # 以下为指定的html的格式
        fout.write("<html>")
        fout.write("<meta charset='utf-8'>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas :
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        
        fout.close()
