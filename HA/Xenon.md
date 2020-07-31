#  Xenon



## 下载安装

### xenon

```shell
git clone https://github.com/xenon/xenon
cd xenon
make build
make test
ll bin/
-rwxr-xr-x 1 root root 12990945 Jul 15 11:59 xenon
-rwxr-xr-x 1 root root 12186684 Jul 15 11:59 xenoncli
```



### xtrabackup

```shell
wget https://www.percona.com/downloads/Percona-XtraBackup-LATEST/Percona-XtraBackup-8.0.13/binary/redhat/7/x86_64/percona-xtrabackup-80-8.0.13-1.el7.x86_64.rpm
yum -y install percona-xtrabackup-80-8.0.13-1.el7.x86_64.rpm 
```





## 配置

mysql用户

```shell
vim /etc/passwd
mysql:x:1001:1001::/home/mysql:/bin/bash

mkdir -pv /home/mysql
chown -R mysql:mysql /home/mysql
passwd mysql
mkdir /data/backup/mysql_xenon -pv
cd /data/backup/mysql_xenon
chown -R mysql:mysql mysql_xenon
visudo
mysql           ALL=(ALL)       NOPASSWD: /usr/sbin/ip
```

SSL互信

```shell
ssh-keygen 
ssh-copy-id mysql@'192.168.64.109'
ssh-copy-id mysql@'192.168.64.154'
ssh-copy-id mysql@'192.168.64.155'
```



启动MySQL，同步主从

xenon 配置









## Reference

[https://github.com/radondb/xenon/blob/master/docs/how_to_build_and_run_xenon.md#step31-prepare-the-configuration-file](https://github.com/radondb/xenon/blob/master/docs/how_to_build_and_run_xenon.md#step31-prepare-the-configuration-file)

