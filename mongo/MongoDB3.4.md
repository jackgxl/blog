# MongoDB3.4

## 下载安装包

```
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.4.4.tgz
```
## 解压安装

```
[root@localhost ~]# tar zxf mongodb-linux-x86_64-rhel70-3.4.4.tgz 
[root@localhost ~]# mv mongodb-linux-x86_64-rhel70-3.4.4 /usr/local/
[root@localhost ~]# ln -sv /usr/local/mongodb-linux-x86_64-rhel70-3.4.4 /usr/local/mongo344
‘/usr/local/mongo344’ -> ‘/usr/local/mongodb-linux-x86_64-rhel70-3.4.4’
[root@localhost ~]# /usr/local/mongo344/bin/mongo --version
MongoDB shell version v3.4.4
git version: 888390515874a9debd1b6c5d36559ca86b44babd
OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
allocator: tcmalloc
modules: none
build environment:
    distmod: rhel70
    distarch: x86_64
    target_arch: x86_64
```

创建数据目录，创建keyFile

```
[root@localhost ~]# mkdir -pv /data/mongo7777/log
[root@localhost mongo7777]# groupadd mongo   
[root@localhost mongo7777]# useradd mongo -g mongo -s /sbin/nologin 
[root@localhost mongo7777]# openssl rand -base64 66 > keyFile
[root@localhost mongo7777]# chmod 600 keyFile 

```

## 配置

系统配置

```
[root@local-157 mongo7777]# vim /etc/security/limits.conf 
ulimit -u 65500
ulimit -n 65500

* soft nofile 65535
* hard nofile 65535
* soft nproc 65535
* hard nproc 65535


mongod soft nofile 64000
mongod hard nofile 64000
mongod soft nproc 62000
mongod hard nproc 62000

[root@local-157 mongo7777]# vim /etc/security/limits.d/20-nproc.conf 
# Default limit for number of user's processes to prevent
# accidental fork bombs.
# See rhbz #432903 for reasoning.

*          soft    nproc     65000
root       soft    nproc     unlimited
```

配置文件

```
[root@arton157 mongo7777]# cat mongodb7777.conf 
fork = true
port = 7777
quiet = false
bind_ip = 0.0.0.0
dbpath = /data/mongo7777/var
unixSocketPrefix = /data/mongo7777/tmp
pidfilepath = /data/mongo7777/var/mongodb7777.pid
logpath = /data/mongo7777/log/mongod.log
logappend = true
journal = true
nohttpinterface = true
directoryperdb = true
profile = 1
slowms = 500
replSet = rs1
oplogSize = 10240
keyFile=/data/mongo7777/keyFile
#setParameter=enableLocalhostAuthByPass=0
storageEngine = wiredTiger
wiredTigerCacheSizeGB = 4
wiredTigerCollectionBlockCompressor = snappy
```

## 启动

修改目录权限

```
[root@localhost mongo7777]# chown -R mongo:mongo .
[root@localhost mongo7777]# cd /usr/local/mongo344/
[root@localhost mongo344]# chown -R mongo:mongo . 
```

脚本如下

```shell
[root@arton157 mongo7777]# cat mongo.sh 
#!/bin/bash

# mongodb 安装目录
MONGOD=/usr/local/mongo344/bin/mongod
#mongodb 数据目录
MONGO_DATA=/data/mongo7777
#mongodb 端口号
PORT=7777
#start mongodb
start() {
    echo "never" > /sys/kernel/mm/transparent_hugepage/enabled 
    echo "never" > /sys/kernel/mm/transparent_hugepage/defrag
    sudo -u mongo numactl --interleave=all ${MONGOD} -f ${MONGO_DATA}/mongodb${PORT}.conf
}

#stop mongodb
stop() {
    sudo -u mongo numactl --interleave=all ${MONGOD} -f ${MONGO_DATA}/mongodb${PORT}.conf --shutdown
}

case "$1" in 
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo $"Usage: $0 {start|stop|restart}"
        exit3
esac
```

