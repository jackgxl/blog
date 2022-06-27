# Xtrabackup 备份恢复

[TOC]



## 安装环境

```shell
安装yum源
yum install https://repo.percona.com/yum/percona-release-latest.noarch.rpm
[root@localhost ~]# ls percona-*
percona-toolkit-3.0.2-1.el7.x86_64.rpm  percona-xtrabackup-24-2.4.7-1.el7.x86_64.rpm

[root@localhost ~]# cat /etc/redhat-release 
CentOS Linux release 7.4.1708 (Core) 

[root@localhost ~]# xtrabackup --version
xtrabackup version 2.4.7 based on MySQL server 5.7.13 Linux (x86_64) (revision id: 6f7a799)

[root@localhost ~]# innobackupex --version
innobackupex version 2.4.7 Linux (x86_64) (revision id: 6f7a799)

wget https://repo.percona.com/yum/release/7/RPMS/x86_64/qpress-11-1.el7.x86_64.rpm
yum install qpress-11-1.el7.x86_64.rpm
```

## 备份恢复
创建备份目录

```shell
[root@localhost ~]# mkdir -pv /data/backup/all
mkdir: created directory '/data/backup/all'

```

* 全备份

```shell
innobackupex --defaults-file=/ssd/mysql3306/etc/my.cnf --user=root --password='123456' --socket=/ssd/mysql3306/tmp/mysql.sock  --safe-slave-backup  --slave-info --no-timestamp --use-memory=1G /data/backup/all

```

* 恢复全备份

```
应用Redolog
innobackupex --apply-log /data/backup/all/
拷贝数据
innobackupex --defaults-file=/data/mysql3307/etc/my.cnf --move-back /data/backup/all/
```

* 单库备份

```
innobackupex --defaults-file=/etc/my.cnf --no-timestamp --user='root' --password='123456' --use-memory=1G --databases="db1 db2"  /data/backup/16/ 
 
innobackupex --apply-log /data/backup/16/
```

* 单库恢复

```

```

* 增量备份

```

```

* 增量恢复

```

```


* 压缩备份

```shell
innobackupex --stream=xbstream /root/backup/ > /root/backup/backup.xbstream

innobackupex --stream=xbstream --compress /root/backup/ > /root/backup/backup.xbstream

xbstream -x <  backup.xbstream -C /root/backup/

innobackupex --stream=tar /root/backup/ > /root/backup/out.tar

innobackupex --stream=tar ./ | ssh user@destination \ "cat - > /data/backups/backup.tar"
用tar压缩备份，在解压时必须使用 -i 参数:
tar -xizf backup.tar.gz

innobackupex --stream=tar ./ | gzip - > backup.tar.gz
innobackupex --stream=tar ./ | bzip2 - > backup.tar.bz2

在恢复之前需要prepared该备份，因为流式备份不会做prepare。
```


### 本地备份传送到远程存储

* 备份到远程

```shell
innobackupex --defaults-file=/data/mysql3306/etc/my.cnf --user='root' --password='123456' --socket=/data/mysql3306/tmp/mysql.sock --safe-slave-backup  --slave-info --no-timestamp --use-memory=1G --compress --stream=xbstream /data/backup |ssh root@'172.16.64.154' "xbstream -x -C /data/backup/all"

```

* 解压

```shell
xbstream -x -C c <c.xb 
xtrabackup --decompress --target-dir=/home/gaoxueliang/c/
xtrabackup --defaults-file=/etc/my.cnf_3307 --move-back --target-dir=/home/gaoxueliang/c/

```

应用Redolog

```shell
innobackupex --apply-log /data/backup/all/
```



拷贝数据

```shell
innobackupex --defaults-file=/data/mysql3307/etc/my.cnf --move-back /data/backup/all/
```





tips:

```shell
解压需要qpress 依赖
tar zxf qpress-11-linux-x64.tar
mv qpress /usr/local/bin/
下载rpm  https://pkgs.org/download/qpress
```

* 恢复

```
innobackupex --defaults-file=/data/mysql5634_3308/etc/my.cnf --move-back /data/backup/all/
```

启动即可




Tips:
>   * defaults-file,user,password,socket 根据自己的实际配置修改
>   * 如果有MyISAM大表,不要在主库操作,低峰备份。
>   * use-memory=1G时 15k转 RAID10 备份时磁盘使用率80%
> * 注意版本8.0不能恢复基于5.7的2.4 版本的备份
> 

# reference

[https://blog.csdn.net/n88lpo/article/details/79226616](https://blog.csdn.net/n88lpo/article/details/79226616)
