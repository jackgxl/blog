# MySQL8.0.11 MGR configured

## 配置环境

* 数据库软硬件配置

| hostname| ip      |system|MySQL         |
| :-----: | :------:|:-------:|:---------:|
|mgr1|192.168.64.152|CentOS7.3|MySQL8.0.11|
|mgr2|192.168.64.154|CentOS7.3|MySQL8.0.11|
|mgr3|192.168.64.159|CentOS7.3|MySQL8.0.11|

* 修改hosts文件
  
修改mgr1,mgr2,mgr3服务器hosts文件

``` shell
[root@mgr1 ~]# cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.64.152  mgr1
192.168.64.154  mgr2
192.168.64.159  mgr3
```

## MGR 限制

* Storage engine : InnoDB
* binlog-checksum=NONE
* transaction_isolation=READ-COMMITTED(官方建议)
* Split Large Transactions(拆分大事务)

## MGR配置步骤
* 配置文件

``` shell
server_id=1
gtid_mode=ON
enforce_gtid_consistency=ON
binlog_checksum=NONE
log_bin=binlog
log_slave_updates=ON
binlog_format=ROW
master_info_repository=TABLE
relay_log_info_repository=TABLE

transaction_write_set_extraction=XXHASH64
loose-group_replication_group_name="aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
loose-group_replication_start_on_boot=off
loose-group_replication_local_address= "192.168.64.152:33102"
loose-group_replication_group_seeds= "192.168.64.152:33102,192.168.64.154:33102,192.168.64.159:33102"
loose-group_replication_bootstrap_group=off
```

* 创建复制账号：

``` sql
set sql_log_bin=0;
create user rep@'192.168.64.%' identified by 'rep';
grant replication slave on *.* to rep@'192.168.64.%';
flush privileges;
set sql_log_bin=1;

CHANGE MASTER TO MASTER_USER='rep', MASTER_PASSWORD='rep' FOR CHANNEL 'group_replication_recovery';
```

* 安装组复制插件

``` sql
INSTALL PLUGIN group_replication SONAME 'group_replication.so';
show plugins;
```

* 单主启动

``` sql
SET GLOBAL group_replication_bootstrap_group=ON;
START GROUP_REPLICATION;
SET GLOBAL group_replication_bootstrap_group=OFF;
```

* 添加新复制实例

``` sql
set global group_replication_allow_local_disjoint_gtids_join=ON;
START GROUP_REPLICATION;
```

* 验证集群

``` sql
mysql(root@localhost:(none))>SELECT * FROM performance_schema.replication_group_members;
+---------------------------+--------------------------------------+-------------+-------------+--------------+-------------+----------------+
| CHANNEL_NAME              | MEMBER_ID                            | MEMBER_HOST | MEMBER_PORT | MEMBER_STATE | MEMBER_ROLE | MEMBER_VERSION |
+---------------------------+--------------------------------------+-------------+-------------+--------------+-------------+----------------+
| group_replication_applier | 1b973100-6d18-11e8-a061-14feb5c77bf3 | mgr3        |        3310 | ONLINE       | SECONDARY   | 8.0.11         |
| group_replication_applier | 3ff6350a-6af5-11e8-8727-d067e5fdda78 | mgr1        |        3310 | ONLINE       | PRIMARY     | 8.0.11         |
| group_replication_applier | e24625e6-6d40-11e8-96c2-14feb5c77923 | mgr2        |        3310 | ONLINE       | SECONDARY   | 8.0.11         |
+---------------------------+--------------------------------------+-------------+-------------+--------------+-------------+----------------+
3 rows in set (0.00 sec)
```

* 多主启动
    
    * 配置文件
        
        ```
        loose-group_replication_single_primary_mode=FALSE
        loose-group_replication_enforce_update_everywhere_checks= TRUE
        ```   
    
    
    * 启动第一个节点
    
        ```
        SET GLOBAL group_replication_bootstrap_group = ON;
              
        START GROUP_REPLICATION;
        
        SET GLOBAL group_replication_bootstrap_group=OFF;
        
        SELECT * FROM performance_schema.replication_group_members;
        ```
    
    * 启动其他节点

        ```
        START GROUP_REPLICATION;
        ```    
    
    * 验证集群
    
        ```
        SELECT * FROM performance_schema.replication_group_members;
        ```

### TIPs：

[官方文档]

[参考文档]

[官方文档]:https://dev.mysql.com/doc/refman/8.0/en/group-replication.html

[参考文档]:https://blog.csdn.net/mchdba/article/details/54381854