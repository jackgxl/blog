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

## Linux 内核配置

```
vi /etc/sysctl.conf  
  
追加到文件末尾  
  
kernel.shmall = 4294967296  
kernel.shmmax=135497418752  
kernel.shmmni = 4096  
kernel.sem = 50100 64128000 50100 1280  
fs.file-max = 7672460  
fs.aio-max-nr = 1048576  
net.ipv4.ip_local_port_range = 9000 65000  
net.core.rmem_default = 262144  
net.core.rmem_max = 4194304  
net.core.wmem_default = 262144  
net.core.wmem_max = 4194304  
net.ipv4.tcp_max_syn_backlog = 4096  
net.core.netdev_max_backlog = 10000  
net.ipv4.netfilter.ip_conntrack_max = 655360  
net.ipv4.tcp_timestamps = 0  
net.ipv4.tcp_tw_recycle=1  
net.ipv4.tcp_timestamps=1  
net.ipv4.tcp_keepalive_time = 72   
net.ipv4.tcp_keepalive_probes = 9   
net.ipv4.tcp_keepalive_intvl = 7  
vm.zone_reclaim_mode=0  
vm.dirty_background_bytes = 40960000  
vm.dirty_ratio = 80  
vm.dirty_expire_centisecs = 6000  
vm.dirty_writeback_centisecs = 50  
vm.swappiness=0  
vm.overcommit_memory = 0  
vm.overcommit_ratio = 90  


生效

sysctl -p  

2. /etc/security/limits.conf

vi /etc/security/limits.conf   
  
* soft    nofile  131072  
* hard    nofile  131072  
* soft    nproc   131072  
* hard    nproc   131072  
* soft    core    unlimited  
* hard    core    unlimited  
* soft    memlock 500000000  
* hard    memlock 500000000  

3. /etc/security/limits.d/*

rm -f /etc/security/limits.d/*  

4. 关闭selinux

# vi /etc/sysconfig/selinux   
  
SELINUX=disabled  
SELINUXTYPE=targeted  

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


