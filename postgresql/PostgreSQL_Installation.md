# PostgreSQL_Installation

[TOC]

## 准备环境

* 配置环境依赖

```
[root@localhost postgresql-11.0]# cat /etc/redhat-release 
CentOS Linux release 7.3.1611 (Core) 
```

```
[root@localhost postgresql-11.0]# yum -y install coreutils glib2 lrzsz mpstat dstat sysstat e4fsprogs xfsprogs ntp readline-devel zlib-devel openssl-devel pam-devel libxml2-devel libxslt-devel python-devel tcl-devel gcc make smartmontools flex bison perl-devel perl-ExtUtils* openldap-devel jadetex  openjade bzip2
```

* 下载安装包

```
wget https://ftp.postgresql.org/pub/source/v11.0/postgresql-11.0.tar.gz
```



## 编译安装

```shell
tar zxf postgresql-11.0.tar.gz

cd postgresql-11.0

./configure --prefix=/usr/local/pg_11

make world -j 12

make install-world

cd /usr/local

ln -sv pg_11 postgres 
```

## 初始化

```shell 
su - postgres
/usr/local/postgresql/bin/initdb -D /data/pg_data_11 -U postgres

```

## 修改配置文件

```

```


## reference

[https://github.com/digoal/blog/blob/master/201611/20161121_01.md](https://github.com/digoal/blog/blob/master/201611/20161121_01.md)


