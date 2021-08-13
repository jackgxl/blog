# Python3 

## 下载安装包

[www.python.org](www.python.org)

```
wget https://www.python.org/ftp/python/3.4.10/Python-3.4.10.tgz
```

## 配置环境

```
yum -y install ncurses ncurses-devel zlib zlib-devel bzip2 bzip2-devel ncurses ncurses-devel readline readline-devel openssl openssl-devel openssl-static xz lzma xz-devel sqlite sqlite-devel gdbm gdbm-devel tk tk-devel libffi libffi-devel
```

## 编译安装

```
[root@syq-191 data1]# rm -rf Python-3.7.3.tgz 
[root@syq-191 data1]# mkdir python3
[root@syq-191 data1]# tar zxf Python-3.4.10.tgz 
[root@syq-191 data1]# cd Python-3.4.10
[root@syq-191 Python-3.4.10]# ./configure --prefix=/data1/python3/
[root@syq-191 Python-3.4.10]# make -j 20
[root@syq-191 Python-3.4.10]# make install
```

## 验证

```
[root@syq-191 mysql_monitor]# /data1/python3/bin/python3 -V
Python 3.4.10
```


### reference

[https://www.cnblogs.com/freeweb/p/5181764.html]()
