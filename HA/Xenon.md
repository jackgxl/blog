#  Xenon



## 下载安装

#### xenon

```shell
git clone https://github.com/xenon/xenon
cd xenon
make build
make test
ll bin/
-rwxr-xr-x 1 root root 12990945 Jul 15 11:59 xenon
-rwxr-xr-x 1 root root 12186684 Jul 15 11:59 xenoncli
```



#### xtrabackup

```shell
wget https://www.percona.com/downloads/Percona-XtraBackup-LATEST/Percona-XtraBackup-8.0.13/binary/redhat/7/x86_64/percona-xtrabackup-80-8.0.13-1.el7.x86_64.rpm
yum -y install percona-xtrabackup-80-8.0.13-1.el7.x86_64.rpm 
```





## 配置

#### mysql用户

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

#### SSL互信

```shell
ssh-keygen 
ssh-copy-id mysql@'192.168.64.109'
ssh-copy-id mysql@'192.168.64.154'
ssh-copy-id mysql@'192.168.64.155'
```



#### 启动MySQL，同步主从

```sql
CHANGE MASTER TO
  MASTER_HOST='192.168.64.154',
  MASTER_USER='rep',
  MASTER_PASSWORD='213456',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=154,
  MASTER_PORT=5001,
  MASTER_CONNECT_RETRY=10;

CHANGE MASTER TO MASTER_AUTO_POSITION = 1;
```

#### xenon 配置




## 功能验证

###  xenon mysql buildme

```shell
[mysql@local-155 xenon]$ ./bin/xenoncli mysql status
{"slave_io_running":false,"slave_sql_running":false,"mysqld_running":true,"mysql_working":false,"seconds_behind_master":"","last_error":"","monitor":"ON"}[mysql@local-155 xenon]$ ./bin/xenoncli c./bin/xenoncli mysql rebuildme                                                         
 2020/07/31 13:53:24.878284       [WARNING]     =====prepare.to.rebuildme=====
                        IMPORTANT: Please check that the backup run completes successfully.
                                   At the end of a successful backup run innobackupex
                                   prints "completed OK!".

 2020/07/31 13:53:24.879443       [WARNING]     S1-->check.raft.leader
 2020/07/31 13:53:25.152422       [WARNING]     best.slave.can't.found.set.to.leader[192.168.64.154:8801]
 2020/07/31 13:53:25.152486       [WARNING]     S2-->prepare.rebuild.from[192.168.64.154:8801]....
 2020/07/31 13:53:25.159562       [WARNING]     S3-->check.bestone[192.168.64.154:8801].is.OK....
 2020/07/31 13:53:25.159622       [WARNING]     S4-->set.learner
 2020/07/31 13:53:25.160701       [WARNING]     S5-->stop.monitor
 2020/07/31 13:53:25.161606       [WARNING]     S6-->kill.mysql
 2020/07/31 13:53:25.258047       [WARNING]     S7-->check.bestone[192.168.64.154:8801].is.OK....
 2020/07/31 13:53:25.535695       [WARNING]     S8-->rm.datadir[/data/mysql5001/data]
 2020/07/31 13:53:25.535736       [WARNING]     S9-->xtrabackup.begin....
 2020/07/31 13:53:25.536649       [WARNING]     rebuildme.backup.req[&{From: BackupDir:/data/mysql5001/data SSHHost:192.168.64.155 SSHUser:mysql SSHPasswd:mysql SSHPort:22 IOPSLimits:100000 XtrabackupBinDir:/usr/bin}].from[192.168.64.154:8801]
 2020/07/31 13:53:31.837525       [WARNING]     S9-->xtrabackup.end....
 2020/07/31 13:53:31.837588       [WARNING]     S10-->apply-log.begin....
 2020/07/31 13:53:38.411133       [WARNING]     S10-->apply-log.end....
 2020/07/31 13:53:38.411183       [WARNING]     S11-->start.mysql.begin...
 2020/07/31 13:53:38.412045       [WARNING]     S11-->start.mysql.end...
 2020/07/31 13:53:38.412081       [WARNING]     S12-->wait.mysqld.running.begin....
 2020/07/31 13:53:41.458856       [WARNING]     wait.mysqld.running...
 2020/07/31 13:53:41.505801       [WARNING]     S12-->wait.mysqld.running.end....
 2020/07/31 13:53:41.505859       [WARNING]     S13-->wait.mysql.working.begin....
 2020/07/31 13:53:44.526142       [WARNING]     S15-->set.gtid_purged.end....
 2020/07/31 13:53:44.526206       [WARNING]     S16-->enable.raft.begin...
 2020/07/31 13:53:44.527076       [WARNING]     S16-->enable.raft.done...
 2020/07/31 13:53:44.527159       [WARNING]     S17-->wait[3000 ms].change.to.master...
 2020/07/31 13:53:44.527220       [WARNING]     S18-->start.slave.begin....
 2020/07/31 13:53:44.531591       [WARNING]     S18-->start.slave.end....
 2020/07/31 13:53:44.531630       [WARNING]     completed OK!
 2020/07/31 13:53:44.531670       [WARNING]     rebuildme.all.done....
[mysql@local-155 xenon]$ ./bin/xenoncli mysql status                                                                                                                      
{"slave_io_running":true,"slave_sql_running":true,"mysqld_running":true,"mysql_working":true,"seconds_behind_master":"0","last_error":"","monitor":"ON"}[mysql@local-155 xenon]$ ./bin/xenoncli cluster status                                                                                                                                      
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
|         ID          |              Raft               | Mysqld  | Monitor |          Backup          |        Mysql        | IO/SQL_RUNNING |      MyLeader       |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.154:8801 | [ViewID:177 EpochID:2]@LEADER   | RUNNING | ON      | state:[NONE]
            | [ALIVE] [READWRITE] | [true/true]    | 192.168.64.154:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.109:8801 | [ViewID:177 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]
            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.154:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.155:8801 | [ViewID:177 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]
            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.154:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
(3 rows)
```





## Reference

[https://github.com/radondb/xenon/blob/master/docs/how_to_build_and_run_xenon.md#step31-prepare-the-configuration-file](https://github.com/radondb/xenon/blob/master/docs/how_to_build_and_run_xenon.md#step31-prepare-the-configuration-file)

[https://blog.51cto.com/wujianwei/2458340](https://blog.51cto.com/wujianwei/2458340)

[[https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-%E9%83%A8%E7%BD%B2/](https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-部署/)]([https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-%E9%83%A8%E7%BD%B2/](https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-部署/))

