# Xtrabackup 备份恢复

## 安装环境

```shell
[root@localhost ~]# ls percona-*
percona-toolkit-3.0.2-1.el7.x86_64.rpm  percona-xtrabackup-24-2.4.7-1.el7.x86_64.rpm

[root@localhost ~]# cat /etc/redhat-release 
CentOS Linux release 7.4.1708 (Core) 

[root@localhost ~]# xtrabackup --version
xtrabackup version 2.4.7 based on MySQL server 5.7.13 Linux (x86_64) (revision id: 6f7a799)

[root@localhost ~]# innobackupex --version
innobackupex version 2.4.7 Linux (x86_64) (revision id: 6f7a799)
```

## 备份恢复
创建备份目录

```shell
[root@localhost ~]# mkdir -pv /data/backup/all
mkdir: created directory ‘/data/backup/all’

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

Tips:
>   * defaults-file,user,password,socket 根据自己的实际配置修改
>   * 如果有MyISAM大表,不要在主库操作,低峰备份。
>   * use-memory=1G时 15k转 RAID10 备份时磁盘使用率80%