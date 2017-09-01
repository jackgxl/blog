# MySQL5.7.19\_Semi\_synchronous\_replication

### MySQL5.7.19 installation

**Compile installation reference**

[MySQL5.7_installation](https://github.com/jackgxl/uplearning/blob/master/mysql/mysql_multi-version_compilation_and_installation.md#mysql5717--mgr)

### MySQL_M-S 

* Do on the master
* Show master status
    
```

mysql> show master status;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000003 |    59524 |              |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

```

* Do on the slave
* Change master to

```
CHANGE MASTER TO
  MASTER_HOST='192.168.1.10',
  MASTER_USER='backup',
  MASTER_PASSWORD='backup',
  MASTER_PORT=3306,
  MASTER_LOG_FILE='mysql-bin.000003',
  MASTER_LOG_POS=59524,
  MASTER_CONNECT_RETRY=10;
  
start salve;
```
### MySQL_Semi\_synchronous\_replication

* Install plugin
    
    * Master
        
        ```
        INSTALL PLUGIN rpl_semi_sync_master SONAME 'semisync_master.so';
        ```
    
    * Slave
        
        ```
        INSTALL PLUGIN rpl_semi_sync_slave SONAME 'semisync_slave.so';
        ```
    
    * Check plugin
    
        ```
        
        mysql> show plugins;
        +----------------------------+----------+--------------------+-------------------+---------+
        | Name                       | Status   | Type               | Library           | License |
        +----------------------------+----------+--------------------+-------------------+---------+
        | rpl_semi_sync_slave        | ACTIVE   | REPLICATION        | semisync_slave.so | GPL     |
        +----------------------------+----------+--------------------+-------------------+---------+
        
       OR
        
        mysql> SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS  WHERE PLUGIN_NAME LIKE '%semi%';
        +----------------------+---------------+
        | PLUGIN_NAME          | PLUGIN_STATUS |
        +----------------------+---------------+
        | rpl_semi_sync_master | ACTIVE        |
        +----------------------+---------------+
        
        ```
        
* Start Semi\_synchronous\_replication
    
    * Master
        
        ```
        mysql> SET GLOBAL rpl_semi_sync_master_enabled = 1;
        Query OK, 0 rows affected (0.00 sec)
        ```
        
    * Slave
        
        ```
        mysql> SET GLOBAL rpl_semi_sync_slave_enabled = 1;
        Query OK, 0 rows affected (0.00 sec)
        ```
    * Restart Slave
        
        ```
        mysql> show variables like '%semi%';
        +---------------------------------+-------+
        | Variable_name                   | Value |
        +---------------------------------+-------+
        | rpl_semi_sync_slave_enabled     | ON    |
        | rpl_semi_sync_slave_trace_level | 32    |
        +---------------------------------+-------+
        ```
    * Check Semi_replication status
        
        
        * Master
        
        ```
        mysql> show variables like '%semi%';
        +-------------------------------------------+------------+
        | Variable_name                             | Value      |
        +-------------------------------------------+------------+
        | rpl_semi_sync_master_enabled              | ON         |
        | rpl_semi_sync_master_timeout              | 10000      |
        | rpl_semi_sync_master_trace_level          | 32         |
        | rpl_semi_sync_master_wait_for_slave_count | 1          |
        | rpl_semi_sync_master_wait_no_slave        | ON         |
        | rpl_semi_sync_master_wait_point           | AFTER_SYNC |
        +-------------------------------------------+------------+
        6 rows in set (0.01 sec)
        
        ```
        
        ```
        
        2017-09-01T06:49:52.046233Z 1633 [Note] Start binlog_dump to master_thread_id(1633) slave_server(1593309), pos(mysql-bin.000003, 59524)
        2017-09-01T08:27:10.657347Z 1620 [Note] Semi-sync replication initialized for transactions.
        2017-09-01T08:27:10.657421Z 1620 [Note] Semi-sync replication enabled on the master.    
        2017-09-01T08:27:10.657752Z 0 [Note] Starting ack receiver thread
        2017-09-01T08:29:17.822324Z 1642 [Note] While initializing dump thread for slave with UUID <954acfee-8d64-11e7-a242-14feb5c77bf3>, found a zombie dump thread with the same UUID. Master is killing the zombie dump thread(1633).
        2017-09-01T08:29:17.822466Z 1642 [Note] Start binlog_dump to master_thread_id(1642) slave_server(1593309), pos(mysql-bin.000003, 59524)
        2017-09-01T08:29:17.822518Z 1633 [Note] Stop asynchronous binlog_dump to slave (server_id: 1593309)
        2017-09-01T08:29:17.822524Z 1642 [Note] Start semi-sync binlog_dump to slave (server_id: 1593309), pos(mysql-bin.000003, 59524)

        ```
        * Slave
            
        ```
        mysql> show variables like '%semi%';
        +---------------------------------+-------+
        | Variable_name                   | Value |
        +---------------------------------+-------+
        | rpl_semi_sync_slave_enabled     | ON    |
        | rpl_semi_sync_slave_trace_level | 32    |
        +---------------------------------+-------+
        2 rows in set (0.00 sec)    
        ```
        ```
        2017-09-01T08:29:17.811669Z 9 [Note] Slave I/O thread: Start semi-sync replication to master 'backup@192.168.64.152:3309' in log 'mysql-bin.000003' at position 59524
        ```

### Tips

Add parameters to the configuration file

Master：

```
plugin-load=rpl_semi_sync_master=semisync_master.so
rpl_semi_sync_master_enabled=1

```
Slave：

```
plugin-load=rpl_semi_sync_slave=semisync_slave.so
rpl_semi_sync_slave_enabled=1
```

For High availability architecture to change slave to master

```
plugin-load = "rpl_semi_sync_master=semisync_master.so;rpl_semi_sync_slave=semisync_slave.so"
rpl-semi-sync-master-enabled = 1
rpl-semi-sync-slave-enabled = 1

```
