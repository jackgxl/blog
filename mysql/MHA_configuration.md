# MHA_configuration

## MHA结构

|IP地址|角色|端口|
|:--:|:--:|:--:|
|192.168.64.182|Master_node|5641|
|192.168.64.101|Slave_node|5641|
|192.168.64.157|Slave_node|5641|
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


**ssh check**

```shell
[root@localhost masterha]# masterha_check_ssh --conf=app1.cnf 
Fri Sep 14 14:47:10 2018 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.
Fri Sep 14 14:47:10 2018 - [info] Reading application default configuration from app1.cnf..
Fri Sep 14 14:47:10 2018 - [info] Reading server configuration from app1.cnf..
Fri Sep 14 14:47:10 2018 - [info] Starting SSH connection tests..
Fri Sep 14 14:47:11 2018 - [debug] 
Fri Sep 14 14:47:10 2018 - [debug]  Connecting via SSH from root@192.168.64.182(192.168.64.182:22) to root@192.168.64.157(192.168.64.157:22)..
Fri Sep 14 14:47:10 2018 - [debug]   ok.
Fri Sep 14 14:47:10 2018 - [debug]  Connecting via SSH from root@192.168.64.182(192.168.64.182:22) to root@192.168.64.101(192.168.64.101:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:11 2018 - [debug] 
Fri Sep 14 14:47:10 2018 - [debug]  Connecting via SSH from root@192.168.64.157(192.168.64.157:22) to root@192.168.64.182(192.168.64.182:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:11 2018 - [debug]  Connecting via SSH from root@192.168.64.157(192.168.64.157:22) to root@192.168.64.101(192.168.64.101:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:12 2018 - [debug] 
Fri Sep 14 14:47:11 2018 - [debug]  Connecting via SSH from root@192.168.64.101(192.168.64.101:22) to root@192.168.64.182(192.168.64.182:22)..
Fri Sep 14 14:47:11 2018 - [debug]   ok.
Fri Sep 14 14:47:11 2018 - [debug]  Connecting via SSH from root@192.168.64.101(192.168.64.101:22) to root@192.168.64.157(192.168.64.157:22)..
Fri Sep 14 14:47:12 2018 - [debug]   ok.
Fri Sep 14 14:47:12 2018 - [info] All SSH connection tests passed successfully.
```

**slave check**

```shell
[root@localhost masterha]# masterha_check_repl --conf=app1.cnf 
Fri Sep 14 14:59:12 2018 - [warning] Global configuration file /etc/masterha_default.cnf not found. Skipping.
Fri Sep 14 14:59:12 2018 - [info] Reading application default configuration from app1.cnf..
Fri Sep 14 14:59:12 2018 - [info] Reading server configuration from app1.cnf..
Fri Sep 14 14:59:12 2018 - [info] MHA::MasterMonitor version 0.58.
Fri Sep 14 14:59:14 2018 - [info] GTID failover mode = 0
Fri Sep 14 14:59:14 2018 - [info] Dead Servers:
Fri Sep 14 14:59:14 2018 - [info] Alive Servers:
Fri Sep 14 14:59:14 2018 - [info]   192.168.64.182(192.168.64.182:5641)
Fri Sep 14 14:59:14 2018 - [info]   192.168.64.157(192.168.64.157:5641)
Fri Sep 14 14:59:14 2018 - [info]   192.168.64.101(192.168.64.101:5641)
Fri Sep 14 14:59:14 2018 - [info] Alive Slaves:
Fri Sep 14 14:59:14 2018 - [info]   192.168.64.157(192.168.64.157:5641)  Version=5.6.41-log (oldest major version between slaves) log-bin:enabled
Fri Sep 14 14:59:14 2018 - [info]     Replicating from 192.168.64.182(192.168.64.182:5641)
Fri Sep 14 14:59:14 2018 - [info]     Primary candidate for the new Master (candidate_master is set)
Fri Sep 14 14:59:14 2018 - [info]   192.168.64.101(192.168.64.101:5641)  Version=5.6.41-log (oldest major version between slaves) log-bin:enabled
Fri Sep 14 14:59:14 2018 - [info]     Replicating from 192.168.64.182(192.168.64.182:5641)
Fri Sep 14 14:59:14 2018 - [info] Current Alive Master: 192.168.64.182(192.168.64.182:5641)
Fri Sep 14 14:59:14 2018 - [info] Checking slave configurations..
Fri Sep 14 14:59:14 2018 - [info]  read_only=1 is not set on slave 192.168.64.157(192.168.64.157:5641).
Fri Sep 14 14:59:14 2018 - [info]  read_only=1 is not set on slave 192.168.64.101(192.168.64.101:5641).
Fri Sep 14 14:59:14 2018 - [info] Checking replication filtering settings..
Fri Sep 14 14:59:14 2018 - [info]  binlog_do_db= , binlog_ignore_db= 
Fri Sep 14 14:59:14 2018 - [info]  Replication filtering check ok.
Fri Sep 14 14:59:14 2018 - [info] GTID (with auto-pos) is not supported
Fri Sep 14 14:59:14 2018 - [info] Starting SSH connection tests..
Fri Sep 14 14:59:16 2018 - [info] All SSH connection tests passed successfully.
Fri Sep 14 14:59:16 2018 - [info] Checking MHA Node version..
Fri Sep 14 14:59:17 2018 - [info]  Version check ok.
Fri Sep 14 14:59:17 2018 - [info] Checking SSH publickey authentication settings on the current master..
Fri Sep 14 14:59:17 2018 - [info] HealthCheck: SSH to 192.168.64.182 is reachable.
Fri Sep 14 14:59:17 2018 - [info] Master MHA Node version is 0.58.
Fri Sep 14 14:59:17 2018 - [info] Checking recovery script configurations on 192.168.64.182(192.168.64.182:5641)..
Fri Sep 14 14:59:17 2018 - [info]   Executing command: save_binary_logs --command=test --start_pos=4 --binlog_dir=/data/mysql5641/var --output_file=/data/mha/save_binary_logs_test --manager_version=0.58 --start_file=mysql-bin.000001 
Fri Sep 14 14:59:17 2018 - [info]   Connecting to root@192.168.64.182(192.168.64.182:22).. 
  Creating /data/mha if not exists..    ok.
  Checking output directory is accessible or not..
   ok.
  Binlog found at /data/mysql5641/var, up to mysql-bin.000001
Fri Sep 14 14:59:18 2018 - [info] Binlog setting check done.
Fri Sep 14 14:59:18 2018 - [info] Checking SSH publickey authentication and checking recovery script configurations on all alive slave servers..
Fri Sep 14 14:59:18 2018 - [info]   Executing command : apply_diff_relay_logs --command=test --slave_user='mha' --slave_host=192.168.64.157 --slave_ip=192.168.64.157 --slave_port=5641 --workdir=/data/mha --target_version=5.6.41-log --manager_version=0.58 --relay_log_info=/data/mysql5641/var/relay-log.info  --relay_dir=/data/mysql5641/var/  --slave_pass=xxx
Fri Sep 14 14:59:18 2018 - [info]   Connecting to root@192.168.64.157(192.168.64.157:22).. 
Creating directory /data/mha.. done.
  Checking slave recovery environment settings..
    Opening /data/mysql5641/var/relay-log.info ... ok.
    Relay log found at /data/mysql5641/var, up to relay-log.000002
    Temporary relay log file is /data/mysql5641/var/relay-log.000002
    Checking if super_read_only is defined and turned on..DBD::mysql::st execute failed: Unknown system variable 'super_read_only' at /usr/share/perl5/vendor_perl/MHA/SlaveUtil.pm line 245.
Fri Sep 14 14:59:18 2018 - [error][/usr/share/perl5/vendor_perl/MHA/MasterMonitor.pm, ln208] Slaves settings check failed!
Fri Sep 14 14:59:18 2018 - [error][/usr/share/perl5/vendor_perl/MHA/MasterMonitor.pm, ln416] Slave configuration failed.
Fri Sep 14 14:59:18 2018 - [error][/usr/share/perl5/vendor_perl/MHA/MasterMonitor.pm, ln427] Error happened on checking configurations.  at /usr/bin/masterha_check_repl line 48.
Fri Sep 14 14:59:18 2018 - [error][/usr/share/perl5/vendor_perl/MHA/MasterMonitor.pm, ln525] Error happened on monitoring servers.
Fri Sep 14 14:59:18 2018 - [info] Got exit code 1 (Not master dead).

MySQL Replication Health is NOT OK!
```


##

