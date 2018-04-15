#! E:\codeprojects\python\pythonEveryDay\002
# encoding = utf-8
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 SQLite3 关系型数据库中。
# test.db

import random, string, sqlite3

def CreateCodeList(codeAmount, codeLength) :                                                # 随机创建200个激活码
    Dictionary = string.ascii_uppercase + string.digits
    codeResult = []

    for i in range(codeAmount) :
        code = ' '.join(random.choice(Dictionary) for j in range(codeLength))
        if code not in codeResult :
            codeResult.append(code)
    return codeResult

conn = sqlite3.connect('test.db')                                                                       # 连接数据库test.db 并建表CODES
                                                                                                                        
conn.execute('''CREATE TABLE CODES                                                           
( code TEXT NOT NULL);''')

codeResult = CreateCodeList(200, 10)

for i in range(200) :                                                                                       # 将200个随机激活码insert到CODES中
    conn.execute("INSERT INTO CODES VALUES ( '" + codeResult[i] + " ')")
conn.commit()

cursor = conn.execute("SELECT * FROM CODES")                        
for row in cursor :                                                                                         # 输出表CODES的数据
    print (row)

# conn.execute("DROP TABLE CODES")
conn.close()
