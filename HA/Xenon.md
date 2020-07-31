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
// 5.7 用xtrabackup2.4 版本
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

visudo
mysql           ALL=(ALL)       NOPASSWD: /usr/sbin/ip
mkdir -pv /data/xenon/bin
cd xenon xenoncli /data/xenon/bin
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
  MASTER_HOST='192.168.64.109',
  MASTER_USER='rep',
  MASTER_PASSWORD='213456',
  MASTER_LOG_FILE='mysql-bin.000001',
  MASTER_LOG_POS=154,
  MASTER_PORT=5001,
  MASTER_CONNECT_RETRY=10;

CHANGE MASTER TO MASTER_AUTO_POSITION = 1;
```

#### xenon 配置

```json
{
        "server":
        {
                "endpoint":"192.168.64.109:8801" //本机IP
        },

        "raft":
        {
                "meta-datadir":"raft.meta",
                "heartbeat-timeout":1000,
                "election-timeout":3000,
                "leader-start-command":"sudo ip a a 192.168.64.11/24 dev em1 && arping -c 3 -A 192.168.64.11 -I em1",
                "leader-stop-command":"sudo ip a d 192.168.64.11/24 dev em1"
        },

        "mysql":
        {
                "admin":"root",
                "passwd":"213456",
                "host":"127.0.0.1",
                "port":5001,
                "basedir":"/usr/local/mysql5001",
                "defaults-file":"/data/mysql5001/conf/my.cnf",
                "ping-timeout":1000,
                "master-sysvars":"super_read_only=0;read_only=0;sync_binlog=default;innodb_flush_log_at_trx_commit=default",
                "slave-sysvars": "super_read_only=1;read_only=1;sync_binlog=1000;innodb_flush_log_at_trx_commit=2"
        },

        "replication":
        {
                "user":"rep",
                "passwd":"213456"
        },

        "backup":
        {
                "ssh-host":"192.168.64.109", //本机IP
                "ssh-user":"mysql",
                "ssh-passwd":"mysql",
                "ssh-port":22,
                "backupdir":"/data/mysql5001/data",//mysql数据目录要和mysql配置文件中的datadir一致
                "xtrabackup-bindir":"/usr/bin",//xtrabackup 安装目录
                "backup-iops-limits":100000,
                "backup-use-memory": "1GB",
                "backup-parallel": 4
        },

        "rpc":
        {
                "request-timeout":500
        },

        "log":
        {
                "level":"DEBUG"
        }
}
```

其余两个节点修改下面两个值为本地IP：

​	endpoint

​	ssh-host

同时创建配置文件路径（xenon启动时依赖此路径）

```shell
echo '/data/xenon/xenon.json'>/data/xenon/bin/config.path
```

启动xenon

```shell
nohup /data/xenon/bin/xenon -c /data/xenon/xenon.json > /data/xenon/xenon.log 2>&1 &   
```

```shell
[mysql@svr157 data]$ tree xenon/
xenon/
├── bin
│   ├── config.path
│   ├── xenon
│   └── xenoncli
├── xenon.json
└── xenon.log
```



所有节点 添加raft 信息,以109节点为例：

```shell
/data/xenon/bin/xenoncli cluster add 192.168.64.154:8801,192.168.64.155:8801
[mysql@local-109 xenon]$ /data/xenon/bin/xenoncli cluster status   
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
|         ID          |              Raft               | Mysqld  | Monitor |          Backup          |        Mysql        | IO/SQL_RUNNING |      MyLeader       |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.154:8801 | [ViewID:182 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.109:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.109:8801 | [ViewID:182 EpochID:2]@LEADER   | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READWRITE] | [true/true]    | 192.168.64.109:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.155:8801 | [ViewID:182 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.109:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
(3 rows)
```



## 功能验证

#### 主库机器宕机 vip漂移

查看状态

```
[mysql@local-109 xenon]$ /data/xenon/bin/xenoncli cluster status   
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
|         ID          |              Raft               | Mysqld  | Monitor |          Backup          |        Mysql        | IO/SQL_RUNNING |      MyLeader       |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.154:8801 | [ViewID:182 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.109:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.109:8801 | [ViewID:182 EpochID:2]@LEADER   | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READWRITE] | [true/true]    | 192.168.64.109:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.155:8801 | [ViewID:182 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.109:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
(3 rows)
```

关闭mysql xenon

```shell
kill mysqld

kill xenon

```

切换log

```shell
2].get.vote.response.from[N:192.168.64.154:8801, R:FOLLOWER].rsp.gtid[{mysql-bin.000001 1247977  false No true Yes b92fe558-c7e2-11ea-8bd1-e0db551f93b4:55-3196 82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196  Slave has read all relay log; waiting for more updates   }].retcode[OK]
 2020/07/31 15:58:33.915650 	  [INFO]  	CANDIDATE[ID:192.168.64.155:8801, V:183, E:2].get.vote.response.from[N:192.168.64.154:8801, V:182].ok.votegranted[2].majoyrity[2]
 2020/07/31 15:58:35.253788 	  [DEBUG]  	CANDIDATE[ID:192.168.64.155:8801, V:183, E:2].timeout.to.check.brain.split
 2020/07/31 15:58:35.254276 	  [ERROR]  	CANDIDATE[ID:192.168.64.155:8801, V:183, E:2].send.ping.to.peer[192.168.64.109:8801].new.client.error[dial tcp 192.168.64.109:8801: connect: connection refused]
 2020/07/31 15:58:35.255593 	  [WARNING]  	CANDIDATE[ID:192.168.64.155:8801, V:183, E:2].send.ping.to.peer[192.168.64.154:8801].client.call.ok.rsp[&{{0 0    FOLLOWER} { 0  false  false        }  OK}]
 2020/07/31 15:58:35.396745 	  [WARNING]  	CANDIDATE[ID:192.168.64.155:8801, V:183, E:2].get.enough.votes[2]/members[3].become.leader
 2020/07/31 15:58:35.396782 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].candidate.state.machine.exit
 2020/07/31 15:58:35.396797 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].state.init
 2020/07/31 15:58:35.396818 	  [INFO]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].purge.bing.start[300000ms]...
 2020/07/31 15:58:35.396832 	  [INFO]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].check.semi-sync.thread.start[5000ms]...
 2020/07/31 15:58:35.396848 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].async.setting.prepare....
 2020/07/31 15:58:35.396875 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].state.machine.run
 2020/07/31 15:58:35.397268 	  [INFO]  	mysql.slave.status:&{mysql-bin.000001 1247977  false No true Yes b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196  Slave has read all relay log; waiting for more updates   }
 2020/07/31 15:58:35.397332 	  [INFO]  	mysql.slave.status:&{mysql-bin.000001 1247977  false No true Yes b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196  Slave has read all relay log; waiting for more updates   }
 2020/07/31 15:58:35.397363 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].my.gtid.is:{mysql-bin.000001 1247977  false No true Yes b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196  Slave has read all relay log; waiting for more updates   }
 2020/07/31 15:58:35.397377 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].1. mysql.WaitUntilAfterGTID.prepare
 2020/07/31 15:58:35.397636 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].mysql.WaitUntilAfterGTID.done
 2020/07/31 15:58:35.397663 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].2. mysql.ChangeToMaster.prepare
 2020/07/31 15:58:35.397700 	  [ERROR]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].send.heartbeat.to.peer[192.168.64.109:8801].new.client.error[dial tcp 192.168.64.109:8801: connect: connection refused]
 2020/07/31 15:58:35.397734 	  [ERROR]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].send.heartbeat.get.rsp[N:, V:0, E:0].error[ErrorRpcCall]
 2020/07/31 15:58:35.398945 	  [INFO]  	mysql.slave.status:&{mysql-bin.000001 1247977  false No true Yes b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196  Waiting for workers to exit   }
 2020/07/31 15:58:35.404379 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].mysql.ChangeToMaster.done
 2020/07/31 15:58:35.404415 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].3. mysql.EnableSemiSyncMaster.prepare
 2020/07/31 15:58:35.404869 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].mysql.EnableSemiSyncMaster.done
 2020/07/31 15:58:35.404896 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].4.mysql.SetSysVars.prepare
 2020/07/31 15:58:35.405745 	  [WARNING]  	mysql[127.0.0.1:5001].SetMasterGlobalSysVar[super_read_only=0;read_only=0;sync_binlog=1;innodb_flush_log_at_trx_commit=1]
 2020/07/31 15:58:35.405772 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].mysql.SetSysVars.done
 2020/07/31 15:58:35.405788 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].5. mysql.SetReadWrite.prepare
 2020/07/31 15:58:35.406427 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].mysql.SetReadWrite.done
 2020/07/31 15:58:35.406453 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].6. start.vip.prepare
 2020/07/31 15:58:36.397089 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].heartbeat.acks.granted[2].less.than.members[3].for.the.first.time
 2020/07/31 15:58:36.397122 	  [WARNING]  	LEADER[ID:192.168.64.155:8801, V:183, E:2].do.updateViewID[FROM:183 TO:185]
 2020/07/31 15:58:36.397551 	  [INFO]  	mysql.slave.status:&{ 0  false  false        }
 2020/07/31 15:58:36.397628 	  [INFO]  	mysql.slave.status:&{ 0  false  false        }
 2020/07/31 15:58:36.397899 	  [INFO]  	mysql.master.status:&{mysql-bin.000001 1206429  true  true   82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 0    }
 2020/07/31 15:58:36.398048 	  [INFO]  	mysql.master.status:&{mysql-bin.000001 1206429  true  true   82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 0    }
 2020/07/31 15:58:36.398474 	  [ERROR]  	LEADER[ID:192.168.64.155:8801, V:185, E:2].send.heartbeat.to.peer[192.168.64.109:8801].new.client.error[dial tcp 192.168.64.109:8801: connect: connection refused]
 2020/07/31 15:58:36.398509 	  [ERROR]  	LEADER[ID:192.168.64.155:8801, V:185, E:2].send.heartbeat.get.rsp[N:, V:0, E:0].error[ErrorRpcCall]
```



修复109 并加入集群

```shell
启动xenon
[mysql@local-109 xenon]$ nohup /data/xenon/bin/xenon -c /data/xenon/xenon.json >/data/xenon/xenon.log 2>&1 &
[1] 8664

[mysql@local-109 xenon]$ /data/xenon/bin/xenoncli cluster status
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
|         ID          |              Raft               | Mysqld  | Monitor |          Backup          |        Mysql        | IO/SQL_RUNNING |      MyLeader       |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.154:8801 | [ViewID:187 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.155:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.109:8801 | [ViewID:187 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.155:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.155:8801 | [ViewID:187 EpochID:2]@LEADER   | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READWRITE] | [true/true]    | 192.168.64.155:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
(3 rows)

[mysql@local-109 xenon]$ /data/xenon/bin/xenoncli mysql status
{"slave_io_running":true,"slave_sql_running":true,"mysqld_running":true,"mysql_working":true,"seconds_behind_master":"0","last_error":"","monitor":"ON"}[mysql@local-109 xenon]$ 


```



```

删除109数据
[mysql@local-109 xenon]$ rm -rf /data/mysql5001/data/*

报错日志

 2020/07/31 16:24:41.734217       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].change.master.to[FROM:192.168.64.155:8801, GTID:{192.168.64.155 5001 rep 213456}].error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:42.477919       [ERROR]       mysql[127.0.0.1:5001].ping.error[dial tcp 127.0.0.1:5001: connect: connection refused].downs:137,downslimits:2
 2020/07/31 16:24:42.477955       [ERROR]       mysql.dead.downs:137,downslimits:2
 2020/07/31 16:24:42.733359       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].mysql.DisableSemiSyncMaster.error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:42.733706       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].mysql.SetReadOnly.error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:42.734028       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].mysql.StartSlave.error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:42.734095       [WARNING]     LEARNER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.from[N:192.168.64.155:8801, V:193, E:2].change.mysql.master[{Master_Log_File:mysql-bin.000001 Read_Master_Log_Pos:1544933 Relay_Master_Log_File: Slave_IO_Running:true Slave_IO_Running_Str: Slave_SQL_Running:true Slave_SQL_Running_Str: Retrieved_GTID_Set: Executed_GTID_Set:3020803a-d2f2-11ea-b075-782bcb147c27:1-1292,
82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 Seconds_Behind_Master:0 Slave_SQL_Running_State: Last_Error: Last_IO_Error: Last_SQL_Error:}]
 2020/07/31 16:24:42.734467       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].change.master.to[FROM:192.168.64.155:8801, GTID:{192.168.64.155 5001 rep 213456}].error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:43.477934       [ERROR]       mysql[127.0.0.1:5001].ping.error[dial tcp 127.0.0.1:5001: connect: connection refused].downs:138,downslimits:2
 2020/07/31 16:24:43.477969       [ERROR]       mysql.dead.downs:138,downslimits:2
 2020/07/31 16:24:43.733651       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].mysql.DisableSemiSyncMaster.error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:43.733946       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].mysql.SetReadOnly.error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:43.734219       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].mysql.StartSlave.error[dial tcp 127.0.0.1:5001: connect: connection refused]
 2020/07/31 16:24:43.734285       [WARNING]     LEARNER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.from[N:192.168.64.155:8801, V:193, E:2].change.mysql.master[{Master_Log_File:mysql-bin.000001 Read_Master_Log_Pos:1545195 Relay_Master_Log_File: Slave_IO_Running:true Slave_IO_Running_Str: Slave_SQL_Running:true Slave_SQL_Running_Str: Retrieved_GTID_Set: Executed_GTID_Set:3020803a-d2f2-11ea-b075-782bcb147c27:1-1293,
82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
```



109 在线重做实例 

xenoncli mysql buildme

```shell
[mysql@local-109 mysql5001]$ /data/xenon/bin/xenoncli mysql rebuildme
 2020/07/31 16:23:36.154485       [WARNING]     =====prepare.to.rebuildme=====
                        IMPORTANT: Please check that the backup run completes successfully.
                                   At the end of a successful backup run innobackupex
                                   prints "completed OK!".

 2020/07/31 16:23:36.155499       [WARNING]     S1-->check.raft.leader
 2020/07/31 16:23:36.169510       [WARNING]     rebuildme.found.best.slave[192.168.64.154:8801].leader[192.168.64.155:8801]
 2020/07/31 16:23:36.169600       [WARNING]     S2-->prepare.rebuild.from[192.168.64.154:8801]....
 2020/07/31 16:23:36.171289       [WARNING]     S3-->check.bestone[192.168.64.154:8801].is.OK....
 2020/07/31 16:23:36.171388       [WARNING]     S4-->set.learner
 2020/07/31 16:23:36.172715       [WARNING]     S5-->stop.monitor
 2020/07/31 16:23:36.173752       [WARNING]     S6-->kill.mysql
 2020/07/31 16:23:36.344442       [WARNING]     S7-->check.bestone[192.168.64.154:8801].is.OK....
 2020/07/31 16:23:36.593235       [WARNING]     S8-->rm.datadir[/data/mysql5001/data]
 2020/07/31 16:23:36.593348       [WARNING]     S9-->xtrabackup.begin....
 2020/07/31 16:23:36.593941       [WARNING]     rebuildme.backup.req[&{From: BackupDir:/data/mysql5001/data SSHHost:192.168.64.109 SSHUser:mysql SSHPasswd:mysql SSHPort:22 IOPSLimits:100000 XtrabackupBinDir:/usr/bin}].from[192.168.64.154:8801]
 2020/07/31 16:23:52.364926       [WARNING]     S9-->xtrabackup.end....
 2020/07/31 16:23:52.364957       [WARNING]     S10-->apply-log.begin....
 2020/07/31 16:24:49.627819       [WARNING]     S10-->apply-log.end....
 2020/07/31 16:24:49.627837       [WARNING]     S11-->start.mysql.begin...
 2020/07/31 16:24:49.628775       [WARNING]     S11-->start.mysql.end...
 2020/07/31 16:24:49.628790       [WARNING]     S12-->wait.mysqld.running.begin....
 2020/07/31 16:24:52.690315       [WARNING]     wait.mysqld.running...
 2020/07/31 16:24:52.772373       [WARNING]     S12-->wait.mysqld.running.end....
 2020/07/31 16:24:52.772402       [WARNING]     S13-->wait.mysql.working.begin....
 2020/07/31 16:24:55.773865       [WARNING]     wait.mysql.working...
 2020/07/31 16:24:58.774512       [WARNING]     wait.mysql.working...
 2020/07/31 16:24:58.775043       [WARNING]     S13-->wait.mysql.working.end....
 2020/07/31 16:24:58.775064       [WARNING]     S14-->stop.and.reset.slave.begin....
 2020/07/31 16:24:58.920877       [WARNING]     S14-->stop.and.reset.slave.end....
 2020/07/31 16:24:58.920908       [WARNING]     S15-->reset.master.begin....
 2020/07/31 16:24:58.980683       [WARNING]     S15-->reset.master.end....
 2020/07/31 16:24:58.980801       [WARNING]     S15-->set.gtid_purged[3020803a-d2f2-11ea-b075-782bcb147c27:1-1244,
82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196
].begin....
 2020/07/31 16:24:58.996516       [WARNING]     S15-->set.gtid_purged.end....
 2020/07/31 16:24:58.996538       [WARNING]     S16-->enable.raft.begin...
 2020/07/31 16:24:58.997706       [WARNING]     S16-->enable.raft.done...
 2020/07/31 16:24:58.997739       [WARNING]     S17-->wait[3000 ms].change.to.master...
 2020/07/31 16:24:58.997767       [WARNING]     S18-->start.slave.begin....
 2020/07/31 16:24:59.060968       [WARNING]     S18-->start.slave.end....
 2020/07/31 16:24:59.060990       [WARNING]     completed OK!
 2020/07/31 16:24:59.060998       [WARNING]     rebuildme.all.done....
[mysql@local-109 mysql5001]$ 


```



rebuild log

```
 2020/07/31 16:24:58.737913       [WARNING]     LEARNER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.from[N:192.168.64.155:8801, V:193, E:2].change.mysql.master[{Master_Log_File:mysql-bin.000001 Read_Master_Log_Pos:1548601 Relay_Master_Log_File: Slave_IO_Running:true Slave_IO_Running_Str: Slave_SQL_Running:true Slave_SQL_Running_Str: Retrieved_GTID_Set: Executed_GTID_Set:3020803a-d2f2-11ea-b075-782bcb147c27:1-1306,
82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 Seconds_Behind_Master:0 Slave_SQL_Running_State: Last_Error: Last_IO_Error: Last_SQL_Error:}]
 2020/07/31 16:24:58.819476       [ERROR]       LEARNER[ID:192.168.64.109:8801, V:191, E:2].change.master.to[FROM:192.168.64.155:8801, GTID:{192.168.64.155 5001 rep 213456}].error[Error 1872: Slave failed to initialize relay log info structure from the repository]
 2020/07/31 16:24:58.997210       [WARNING]     LEARNER[ID:192.168.64.109:8801, V:191, E:2].RPC.HAEnable.call.from[]
 2020/07/31 16:24:58.997359       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].state.machine.loop.got.fired
 2020/07/31 16:24:58.997426       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].state.init
 2020/07/31 16:24:59.022749       [ERROR]       FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].leaderStartShellCommand[[-c sudo ip a d 192.168.64.11/24 dev em1]].out[bash -c sudo ip a d 192.168.64.11/24 dev em1RTNETLINK answers: Cannot assign requested address
].error[exit status 2]
 2020/07/31 16:24:59.022789       [ERROR]       FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].stopShellCommand.error[exit status 2]
 2020/07/31 16:24:59.022820       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].mysql.waitMysqlDoneAsync.prepare
 2020/07/31 16:24:59.022852       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].state.machine.run
 2020/07/31 16:24:59.023606       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].mysql.SetReadOnly.done
 2020/07/31 16:24:59.024297       [WARNING]     mysql[127.0.0.1:5001].SetSlaveGlobalSysVar[super_read_only=1;read_only=1;sync_binlog=1000;innodb_flush_log_at_trx_commit=2]
 2020/07/31 16:24:59.024330       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].mysql.SetSlaveGlobalSysVar.done
 2020/07/31 16:24:59.024344       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].prepareAsync.done
 2020/07/31 16:24:59.060913       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].init.my.gtid.is:{mysql-bin.000001 154  true  true   3020803a-d2f2-11ea-b075-782bcb147c27:1-1244,
82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 0    }
 2020/07/31 16:24:59.737546       [ERROR]       FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].mysql.StartSlave.error[Error 1200: The server is not configured as slave; fix in config file or with CHANGE MASTER TO]
 2020/07/31 16:24:59.738246       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.my.gtid.is:{mysql-bin.000001 154  true  true   3020803a-d2f2-11ea-b075-782bcb147c27:1-1244,
82e0da87-cc93-11ea-ad91-14feb5c77923:1-1649,
b92fe558-c7e2-11ea-8bd1-e0db551f93b4:1-3196 0    }
 2020/07/31 16:24:59.739231       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.from[N:192.168.64.155:8801, V:193, E:2].change.mysql.master
 2020/07/31 16:24:59.863801       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.change.to.the.new.master[192.168.64.155:8801].successed
 2020/07/31 16:24:59.863827       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].get.heartbeat.from[N:192.168.64.155:8801, V:193, E:2].update.view
 2020/07/31 16:24:59.863838       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:191, E:2].do.updateViewID[FROM:191 TO:193]
 2020/07/31 16:25:00.497643       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:193, E:2].ping.responses[1].is.less.than.half.maybe.brain.split
 2020/07/31 16:25:00.500880       [WARNING]     FOLLOWER[ID:192.168.64.109:8801, V:193, E:2].send.ping.to.peer[192.168.64.155:8801].client.call.ok.rsp[&{{0 0    LEADER} { 0  false  false        }  OK}]
```

主从状态恢复

```shell
[mysql@local-109 mysql5001]$ /data/xenon/bin/xenoncli mysql status
{"slave_io_running":true,"slave_sql_running":true,"mysqld_running":true,"mysql_working":true,"seconds_behind_master":"0","last_error":"","monitor":"ON"}[mysql@local-109 mysql5001]$ /data/xenon/bin/xenoncli cluster status
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
|         ID          |              Raft               | Mysqld  | Monitor |          Backup          |        Mysql        | IO/SQL_RUNNING |      MyLeader       |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.154:8801 | [ViewID:193 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.155:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.109:8801 | [ViewID:193 EpochID:2]@FOLLOWER | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READONLY]  | [true/true]    | 192.168.64.155:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
| 192.168.64.155:8801 | [ViewID:193 EpochID:2]@LEADER   | RUNNING | ON      | state:[NONE]␤            | [ALIVE] [READWRITE] | [true/true]    | 192.168.64.155:8801 |
|                     |                                 |         |         | LastError:               |                     |                |                     |
+---------------------+---------------------------------+---------+---------+--------------------------+---------------------+----------------+---------------------+
(3 rows)
```



添加新实例157

添加xenon

rebuild mysql 实例





## Reference

[https://github.com/radondb/xenon/blob/master/docs/how_to_build_and_run_xenon.md#step31-prepare-the-configuration-file](https://github.com/radondb/xenon/blob/master/docs/how_to_build_and_run_xenon.md#step31-prepare-the-configuration-file)

[https://blog.51cto.com/wujianwei/2458340](https://blog.51cto.com/wujianwei/2458340)

[[https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-%E9%83%A8%E7%BD%B2/](https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-部署/)]([https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-%E9%83%A8%E7%BD%B2/](https://www.fallbook.cn/2018/10/29/QingCloud-Mysql-Plus-Xenon-部署/))

