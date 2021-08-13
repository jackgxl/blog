# MHA_Configuration

[TOC]

## MHA结构

```shell
[root@localhost ~]# /data/mysql5723/bin/mysql --version
/data/mysql5723/bin/mysql  Ver 14.14 Distrib 5.7.23, for Linux (x86_64) using  EditLine wrapper
[root@localhost ~]# rpm -qa | grep mha                 
mha4mysql-node-0.58-0.el7.centos.noarch
```

|IP地址|角色|端口|
|:--:|:--:|:--:|
|192.168.64.182|Master_node|5723|
|192.168.64.101|Slave_node|5723|
|192.168.64.157|Slave_node|5723|
|192.168.64.160|MHA_Master||


## SSH 互信


每台HOST上都要执行

```shell
ssh-keygen -t RSA
ssh-copy-id -i /root/.ssh/id_rsa.pub root@'192.168.64.182'
ssh-copy-id -i /root/.ssh/id_rsa.pub root@'192.168.64.157'
ssh-copy-id -i /root/.ssh/id_rsa.pub root@'192.168.64.101'
```

mha需要调用mysqlbinlog命令，编译安装的MySQl需要做软连接

```
ln -sv /data/mysql5641/bin/mysqlbinlog /usr/local/bin/mysqlbinlog
```


## 配置MHA_Manage

### Configuration_file

```shell
[root@localhost ~]# cat /data/mha/masterha/app2.cnf 
[server default]
manager_workdir=/data/mha/app2
#manager_log=/data/mha/app2/app2.log
master_binlog_dir=/data/mysql5723/var
shutdown_script=""
#master_ip_failover_script=/data/mha/masterha/
#master_ip_online_change_script=/data/mha/masterha/master_online_change_new
#report_script=/data/mha/masterha/report.sh
user=root
password=Artron_2018
ping_interval=3
remote_workdir=/data/mha/app2
repl_user=rep
repl_password=rep
ssh_user=root

[server1]
hostname=192.168.64.182
port=5723
master_binlog_dir=/data/mysql5723/var
#candidate_master=1

[server2]
hostname=192.168.64.157
port=5723
candidate_master=1
master_binlog_dir=/data/mysql5723/var
#check_repl_delay=0

[server3]
hostname=192.168.64.101
port=5723
master_binlog_dir=/data/mysql5723/var

#[server4]
#hostname=host4
#no_master=1
[root@localhost ~]# 
```

### ssh check

```shell
[root@localhost ~]# masterha_check_ssh --conf=/data/mha/masterha/app2.cnf 
Tue Sep 18 13:41:54 2018 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.
Tue Sep 18 13:41:54 2018 - [info] Reading application default configuration from /data/mha/masterha/app2.cnf..
Tue Sep 18 13:41:54 2018 - [info] Reading server configuration from /data/mha/masterha/app2.cnf..
Tue Sep 18 13:41:54 2018 - [info] Starting SSH connection tests..
Tue Sep 18 13:41:55 2018 - [debug] 
Tue Sep 18 13:41:54 2018 - [debug]  Connecting via SSH from root@192.168.64.182(192.168.64.182:22) to root@192.168.64.157(192.168.64.157:22)..
Tue Sep 18 13:41:54 2018 - [debug]   ok.
Tue Sep 18 13:41:54 2018 - [debug]  Connecting via SSH from root@192.168.64.182(192.168.64.182:22) to root@192.168.64.101(192.168.64.101:22)..
Tue Sep 18 13:41:55 2018 - [debug]   ok.
Tue Sep 18 13:41:55 2018 - [debug] 
Tue Sep 18 13:41:54 2018 - [debug]  Connecting via SSH from root@192.168.64.157(192.168.64.157:22) to root@192.168.64.182(192.168.64.182:22)..
Tue Sep 18 13:41:55 2018 - [debug]   ok.
Tue Sep 18 13:41:55 2018 - [debug]  Connecting via SSH from root@192.168.64.157(192.168.64.157:22) to root@192.168.64.101(192.168.64.101:22)..
Tue Sep 18 13:41:55 2018 - [debug]   ok.
Tue Sep 18 13:41:56 2018 - [debug] 
Tue Sep 18 13:41:55 2018 - [debug]  Connecting via SSH from root@192.168.64.101(192.168.64.101:22) to root@192.168.64.182(192.168.64.182:22)..
Tue Sep 18 13:41:55 2018 - [debug]   ok.
Tue Sep 18 13:41:55 2018 - [debug]  Connecting via SSH from root@192.168.64.101(192.168.64.101:22) to root@192.168.64.157(192.168.64.157:22)..
Tue Sep 18 13:41:55 2018 - [debug]   ok.
Tue Sep 18 13:41:56 2018 - [info] All SSH connection tests passed successfully.
[root@localhost ~]# 
```

### slave check

```shell
[root@localhost ~]# masterha_check_repl --conf=/data/mha/masterha/app2.cnf    
Tue Sep 18 13:44:16 2018 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.
Tue Sep 18 13:44:16 2018 - [info] Reading application default configuration from /data/mha/masterha/app2.cnf..
Tue Sep 18 13:44:16 2018 - [info] Reading server configuration from /data/mha/masterha/app2.cnf..
Tue Sep 18 13:44:16 2018 - [info] MHA::MasterMonitor version 0.58.
Tue Sep 18 13:44:17 2018 - [info] GTID failover mode = 0
Tue Sep 18 13:44:17 2018 - [info] Dead Servers:
Tue Sep 18 13:44:17 2018 - [info] Alive Servers:
Tue Sep 18 13:44:17 2018 - [info]   192.168.64.182(192.168.64.182:5723)
Tue Sep 18 13:44:17 2018 - [info]   192.168.64.157(192.168.64.157:5723)
Tue Sep 18 13:44:17 2018 - [info]   192.168.64.101(192.168.64.101:5723)
Tue Sep 18 13:44:17 2018 - [info] Alive Slaves:
Tue Sep 18 13:44:17 2018 - [info]   192.168.64.157(192.168.64.157:5723)  Version=5.7.23-log (oldest major version between slaves) log-bin:enabled
Tue Sep 18 13:44:17 2018 - [info]     Replicating from 192.168.64.182(192.168.64.182:5723)
Tue Sep 18 13:44:17 2018 - [info]     Primary candidate for the new Master (candidate_master is set)
Tue Sep 18 13:44:17 2018 - [info]   192.168.64.101(192.168.64.101:5723)  Version=5.7.23-log (oldest major version between slaves) log-bin:enabled
Tue Sep 18 13:44:17 2018 - [info]     Replicating from 192.168.64.182(192.168.64.182:5723)
Tue Sep 18 13:44:17 2018 - [info] Current Alive Master: 192.168.64.182(192.168.64.182:5723)
Tue Sep 18 13:44:17 2018 - [info] Checking slave configurations..
Tue Sep 18 13:44:17 2018 - [info]  read_only=1 is not set on slave 192.168.64.157(192.168.64.157:5723).
Tue Sep 18 13:44:17 2018 - [info]  read_only=1 is not set on slave 192.168.64.101(192.168.64.101:5723).
Tue Sep 18 13:44:17 2018 - [info] Checking replication filtering settings..
Tue Sep 18 13:44:17 2018 - [info]  binlog_do_db= , binlog_ignore_db= 
Tue Sep 18 13:44:17 2018 - [info]  Replication filtering check ok.
Tue Sep 18 13:44:17 2018 - [info] GTID (with auto-pos) is not supported
Tue Sep 18 13:44:17 2018 - [info] Starting SSH connection tests..
Tue Sep 18 13:44:20 2018 - [info] All SSH connection tests passed successfully.
Tue Sep 18 13:44:20 2018 - [info] Checking MHA Node version..
Tue Sep 18 13:44:20 2018 - [info]  Version check ok.
Tue Sep 18 13:44:20 2018 - [info] Checking SSH publickey authentication settings on the current master..
Tue Sep 18 13:44:21 2018 - [info] HealthCheck: SSH to 192.168.64.182 is reachable.
Tue Sep 18 13:44:21 2018 - [info] Master MHA Node version is 0.58.
Tue Sep 18 13:44:21 2018 - [info] Checking recovery script configurations on 192.168.64.182(192.168.64.182:5723)..
Tue Sep 18 13:44:21 2018 - [info]   Executing command: save_binary_logs --command=test --start_pos=4 --binlog_dir=/data/mysql5723/var --output_file=/data/mha/app2/save_binary_logs_test --manager_version=0.58 --start_file=mysql-bin.000001 
Tue Sep 18 13:44:21 2018 - [info]   Connecting to root@192.168.64.182(192.168.64.182:22).. 
  Creating /data/mha/app2 if not exists..    ok.
  Checking output directory is accessible or not..
   ok.
  Binlog found at /data/mysql5723/var, up to mysql-bin.000001
Tue Sep 18 13:44:21 2018 - [info] Binlog setting check done.
Tue Sep 18 13:44:21 2018 - [info] Checking SSH publickey authentication and checking recovery script configurations on all alive slave servers..
Tue Sep 18 13:44:21 2018 - [info]   Executing command : apply_diff_relay_logs --command=test --slave_user='root' --slave_host=192.168.64.157 --slave_ip=192.168.64.157 --slave_port=5723 --workdir=/data/mha/app2 --target_version=5.7.23-log --manager_version=0.58 --relay_dir=/data/mysql5723/var --current_relay_log=relay-log.000001  --slave_pass=xxx
Tue Sep 18 13:44:21 2018 - [info]   Connecting to root@192.168.64.157(192.168.64.157:22).. 
  Checking slave recovery environment settings..
    Relay log found at /data/mysql5723/var, up to relay-log.000002
    Temporary relay log file is /data/mysql5723/var/relay-log.000002
    Checking if super_read_only is defined and turned on.. not present or turned off, ignoring.
    Testing mysql connection and privileges..
mysql: [Warning] Using a password on the command line interface can be insecure.
 done.
    Testing mysqlbinlog output.. done.
    Cleaning up test file(s).. done.
Tue Sep 18 13:44:22 2018 - [info]   Executing command : apply_diff_relay_logs --command=test --slave_user='root' --slave_host=192.168.64.101 --slave_ip=192.168.64.101 --slave_port=5723 --workdir=/data/mha/app2 --target_version=5.7.23-log --manager_version=0.58 --relay_dir=/data/mysql5723/var --current_relay_log=relay-log.000001  --slave_pass=xxx
Tue Sep 18 13:44:22 2018 - [info]   Connecting to root@192.168.64.101(192.168.64.101:22).. 
  Checking slave recovery environment settings..
    Relay log found at /data/mysql5723/var, up to relay-log.000002
    Temporary relay log file is /data/mysql5723/var/relay-log.000002
    Checking if super_read_only is defined and turned on.. not present or turned off, ignoring.
    Testing mysql connection and privileges..
mysql: [Warning] Using a password on the command line interface can be insecure.
 done.
    Testing mysqlbinlog output.. done.
    Cleaning up test file(s).. done.
Tue Sep 18 13:44:22 2018 - [info] Slaves settings check done.
Tue Sep 18 13:44:22 2018 - [info] 
192.168.64.182(192.168.64.182:5723) (current master)
 +--192.168.64.157(192.168.64.157:5723)
 +--192.168.64.101(192.168.64.101:5723)

Tue Sep 18 13:44:22 2018 - [info] Checking replication health on 192.168.64.157..
Tue Sep 18 13:44:22 2018 - [info]  ok.
Tue Sep 18 13:44:22 2018 - [info] Checking replication health on 192.168.64.101..
Tue Sep 18 13:44:22 2018 - [info]  ok.
Tue Sep 18 13:44:22 2018 - [warning] master_ip_failover_script is not defined.
Tue Sep 18 13:44:22 2018 - [warning] shutdown_script is not defined.
Tue Sep 18 13:44:22 2018 - [info] Got exit code 0 (Not master dead).

MySQL Replication Health is OK.
[root@localhost ~]# 
```

## 管理MHA

### 启动
```shell
nohup masterha_manager --conf=/data/mha/masterha/app2.cnf > /data/mha/app2/manager.log 2>&1 &
```

### 关闭

```shell
 masterha_stop --conf=/data/mha/masterha/app2.cnf 
```


