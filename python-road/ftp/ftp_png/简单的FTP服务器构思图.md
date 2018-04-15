# 简单的FTP服务器

## FTP服务器主程序 base_ftp_server.py

### main

#### 提取用户配置文件中合法的行 ignor_octothrpe (text)

#### 初始化有授权的用户名单 init_user_config ()

#### 初始化FTP服务器 init_ftp_server ()

##### 设置Authorizer

##### 设置ThrottledDTPHandler

##### 设置FTPHandler

##### 设置FTPServer

##### 开启FTPServer

## 用户配置文件 baseftp.ini

### 账号

#### name

### 密码

#### passwd

### 权限

#### permit

### 浏览路径

#### homedir

## FTP服务器配置文件 config_ftp.py

### ip地址

#### ip

### 端口号

#### port

### 最大上传速度

#### max_upload

### 最大下载速度

#### max_download

### 最大连接数

#### max_cons

### 最大ip连接数

#### max_pre_ip

### FTP服务器被动连接端口号

#### passive_ports

### 匿名登录限制

#### enable_anonymous

### 日志显示限制

#### enable_logging

### 日志记录文件名

#### logging_name

### 公网ip地址

#### mesquerade_address

### FTP服务器欢迎标题

#### welcome_banner

### 默认的匿名用户浏览目录

#### anonymous_path

## 用户浏览目录 ./home

### 匿名用户浏览目录

#### ./home/anonymous

### 授权用户浏览目录

#### ./home/no_anonmymous
