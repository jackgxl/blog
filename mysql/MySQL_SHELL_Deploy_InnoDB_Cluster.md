# MySQL SHELL Deploy InnoDB Cluster

## tips:

*   每个节点安装mysqlshell
*   创建组复制账号
*   在本地检查集群各节点是否处于可以部署集群的状态

## 管理节点 mysqlsh 登录mgr1

```
 MySQL  JS > shell.connect('sh_user@mgr1:3310')
Please provide the password for 'sh_user@mgr1:3310': *********
Creating a session to 'sh_user@mgr1:3310'
Fetching schema names for autocompletion... Press ^C to stop.
Your MySQL connection id is 26
Server version: 8.0.11 Source distribution
No default schema selected; type \use <schema> to set one.
```

## 管理节点 创建InnoDB Cluster

```
 MySQL  mgr1:3310 ssl  JS > var cluster = dba.createCluster('proCluster');
A new InnoDB cluster will be created on instance 'sh_user@mgr1:3310'.

Validating instance at mgr1:3310...

This instance reports its own address as mgr1
DBA: mysqlprovision: Executing '[{"server":{"host":"mgr1","passwd":"****","password":"****","port":3310,"scheme":"mysql","user":"sh_user"},"verbose":2}]\n.\n' | mysqlsh --log-level=8 --py -f /usr/share/mysqlsh/mysqlprovision.zip check
=========================== MySQL Provision Output ===========================

DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
Running check command.
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status where CHANNEL_NAME = 'group_replication_applier'
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
Checking Group Replication prerequisites.
DEBUG: The server: 'mgr1:3310' has been set to check
DEBUG: Option checking started: {'log_slave_updates': {'ONE OF': ('ON', '1')}, 'binlog_format': {'ONE OF': ('ROW',)}, 'relay_log_info_repository': {'ONE OF': ('TABLE',)}, 'binlog_checksum': {'ONE OF': ('NONE',)}, 'report_port': {'ONE OF': ('3310',)}, 'enforce_gtid_consistency': {'ONE OF': ('ON', '1')}, 'master_info_repository': {'ONE OF': ('TABLE',)}, 'log_bin': {'ONE OF': ('1', 'ON')}, 'gtid_mode': {'ONE OF': ('ON',)}, 'transaction_write_set_extraction': {'ONE OF': ('XXHASH64', '2', 'MURMUR32', '1')}}
DEBUG: Checking option: 'log_slave_updates' 
DEBUG: MySQL query: SELECT @@log_slave_updates
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('ON', '1')
DEBUG: Checking option: 'binlog_format' 
DEBUG: MySQL query: SELECT @@binlog_format
DEBUG: Option current value: 'ROW' 
DEBUG: OK: value ROW is one of ('ROW',)
DEBUG: Checking option: 'relay_log_info_repository' 
DEBUG: MySQL query: SELECT @@relay_log_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'binlog_checksum' 
DEBUG: MySQL query: SELECT @@binlog_checksum
DEBUG: Option current value: 'NONE' 
DEBUG: OK: value NONE is one of ('NONE',)
DEBUG: Checking option: 'report_port' 
DEBUG: MySQL query: SELECT @@report_port
DEBUG: Option current value: '3310' 
DEBUG: OK: value 3310 is one of ('3310',)
DEBUG: Checking option: 'enforce_gtid_consistency' 
DEBUG: MySQL query: SELECT @@enforce_gtid_consistency
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON', '1')
DEBUG: Checking option: 'master_info_repository' 
DEBUG: MySQL query: SELECT @@master_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'log_bin' 
DEBUG: MySQL query: SELECT @@log_bin
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('1', 'ON')
DEBUG: Checking option: 'gtid_mode' 
DEBUG: MySQL query: SELECT @@gtid_mode
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON',)
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@transaction_write_set_extraction
DEBUG: Option current value: 'XXHASH64' 
DEBUG: OK: value XXHASH64 is one of ('XXHASH64', '2', 'MURMUR32', '1')
DEBUG: Options check result: True
* Comparing options compatibility with Group Replication... PASS
Server configuration is compliant with the requirements.
DEBUG: Server version checking: 5.7.17
DEBUG: MySQL query: SHOW VARIABLES LIKE 'VERSION'
DEBUG: Server version: [8, 0, 11]
DEBUG: Server version check result: True
* Checking server version... PASS
Server is 8.0.11

DEBUG: checking server id uniqueness
DEBUG: MySQL query: SELECT @@server_id
DEBUG: server id = 152
DEBUG: MySQL query: SELECT variable_source FROM performance_schema.variables_info WHERE variable_name='server_id'
* Checking that server_id is unique... PASS
The server_id is valid.

DEBUG: MySQL query: SELECT @@slave_parallel_workers
* Checking compatibility of Multi-Threaded Slave settings... PASS
Multi-Threaded Slave settings are compatible with Group Replication.

DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'group_replication%'
DEBUG: Plugin group_replication has state: ACTIVE and not the expected: DISABLED
==============================================================================

Instance configuration is suitable.
Creating InnoDB cluster 'proCluster' on 'sh_user@mgr1:3310'...
DBA: mysqlprovision: Executing '[{"rep_user_passwd":"****","replication_user":"mysql_innodb_cluster_r2433899910","ssl_mode":"REQUIRED","verbose":2},{"host":"mgr1","passwd":"****","password":"****","port":3310,"scheme":"mysql","user":"sh_user"}]\n.\n' | mysqlsh --log-level=8 --py -f /usr/share/mysqlsh/mysqlprovision.zip start-replicaset
=========================== MySQL Provision Output ===========================
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'

Running start command on 'mgr1:3310'.
Checking Group Replication prerequisites.
DEBUG: MySQL query: SELECT @@have_ssl
DEBUG: ->parse_server_address 
  host: % 
  address_type: host like
DEBUG: Using replication_user: mysql_innodb_cluster_r2433899910@'%'
DEBUG: ->rpl_user_dict {'replication_user': "mysql_innodb_cluster_r2433899910@'%'", 'rep_user_passwd': '******', 'host': '%', 'recovery_user': 'mysql_innodb_cluster_r2433899910', 'ssl_mode': u'REQUIRED'}
DEBUG: The server: 'mgr1:3310' has been set to check
DEBUG: Option checking started: {'log_slave_updates': {'ONE OF': ('ON', '1')}, 'binlog_format': {'ONE OF': ('ROW',)}, 'relay_log_info_repository': {'ONE OF': ('TABLE',)}, 'binlog_checksum': {'ONE OF': ('NONE',)}, 'report_port': {'ONE OF': ('3310',)}, 'enforce_gtid_consistency': {'ONE OF': ('ON', '1')}, 'master_info_repository': {'ONE OF': ('TABLE',)}, 'log_bin': {'ONE OF': ('1', 'ON')}, 'gtid_mode': {'ONE OF': ('ON',)}, 'transaction_write_set_extraction': {'ONE OF': ('XXHASH64', '2', 'MURMUR32', '1')}}
DEBUG: Checking option: 'log_slave_updates' 
DEBUG: MySQL query: SELECT @@log_slave_updates
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('ON', '1')
DEBUG: Checking option: 'binlog_format' 
DEBUG: MySQL query: SELECT @@binlog_format
DEBUG: Option current value: 'ROW' 
DEBUG: OK: value ROW is one of ('ROW',)
DEBUG: Checking option: 'relay_log_info_repository' 
DEBUG: MySQL query: SELECT @@relay_log_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'binlog_checksum' 
DEBUG: MySQL query: SELECT @@binlog_checksum
DEBUG: Option current value: 'NONE' 
DEBUG: OK: value NONE is one of ('NONE',)
DEBUG: Checking option: 'report_port' 
DEBUG: MySQL query: SELECT @@report_port
DEBUG: Option current value: '3310' 
DEBUG: OK: value 3310 is one of ('3310',)
DEBUG: Checking option: 'enforce_gtid_consistency' 
DEBUG: MySQL query: SELECT @@enforce_gtid_consistency
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON', '1')
DEBUG: Checking option: 'master_info_repository' 
DEBUG: MySQL query: SELECT @@master_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'log_bin' 
DEBUG: MySQL query: SELECT @@log_bin
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('1', 'ON')
DEBUG: Checking option: 'gtid_mode' 
DEBUG: MySQL query: SELECT @@gtid_mode
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON',)
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@transaction_write_set_extraction
DEBUG: Option current value: 'XXHASH64' 
DEBUG: OK: value XXHASH64 is one of ('XXHASH64', '2', 'MURMUR32', '1')
DEBUG: Options check result: True
* Comparing options compatibility with Group Replication... PASS
Server configuration is compliant with the requirements.
DEBUG: Server version checking: 5.7.17
DEBUG: MySQL query: SHOW VARIABLES LIKE 'VERSION'
DEBUG: Server version: [8, 0, 11]
DEBUG: Server version check result: True
* Checking server version... PASS
Server is 8.0.11

DEBUG: checking server id uniqueness
DEBUG: MySQL query: SELECT @@server_id
DEBUG: server id = 152
DEBUG: MySQL query: SELECT variable_source FROM performance_schema.variables_info WHERE variable_name='server_id'
* Checking that server_id is unique... PASS
The server_id is valid.

DEBUG: MySQL query: SELECT @@slave_parallel_workers
* Checking compatibility of Multi-Threaded Slave settings... PASS
Multi-Threaded Slave settings are compatible with Group Replication.

DEBUG: privileges Checking
DEBUG: User: mysql_innodb_cluster_r2433899910@'%' required privileges: ('REPLICATION SLAVE',)
DEBUG: ->parse_server_address 
  host: % 
  address_type: host like
DEBUG: MySQL query: SELECT * FROM mysql.user WHERE user = ? and host = ?, params ('mysql_innodb_cluster_r2433899910', '%')
DEBUG: MySQL query: SHOW GRANTS FOR 'snuffles'@'host'
DEBUG: MySQL query: SELECT CURRENT_USER()
DEBUG: MySQL query: SHOW GRANTS FOR 'mysql_innodb_cluster_r2433899910'@'%'
DEBUG: MySQL query: SELECT @@SQL_MODE
DEBUG: missing privileges: 
DEBUG: User: sh_user@'mgr1' required privileges: ('CREATE USER', 'SUPER', 'REPLICATION SLAVE')
DEBUG: ->parse_server_address 
  host: mgr1 
  address_type: hostname
DEBUG: MySQL query: SELECT * FROM mysql.user WHERE user = ? and host = ?, params ('sh_user', 'mgr1')
DEBUG: Privileges check result: {"mysql_innodb_cluster_r2433899910@'%'": '', "sh_user@'mgr1'": ['NO EXISTS!'], 'pass': False}
The user sh_user@'mgr1' does not exists on 'mgr1:3310' and requires to be created.
DEBUG: Replication user has REPLICATION SLAVE.
DEBUG: check user privileges result: {"mysql_innodb_cluster_r2433899910@'%'": '', "sh_user@'mgr1'": ['NO EXISTS!'], 'pass': False}.
* Checking user privileges... PASS
DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'group_replication%'
DEBUG: Plugin group_replication has state: ACTIVE and not the expected: DISABLED
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
DEBUG: MySQL query: SELECT @@server_id
DEBUG: MySQL query: SELECT UUID()
DEBUG: A new UUID has been generated for the group replication name a05740e5-7842-11e8-adaf-d067e5fdda78
Group Replication group name: a05740e5-7842-11e8-adaf-d067e5fdda78
DEBUG: Setting Group Replication variables
DEBUG:   group_replication_single_primary_mode = "ON"
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_single_primary_mode = "ON"
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_group_name = a05740e5-7842-11e8-adaf-d067e5fdda78
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_group_name = ?, params ('a05740e5-7842-11e8-adaf-d067e5fdda78',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_recovery_use_ssl = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_recovery_use_ssl = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   auto_increment_offset = 6
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST auto_increment_offset = ?, params (6,)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_ssl_mode = 'REQUIRED'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_ssl_mode = 'REQUIRED'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_start_on_boot = ON
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_start_on_boot = ?, params ('ON',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_local_address = 'mgr1:49178'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_local_address = 'mgr1:49178'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   auto_increment_increment = 7
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST auto_increment_increment = ?, params (7,)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
* Running change master command
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: CHANGE MASTER TO MASTER_USER = /*(*/ 'mysql_innodb_cluster_r2433899910' /*)*/, MASTER_PASSWORD = /*(*/ '******' /*)*/ FOR CHANNEL 'group_replication_recovery';
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG: MySQL query: SET PERSIST group_replication_bootstrap_group = 1
Attempting to start the Group Replication group...
DEBUG: 
DEBUG: * Starting Group Replication plugin...
DEBUG: MySQL query: START group_replication
DEBUG: MySQL query: SELECT @@global.super_read_only
DEBUG: super_read_only: 1
DEBUG: have been waiting 1 seconds
DEBUG: MySQL query: SELECT @@global.super_read_only
DEBUG: super_read_only: 0
Group Replication started for group: a05740e5-7842-11e8-adaf-d067e5fdda78.
DEBUG: MySQL query: SET PERSIST group_replication_bootstrap_group = 0
==============================================================================
Adding Seed Instance...

Cluster successfully created. Use Cluster.addInstance() to add MySQL instances.
At least 3 instances are needed for the cluster to be able to withstand up to
one server failure.
```

## 添加第一个节点后集群状态

```
MySQL  mgr1:3310 ssl  JS > cluster.status();
{
    "clusterName": "proCluster", 
    "defaultReplicaSet": {
        "name": "default", 
        "primary": "mgr1:3310", 
        "ssl": "REQUIRED", 
        "status": "OK_NO_TOLERANCE", 
        "statusText": "Cluster is NOT tolerant to any failures.", 
        "topology": {
            "mgr1:3310": {
                "address": "mgr1:3310", 
                "mode": "R/W", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }
        }
    }, 
    "groupInformationSourceMember": "mysql://sh_user@mgr1:3310"
}
```

## 添加第二个节点

```
 MySQL  mgr1:3310 ssl  JS > cluster.addInstance('sh_user@mgr2:3310')
A new instance will be added to the InnoDB cluster. Depending on the amount of
data on the cluster this might take from a few seconds to several hours.

Please provide the password for 'sh_user@mgr2:3310': *********
Adding instance to the cluster ...

Validating instance at mgr2:3310...

This instance reports its own address as mgr2
DBA: mysqlprovision: Executing '[{"server":{"host":"mgr2","passwd":"****","password":"****","port":3310,"scheme":"mysql","user":"sh_user"},"verbose":2}]\n.\n' | mysqlsh --log-level=8 --py -f /usr/share/mysqlsh/mysqlprovision.zip check
=========================== MySQL Provision Output ===========================

DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
Running check command.
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status where CHANNEL_NAME = 'group_replication_applier'
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
Checking Group Replication prerequisites.
DEBUG: The server: 'mgr2:3310' has been set to check
DEBUG: Option checking started: {'log_slave_updates': {'ONE OF': ('ON', '1')}, 'binlog_format': {'ONE OF': ('ROW',)}, 'relay_log_info_repository': {'ONE OF': ('TABLE',)}, 'binlog_checksum': {'ONE OF': ('NONE',)}, 'report_port': {'ONE OF': ('3310',)}, 'enforce_gtid_consistency': {'ONE OF': ('ON', '1')}, 'master_info_repository': {'ONE OF': ('TABLE',)}, 'log_bin': {'ONE OF': ('1', 'ON')}, 'gtid_mode': {'ONE OF': ('ON',)}, 'transaction_write_set_extraction': {'ONE OF': ('XXHASH64', '2', 'MURMUR32', '1')}}
DEBUG: Checking option: 'log_slave_updates' 
DEBUG: MySQL query: SELECT @@log_slave_updates
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('ON', '1')
DEBUG: Checking option: 'binlog_format' 
DEBUG: MySQL query: SELECT @@binlog_format
DEBUG: Option current value: 'ROW' 
DEBUG: OK: value ROW is one of ('ROW',)
DEBUG: Checking option: 'relay_log_info_repository' 
DEBUG: MySQL query: SELECT @@relay_log_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'binlog_checksum' 
DEBUG: MySQL query: SELECT @@binlog_checksum
DEBUG: Option current value: 'NONE' 
DEBUG: OK: value NONE is one of ('NONE',)
DEBUG: Checking option: 'report_port' 
DEBUG: MySQL query: SELECT @@report_port
DEBUG: Option current value: '3310' 
DEBUG: OK: value 3310 is one of ('3310',)
DEBUG: Checking option: 'enforce_gtid_consistency' 
DEBUG: MySQL query: SELECT @@enforce_gtid_consistency
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON', '1')
DEBUG: Checking option: 'master_info_repository' 
DEBUG: MySQL query: SELECT @@master_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'log_bin' 
DEBUG: MySQL query: SELECT @@log_bin
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('1', 'ON')
DEBUG: Checking option: 'gtid_mode' 
DEBUG: MySQL query: SELECT @@gtid_mode
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON',)
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@transaction_write_set_extraction
DEBUG: Option current value: 'XXHASH64' 
DEBUG: OK: value XXHASH64 is one of ('XXHASH64', '2', 'MURMUR32', '1')
DEBUG: Options check result: True
* Comparing options compatibility with Group Replication... PASS
Server configuration is compliant with the requirements.
DEBUG: Server version checking: 5.7.17
DEBUG: MySQL query: SHOW VARIABLES LIKE 'VERSION'
DEBUG: Server version: [8, 0, 11]
DEBUG: Server version check result: True
* Checking server version... PASS
Server is 8.0.11

DEBUG: checking server id uniqueness
DEBUG: MySQL query: SELECT @@server_id
DEBUG: server id = 154
DEBUG: MySQL query: SELECT variable_source FROM performance_schema.variables_info WHERE variable_name='server_id'
* Checking that server_id is unique... PASS
The server_id is valid.

DEBUG: MySQL query: SELECT @@slave_parallel_workers
* Checking compatibility of Multi-Threaded Slave settings... PASS
Multi-Threaded Slave settings are compatible with Group Replication.

DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'group_replication%'
DEBUG: Plugin group_replication has state: ACTIVE and not the expected: DISABLED
==============================================================================

Instance configuration is suitable.
DBA: mysqlprovision: Executing '[{"group_seeds":"mgr1:49178","rep_user_passwd":"****","replication_user":"mysql_innodb_cluster_r2433924357","ssl_mode":"REQUIRED","verbose":2},{"host":"mgr2","passwd":"****","password":"****","port":3310,"user":"sh_user"},{"host":"mgr1","passwd":"****","port":3310,"user":"sh_user"}]\n.\n' | mysqlsh --log-level=8 --py -f /usr/share/mysqlsh/mysqlprovision.zip join-replicaset
=========================== MySQL Provision Output ===========================
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'

Running join command on 'mgr2:3310'.
Checking Group Replication prerequisites.
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status where CHANNEL_NAME = 'group_replication_applier'
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
DEBUG: MySQL query: SELECT @@have_ssl
DEBUG: MySQL query: SELECT @@group_replication_recovery_use_ssl
DEBUG: MySQL query: SELECT @@group_replication_ssl_mode
DEBUG: ->parse_server_address 
  host: % 
  address_type: host like
DEBUG: Using replication_user: mysql_innodb_cluster_r2433924357@'%'
DEBUG: ->rpl_user_dict {'replication_user': "mysql_innodb_cluster_r2433924357@'%'", 'rep_user_passwd': '******', 'host': '%', 'recovery_user': 'mysql_innodb_cluster_r2433924357', 'ssl_mode': u'REQUIRED'}
DEBUG: MySQL query: select MEMBER_HOST, MEMBER_PORT from performance_schema.replication_group_members
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
DEBUG: The server: 'mgr2:3310' has been set to check
DEBUG: Option checking started: {'log_slave_updates': {'ONE OF': ('ON', '1')}, 'binlog_format': {'ONE OF': ('ROW',)}, 'relay_log_info_repository': {'ONE OF': ('TABLE',)}, 'binlog_checksum': {'ONE OF': ('NONE',)}, 'report_port': {'ONE OF': ('3310',)}, 'enforce_gtid_consistency': {'ONE OF': ('ON', '1')}, 'master_info_repository': {'ONE OF': ('TABLE',)}, 'log_bin': {'ONE OF': ('1', 'ON')}, 'gtid_mode': {'ONE OF': ('ON',)}, 'transaction_write_set_extraction': {'ONE OF': ('XXHASH64', '2', 'MURMUR32', '1')}}
DEBUG: Checking option: 'log_slave_updates' 
DEBUG: MySQL query: SELECT @@log_slave_updates
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('ON', '1')
DEBUG: Checking option: 'binlog_format' 
DEBUG: MySQL query: SELECT @@binlog_format
DEBUG: Option current value: 'ROW' 
DEBUG: OK: value ROW is one of ('ROW',)
DEBUG: Checking option: 'relay_log_info_repository' 
DEBUG: MySQL query: SELECT @@relay_log_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'binlog_checksum' 
DEBUG: MySQL query: SELECT @@binlog_checksum
DEBUG: Option current value: 'NONE' 
DEBUG: OK: value NONE is one of ('NONE',)
DEBUG: Checking option: 'report_port' 
DEBUG: MySQL query: SELECT @@report_port
DEBUG: Option current value: '3310' 
DEBUG: OK: value 3310 is one of ('3310',)
DEBUG: Checking option: 'enforce_gtid_consistency' 
DEBUG: MySQL query: SELECT @@enforce_gtid_consistency
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON', '1')
DEBUG: Checking option: 'master_info_repository' 
DEBUG: MySQL query: SELECT @@master_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'log_bin' 
DEBUG: MySQL query: SELECT @@log_bin
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('1', 'ON')
DEBUG: Checking option: 'gtid_mode' 
DEBUG: MySQL query: SELECT @@gtid_mode
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON',)
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@transaction_write_set_extraction
DEBUG: Option current value: 'XXHASH64' 
DEBUG: OK: value XXHASH64 is one of ('XXHASH64', '2', 'MURMUR32', '1')
DEBUG: Options check result: True
* Comparing options compatibility with Group Replication... PASS
Server configuration is compliant with the requirements.
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@global.transaction_write_set_extraction
DEBUG: MySQL query: SELECT @@global.transaction_write_set_extraction
DEBUG: expected value: XXHASH64 found
* Comparing options compatibility with the group of the given peer-instance... PASS
Server configuration is compliant with current group configuration.
Option name                      Required Value   Current Value    Result
-------------------------------  ---------------  ---------------  -----
transaction_write_set_extraction  XXHASH64         XXHASH64         PASS 
DEBUG: Server version checking: 5.7.17
DEBUG: MySQL query: SHOW VARIABLES LIKE 'VERSION'
DEBUG: Server version: [8, 0, 11]
DEBUG: Server version check result: True
* Checking server version... PASS
Server is 8.0.11

DEBUG: checking server id uniqueness
DEBUG: MySQL query: SELECT @@server_id
DEBUG: server id = 154
DEBUG: MySQL query: SELECT variable_source FROM performance_schema.variables_info WHERE variable_name='server_id'
DEBUG: MySQL query: SELECT @@server_id
DEBUG: Verifying the peer 'mgr1:3310' ...
DEBUG: The peer 'mgr1:3310' have a different server_id  152
* Checking that server_id is unique... PASS
The server_id is valid.

DEBUG: MySQL query: SELECT @@slave_parallel_workers
* Checking compatibility of Multi-Threaded Slave settings... PASS
Multi-Threaded Slave settings are compatible with Group Replication.

DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'group_replication%'
DEBUG: Plugin group_replication has state: ACTIVE and not the expected: DISABLED
WARNING: Not running locally on the server and can not access its error log.
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
DEBUG: local_address to use: mgr2:34277
DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT @@global.group_replication_local_address
DEBUG: MySQL query: SELECT @@group_replication_single_primary_mode
DEBUG: MySQL query: SELECT @@server_id
DEBUG: Trying to retrieve group replication name from peer server.
DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status WHERE CHANNEL_NAME='group_replication_applier'
DEBUG: Retrieved group replication name from peer server: a05740e5-7842-11e8-adaf-d067e5fdda78.
Joining Group Replication group: a05740e5-7842-11e8-adaf-d067e5fdda78
DEBUG: Setting Group Replication variables
DEBUG:   group_replication_group_seeds = mgr1:49178
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_group_seeds = ?, params (u'mgr1:49178',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_single_primary_mode = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_single_primary_mode = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_group_name = a05740e5-7842-11e8-adaf-d067e5fdda78
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_group_name = ?, params ('a05740e5-7842-11e8-adaf-d067e5fdda78',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_recovery_use_ssl = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_recovery_use_ssl = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   auto_increment_offset = 2
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST auto_increment_offset = ?, params (2,)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_ssl_mode = 'REQUIRED'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_ssl_mode = 'REQUIRED'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_start_on_boot = ON
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_start_on_boot = ?, params ('ON',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_local_address = 'mgr2:34277'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_local_address = 'mgr2:34277'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   auto_increment_increment = 1
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST auto_increment_increment = ?, params (1,)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
* Running change master command
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: CHANGE MASTER TO MASTER_USER = /*(*/ 'mysql_innodb_cluster_r2433924357' /*)*/, MASTER_PASSWORD = /*(*/ '******' /*)*/ FOR CHANNEL 'group_replication_recovery';
DEBUG: MySQL query: SET SQL_LOG_BIN=1
Attempting to join to Group Replication group...
DEBUG: 
DEBUG: * Starting Group Replication plugin...
DEBUG: MySQL query: START group_replication
Server 'mgr2:3310' joined Group Replication group a05740e5-7842-11e8-adaf-d067e5fdda78.
==============================================================================
The instance 'sh_user@mgr2:3310' was successfully added to the cluster.

```

## 添加第二个节点后,集群状态

```
 MySQL  mgr1:3310 ssl  JS > cluster.status();
{
    "clusterName": "proCluster", 
    "defaultReplicaSet": {
        "name": "default", 
        "primary": "mgr1:3310", 
        "ssl": "REQUIRED", 
        "status": "OK_NO_TOLERANCE", 
        "statusText": "Cluster is NOT tolerant to any failures. 1 member is not active", 
        "topology": {
            "mgr1:3310": {
                "address": "mgr1:3310", 
                "mode": "R/W", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }, 
            "mgr2:3310": {
                "address": "mgr2:3310", 
                "mode": "R/O", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "RECOVERING"
            }
        }
    }, 
    "groupInformationSourceMember": "mysql://sh_user@mgr1:3310"
}

 MySQL  mgr1:3310 ssl  JS > cluster.status();
{
    "clusterName": "proCluster", 
    "defaultReplicaSet": {
        "name": "default", 
        "primary": "mgr1:3310", 
        "ssl": "REQUIRED", 
        "status": "OK_NO_TOLERANCE", 
        "statusText": "Cluster is NOT tolerant to any failures.", 
        "topology": {
            "mgr1:3310": {
                "address": "mgr1:3310", 
                "mode": "R/W", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }, 
            "mgr2:3310": {
                "address": "mgr2:3310", 
                "mode": "R/O", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }
        }
    }, 
    "groupInformationSourceMember": "mysql://sh_user@mgr1:3310"
}
```

## 添加第三个节点

```
 MySQL  mgr1:3310 ssl  JS > cluster.addInstance('sh_user@mgr3:3310')
A new instance will be added to the InnoDB cluster. Depending on the amount of
data on the cluster this might take from a few seconds to several hours.

Please provide the password for 'sh_user@mgr3:3310': *********
Adding instance to the cluster ...

Validating instance at mgr3:3310...

This instance reports its own address as mgr3
DBA: mysqlprovision: Executing '[{"server":{"host":"mgr3","passwd":"****","password":"****","port":3310,"scheme":"mysql","user":"sh_user"},"verbose":2}]\n.\n' | mysqlsh --log-level=8 --py -f /usr/share/mysqlsh/mysqlprovision.zip check
=========================== MySQL Provision Output ===========================

DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
Running check command.
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status where CHANNEL_NAME = 'group_replication_applier'
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
Checking Group Replication prerequisites.
DEBUG: The server: 'mgr3:3310' has been set to check
DEBUG: Option checking started: {'log_slave_updates': {'ONE OF': ('ON', '1')}, 'binlog_format': {'ONE OF': ('ROW',)}, 'relay_log_info_repository': {'ONE OF': ('TABLE',)}, 'binlog_checksum': {'ONE OF': ('NONE',)}, 'report_port': {'ONE OF': ('3310',)}, 'enforce_gtid_consistency': {'ONE OF': ('ON', '1')}, 'master_info_repository': {'ONE OF': ('TABLE',)}, 'log_bin': {'ONE OF': ('1', 'ON')}, 'gtid_mode': {'ONE OF': ('ON',)}, 'transaction_write_set_extraction': {'ONE OF': ('XXHASH64', '2', 'MURMUR32', '1')}}
DEBUG: Checking option: 'log_slave_updates' 
DEBUG: MySQL query: SELECT @@log_slave_updates
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('ON', '1')
DEBUG: Checking option: 'binlog_format' 
DEBUG: MySQL query: SELECT @@binlog_format
DEBUG: Option current value: 'ROW' 
DEBUG: OK: value ROW is one of ('ROW',)
DEBUG: Checking option: 'relay_log_info_repository' 
DEBUG: MySQL query: SELECT @@relay_log_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'binlog_checksum' 
DEBUG: MySQL query: SELECT @@binlog_checksum
DEBUG: Option current value: 'NONE' 
DEBUG: OK: value NONE is one of ('NONE',)
DEBUG: Checking option: 'report_port' 
DEBUG: MySQL query: SELECT @@report_port
DEBUG: Option current value: '3310' 
DEBUG: OK: value 3310 is one of ('3310',)
DEBUG: Checking option: 'enforce_gtid_consistency' 
DEBUG: MySQL query: SELECT @@enforce_gtid_consistency
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON', '1')
DEBUG: Checking option: 'master_info_repository' 
DEBUG: MySQL query: SELECT @@master_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'log_bin' 
DEBUG: MySQL query: SELECT @@log_bin
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('1', 'ON')
DEBUG: Checking option: 'gtid_mode' 
DEBUG: MySQL query: SELECT @@gtid_mode
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON',)
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@transaction_write_set_extraction
DEBUG: Option current value: 'XXHASH64' 
DEBUG: OK: value XXHASH64 is one of ('XXHASH64', '2', 'MURMUR32', '1')
DEBUG: Options check result: True
* Comparing options compatibility with Group Replication... PASS
Server configuration is compliant with the requirements.
DEBUG: Server version checking: 5.7.17
DEBUG: MySQL query: SHOW VARIABLES LIKE 'VERSION'
DEBUG: Server version: [8, 0, 11]
DEBUG: Server version check result: True
* Checking server version... PASS
Server is 8.0.11

DEBUG: checking server id uniqueness
DEBUG: MySQL query: SELECT @@server_id
DEBUG: server id = 159
DEBUG: MySQL query: SELECT variable_source FROM performance_schema.variables_info WHERE variable_name='server_id'
* Checking that server_id is unique... PASS
The server_id is valid.

DEBUG: MySQL query: SELECT @@slave_parallel_workers
* Checking compatibility of Multi-Threaded Slave settings... PASS
Multi-Threaded Slave settings are compatible with Group Replication.

DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'group_replication%'
DEBUG: Plugin group_replication has state: ACTIVE and not the expected: DISABLED
==============================================================================

Instance configuration is suitable.
DBA: mysqlprovision: Executing '[{"group_seeds":"mgr1:49178,mgr2:34277","rep_user_passwd":"****","replication_user":"mysql_innodb_cluster_r2433951064","ssl_mode":"REQUIRED","verbose":2},{"host":"mgr3","passwd":"****","password":"****","port":3310,"user":"sh_user"},{"host":"mgr1","passwd":"****","port":3310,"user":"sh_user"}]\n.\n' | mysqlsh --log-level=8 --py -f /usr/share/mysqlsh/mysqlprovision.zip join-replicaset
=========================== MySQL Provision Output ===========================
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'

Running join command on 'mgr3:3310'.
Checking Group Replication prerequisites.
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status where CHANNEL_NAME = 'group_replication_applier'
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
DEBUG: MySQL query: SELECT @@have_ssl
DEBUG: MySQL query: SELECT @@group_replication_recovery_use_ssl
DEBUG: MySQL query: SELECT @@group_replication_ssl_mode
DEBUG: ->parse_server_address 
  host: % 
  address_type: host like
DEBUG: Using replication_user: mysql_innodb_cluster_r2433951064@'%'
DEBUG: ->rpl_user_dict {'replication_user': "mysql_innodb_cluster_r2433951064@'%'", 'rep_user_passwd': '******', 'host': '%', 'recovery_user': 'mysql_innodb_cluster_r2433951064', 'ssl_mode': u'REQUIRED'}
DEBUG: MySQL query: select MEMBER_HOST, MEMBER_PORT from performance_schema.replication_group_members
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
DEBUG: MySQL query: SHOW VARIABLES LIKE 'READ_ONLY'
DEBUG: The server: 'mgr3:3310' has been set to check
DEBUG: Option checking started: {'log_slave_updates': {'ONE OF': ('ON', '1')}, 'binlog_format': {'ONE OF': ('ROW',)}, 'relay_log_info_repository': {'ONE OF': ('TABLE',)}, 'binlog_checksum': {'ONE OF': ('NONE',)}, 'report_port': {'ONE OF': ('3310',)}, 'enforce_gtid_consistency': {'ONE OF': ('ON', '1')}, 'master_info_repository': {'ONE OF': ('TABLE',)}, 'log_bin': {'ONE OF': ('1', 'ON')}, 'gtid_mode': {'ONE OF': ('ON',)}, 'transaction_write_set_extraction': {'ONE OF': ('XXHASH64', '2', 'MURMUR32', '1')}}
DEBUG: Checking option: 'log_slave_updates' 
DEBUG: MySQL query: SELECT @@log_slave_updates
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('ON', '1')
DEBUG: Checking option: 'binlog_format' 
DEBUG: MySQL query: SELECT @@binlog_format
DEBUG: Option current value: 'ROW' 
DEBUG: OK: value ROW is one of ('ROW',)
DEBUG: Checking option: 'relay_log_info_repository' 
DEBUG: MySQL query: SELECT @@relay_log_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'binlog_checksum' 
DEBUG: MySQL query: SELECT @@binlog_checksum
DEBUG: Option current value: 'NONE' 
DEBUG: OK: value NONE is one of ('NONE',)
DEBUG: Checking option: 'report_port' 
DEBUG: MySQL query: SELECT @@report_port
DEBUG: Option current value: '3310' 
DEBUG: OK: value 3310 is one of ('3310',)
DEBUG: Checking option: 'enforce_gtid_consistency' 
DEBUG: MySQL query: SELECT @@enforce_gtid_consistency
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON', '1')
DEBUG: Checking option: 'master_info_repository' 
DEBUG: MySQL query: SELECT @@master_info_repository
DEBUG: Option current value: 'TABLE' 
DEBUG: OK: value TABLE is one of ('TABLE',)
DEBUG: Checking option: 'log_bin' 
DEBUG: MySQL query: SELECT @@log_bin
DEBUG: Option current value: '1' 
DEBUG: OK: value 1 is one of ('1', 'ON')
DEBUG: Checking option: 'gtid_mode' 
DEBUG: MySQL query: SELECT @@gtid_mode
DEBUG: Option current value: 'ON' 
DEBUG: OK: value ON is one of ('ON',)
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@transaction_write_set_extraction
DEBUG: Option current value: 'XXHASH64' 
DEBUG: OK: value XXHASH64 is one of ('XXHASH64', '2', 'MURMUR32', '1')
DEBUG: Options check result: True
* Comparing options compatibility with Group Replication... PASS
Server configuration is compliant with the requirements.
DEBUG: Checking option: 'transaction_write_set_extraction' 
DEBUG: MySQL query: SELECT @@global.transaction_write_set_extraction
DEBUG: MySQL query: SELECT @@global.transaction_write_set_extraction
DEBUG: expected value: XXHASH64 found
* Comparing options compatibility with the group of the given peer-instance... PASS
Server configuration is compliant with current group configuration.
Option name                      Required Value   Current Value    Result
-------------------------------  ---------------  ---------------  -----
transaction_write_set_extraction  XXHASH64         XXHASH64         PASS 
DEBUG: Server version checking: 5.7.17
DEBUG: MySQL query: SHOW VARIABLES LIKE 'VERSION'
DEBUG: Server version: [8, 0, 11]
DEBUG: Server version check result: True
* Checking server version... PASS
Server is 8.0.11

DEBUG: checking server id uniqueness
DEBUG: MySQL query: SELECT @@server_id
DEBUG: server id = 159
DEBUG: MySQL query: SELECT variable_source FROM performance_schema.variables_info WHERE variable_name='server_id'
DEBUG: MySQL query: SELECT @@server_id
DEBUG: Verifying the peer 'mgr1:3310' ...
DEBUG: The peer 'mgr1:3310' have a different server_id  152
DEBUG: MySQL query: SELECT @@server_id
DEBUG: Verifying the peer 'mgr2:3310' ...
DEBUG: The peer 'mgr2:3310' have a different server_id  154
* Checking that server_id is unique... PASS
The server_id is valid.

DEBUG: MySQL query: SELECT @@slave_parallel_workers
* Checking compatibility of Multi-Threaded Slave settings... PASS
Multi-Threaded Slave settings are compatible with Group Replication.

DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'group_replication%'
DEBUG: Plugin group_replication has state: ACTIVE and not the expected: DISABLED
WARNING: Not running locally on the server and can not access its error log.
DEBUG: MySQL query: SELECT MEMBER_STATE FROM performance_schema.replication_group_members as m JOIN performance_schema.replication_group_member_stats as s on m.MEMBER_ID = s.MEMBER_ID AND m.MEMBER_ID = @@server_uuid
DEBUG: local_address to use: mgr3:45353
DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT @@global.group_replication_local_address
DEBUG: MySQL query: SELECT @@group_replication_single_primary_mode
DEBUG: MySQL query: SELECT @@server_id
DEBUG: Trying to retrieve group replication name from peer server.
DEBUG: MySQL query: show plugins
DEBUG: MySQL query: SELECT GROUP_NAME FROM performance_schema.replication_connection_status WHERE CHANNEL_NAME='group_replication_applier'
DEBUG: Retrieved group replication name from peer server: a05740e5-7842-11e8-adaf-d067e5fdda78.
Joining Group Replication group: a05740e5-7842-11e8-adaf-d067e5fdda78
DEBUG: Setting Group Replication variables
DEBUG:   group_replication_group_seeds = mgr1:49178,mgr2:34277
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_group_seeds = ?, params (u'mgr1:49178,mgr2:34277',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_single_primary_mode = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_single_primary_mode = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_group_name = a05740e5-7842-11e8-adaf-d067e5fdda78
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_group_name = ?, params ('a05740e5-7842-11e8-adaf-d067e5fdda78',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_recovery_use_ssl = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_recovery_use_ssl = 'ON'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   auto_increment_offset = 2
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST auto_increment_offset = ?, params (2,)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_ssl_mode = 'REQUIRED'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_ssl_mode = 'REQUIRED'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_start_on_boot = ON
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_start_on_boot = ?, params ('ON',)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   group_replication_local_address = 'mgr3:45353'
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST group_replication_local_address = 'mgr3:45353'
DEBUG: MySQL query: SET SQL_LOG_BIN=1
DEBUG:   auto_increment_increment = 1
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: SET PERSIST auto_increment_increment = ?, params (1,)
DEBUG: MySQL query: SET SQL_LOG_BIN=1
* Running change master command
DEBUG: MySQL query: SET SQL_LOG_BIN=0
DEBUG: MySQL query: CHANGE MASTER TO MASTER_USER = /*(*/ 'mysql_innodb_cluster_r2433951064' /*)*/, MASTER_PASSWORD = /*(*/ '******' /*)*/ FOR CHANNEL 'group_replication_recovery';
DEBUG: MySQL query: SET SQL_LOG_BIN=1
Attempting to join to Group Replication group...
DEBUG: 
DEBUG: * Starting Group Replication plugin...
DEBUG: MySQL query: START group_replication
Server 'mgr3:3310' joined Group Replication group a05740e5-7842-11e8-adaf-d067e5fdda78.
==============================================================================
The instance 'sh_user@mgr3:3310' was successfully added to the cluster.
```

## 添加第三个节点后集群状态

```
 MySQL  mgr1:3310 ssl  JS > cluster.status();
{
    "clusterName": "proCluster", 
    "defaultReplicaSet": {
        "name": "default", 
        "primary": "mgr1:3310", 
        "ssl": "REQUIRED", 
        "status": "OK", 
        "statusText": "Cluster is ONLINE and can tolerate up to ONE failure.", 
        "topology": {
            "mgr1:3310": {
                "address": "mgr1:3310", 
                "mode": "R/W", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }, 
            "mgr2:3310": {
                "address": "mgr2:3310", 
                "mode": "R/O", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }, 
            "mgr3:3310": {
                "address": "mgr3:3310", 
                "mode": "R/O", 
                "readReplicas": {}, 
                "role": "HA", 
                "status": "ONLINE"
            }
        }
    }, 
    "groupInformationSourceMember": "mysql://sh_user@mgr1:3310"
}
```

### 参考资料

[https://dev.mysql.com/doc/refman/8.0/en/mysql-innodb-cluster-production-deployment.html#create-cluster](https://dev.mysql.com/doc/refman/8.0/en/mysql-innodb-cluster-production-deployment.html#create-cluster)

[http://www.actionsky.com/%E4%BB%8E%E9%9B%B6%E6%90%AD%E5%BB%BAmysql-innodb-cluster/](http://www.actionsky.com/%E4%BB%8E%E9%9B%B6%E6%90%AD%E5%BB%BAmysql-innodb-cluster/)