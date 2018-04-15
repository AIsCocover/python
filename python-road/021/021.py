#! E:\codeprojects\python\pythonEveryDay\021
#  通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？
# 请使用 Python 对密码加密。
# 1、给password加上唯一标识uuid4(全部转换成hex)
# 2、使用hashlib中的sha256处理过的password加密

import uuid, hashlib
                                                                                        # hash password
def hash_password(password) :                                   
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
                                                                                        # check password
def check_password(hashed_password, user_password) :
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def main() :
    new_pass = input('New password: ')
    hashed_pass = hash_password(new_pass)
    print ('Hashed_pass: ' + hashed_pass)

    old_pass = input('Old password: ')
    if check_password(hashed_pass, old_pass) :
        print ('Password is right')
    else :
        print ('Password is wrong')

if __name__=='__main__':
    main()
