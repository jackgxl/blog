# MariaDB\_Spider\_Installation\_Using

[TOC]

# Installation

* 下载MariaDB

```shell
wget https://downloads.mariadb.com/MariaDB/mariadb-10.3.10/mariadb-10.3.10-linux-glibc_214-x86_64.tar.gz
```

* 解压安装包安装spider插件

```shell
tar zxf mariadb-10.3.10-linux-x86_64.tar.gz -C /usr/local
cd /usr/local
ln -sv mariadb-10.3.10-linux-x86_64 mysql
mkdir -pv /data/mysqldata/
配置my.cnf
cd /usr/local/mysql
./scripts/mysql_install_db --defaults-file=/path/to/my.cnf --user=mysql
./bin/mysqld_safe --defaults-file=/path/to/my.cnf --user=mysql &
cd /usr/local/mysql/share
MariaDB [(none)]> source ./install_spider.sql
```
```
Spider 插件安装验证

MariaDB [mysql]> show tables like '%spider%';
+------------------------------------+
| Tables_in_mysql (%spider%)         |
+------------------------------------+
| spider_link_failed_log             |
| spider_link_mon_servers            |
| spider_table_crd                   |
| spider_table_position_for_recovery |
| spider_table_sts                   |
| spider_tables                      |
| spider_xa                          |
| spider_xa_failed_log               |
| spider_xa_member                   |
+------------------------------------+
9 rows in set (0.001 sec)

MariaDB [mysql]> show plugins;
+-------------------------------+----------+--------------------+--------------+---------+
| Name                          | Status   | Type               | Library      | License |
+-------------------------------+----------+--------------------+--------------+---------+
| binlog                        | ACTIVE   | STORAGE ENGINE     | NULL         | GPL     |
| mysql_native_password         | ACTIVE   | AUTHENTICATION     | NULL         | GPL     |
| mysql_old_password            | ACTIVE   | AUTHENTICATION     | NULL         | GPL     |
...
| SPIDER                        | ACTIVE   | STORAGE ENGINE     | ha_spider.so | GPL     |
| SPIDER_ALLOC_MEM              | ACTIVE   | INFORMATION SCHEMA | ha_spider.so | GPL     |
+-------------------------------+----------+--------------------+--------------+---------+
```

# Spider 配置
**Spider 参数**

```
MariaDB [db3]> show variables like '%spider%';

```


| Variable_name                         | Value  |参数说明|
|:-:|:-:|:-:|
| spider\_auto\_increment\_mode            | -1     | |
| spider\_bgs\_first\_read                 | -1     |
| spider\_bgs\_mode                       | -1     |
| spider\_bgs\_second\_read                | -1     |
| spider\_bka\_engine                     |        |
| spider\_bka\_mode                       | -1     |
| spider\_bka\_table\_name\_type            | -1     |
| spider\_block\_size                     | 16384  |
| spider\_bulk\_size                      | -1     |
| spider\_bulk\_update\_mode               | -1     |
| spider\_bulk\_update\_size               | -1     |
| spider\_casual\_read                    | -1     |
| spider\_conn\_recycle\_mode              | 0      |
| spider\_conn\_recycle\_strict            | 0      |
| spider\_conn\_wait\_timeout              | 10     |
| spider\_connect\_error\_interval         | 1      |
| spider\_connect\_mutex                  | OFF    |
| spider\_connect\_retry\_count            | 1000   |
| spider\_connect\_retry\_interval         | 1000   |
| spider\_connect\_timeout                | -1     |
| spider\_crd\_bg\_mode                    | -1     |
| spider\_crd\_interval                   | -1     |
| spider\_crd\_mode                       | -1     |
| spider\_crd\_sync                       | -1     |
| spider\_crd\_type                       | -1     |
| spider\_crd\_weight                     | -1     |
| spider\_delete\_all\_rows\_type           | -1     |
| spider\_direct\_dup\_insert              | -1     |
| spider\_direct\_order\_limit             | -1     |
| spider\_dry\_access                     | OFF    |
| spider\_error\_read\_mode                | -1     |
| spider\_error\_write\_mode               | -1     |
| spider\_first\_read                     | -1     |
| spider\_force\_commit                   | 1      |
| spider\_general\_log                    | OFF    |
| spider\_index\_hint\_pushdown            | OFF    |
| spider\_init\_sql\_alloc\_size            | -1     |
| spider\_internal\_limit                 | -1     |
| spider\_internal\_offset                | -1     |
| spider\_internal\_optimize              | -1     |
| spider\_internal\_optimize\_local        | -1     |
| spider\_internal\_sql\_log\_off           | -1     |
| spider\_internal\_unlock                | OFF    |
| spider\_internal\_xa                    | OFF    |
| spider\_internal\_xa\_id\_type            | 0      |
| spider\_internal\_xa\_snapshot           | 0      |
| spider\_load\_crd\_at\_startup            | -1     |
| spider\_load\_sts\_at\_startup            | -1     |
| spider\_local\_lock\_table               | OFF    |
| spider\_lock\_exchange                  | OFF    |
| spider\_log\_result\_error\_with\_sql      | 0      |
| spider\_log\_result\_errors              | 0      |
| spider\_low\_mem\_read                   | -1     |
| spider\_max\_connections                | 0      |
| spider\_max\_order                      | -1     |
| spider\_multi\_split\_read               | -1     |
| spider\_net\_read\_timeout               | -1     |
| spider\_net\_write\_timeout              | -1     |
| spider\_ping\_interval\_at\_trx\_start     | 3600   |
| spider\_quick\_mode                     | -1     |
| spider\_quick\_page\_size                | -1     |
| spider\_read\_only\_mode                 | -1     |
| spider\_remote\_access\_charset          |        |
| spider\_remote\_autocommit              | -1     |
| spider\_remote\_default\_database        |        |
| spider\_remote\_sql\_log\_off             | -1     |
| spider\_remote\_time\_zone               |        |
| spider\_remote\_trx\_isolation           | -1     |
| spider\_reset\_sql\_alloc                | -1     |
| spider\_same\_server\_link               | OFF    |
| spider\_second\_read                    | -1     |
| spider\_select\_column\_mode             | -1     |
| spider\_selupd\_lock\_mode               | -1     |
| spider\_semi\_split\_read                | -1     |
| spider\_semi\_split\_read\_limit          | -1     |
| spider\_semi\_table\_lock                | 1      |
| spider\_semi\_table\_lock\_connection     | -1     |
| spider\_semi\_trx                       | ON     |
| spider\_semi\_trx\_isolation             | -1     |
| spider\_skip\_default\_condition         | -1     |
| spider\_skip\_parallel\_search           | -1     |
| spider\_split\_read                     | -1     |
| spider\_store\_last\_crd                 | -1     |
| spider\_store\_last\_sts                 | -1     |
| spider\_sts\_bg\_mode                    | -1     |
| spider\_sts\_interval                   | -1     |
| spider\_sts\_mode                       | -1     |
| spider\_sts\_sync                       | -1     |
| spider\_support\_xa                     | ON     |
| spider\_sync\_autocommit                | ON     |
| spider\_sync\_trx\_isolation             | ON     |
| spider\_table\_crd\_thread\_count         | 10     |
| spider\_table\_init\_error\_interval      | 1      |
| spider\_table\_sts\_thread\_count         | 10     |
| spider\_udf\_ct\_bulk\_insert\_interval    | -1     |
| spider\_udf\_ct\_bulk\_insert\_rows        | -1     |
| spider\_udf\_ds\_bulk\_insert\_rows        | -1     |
| spider\_udf\_ds\_table\_loop\_mode         | -1     |
| spider\_udf\_ds\_use\_real\_table          | -1     |
| spider\_udf\_table\_lock\_mutex\_count     | 20     |
| spider\_udf\_table\_mon\_mutex\_count      | 20     |
| spider\_use\_all\_conns\_snapshot         | OFF    |
| spider\_use\_consistent\_snapshot        | OFF    |
| spider\_use\_default\_database           | ON     |
| spider\_use\_flash\_logs                 | OFF    |
| spider\_use\_handler                    | -1     |
| spider\_use\_pushdown\_udf               | -1     |
| spider\_use\_snapshot\_with\_flush\_tables | 0      |
| spider\_use\_table\_charset              | -1     |
| spider\_version                        | 3.3.13 |
| spider\_xa\_register\_mode               | 1      |


# Spider 验证
*  环境
    
    |Host|Port|DB|Role|User|Password|
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |192.168.64.101|6000|test_db|Spider|gao|gao|
    |192.168.64.157|3307|test_db|backend1|gao|gao|
    |192.168.64.182|5732|test_db|backend2|gao|gao|
    Spider 用户
    
    ```
    gao@'%' all privielges
    ```
    
*  直接创建单表

    * backend
        
        ```
        CREATE TABLE `t1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ;
        ```
    
    * spider

        ```
        CREATE TABLE `t1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=SPIDER  DEFAULT CHARSET=utf8 COMMENT='host "192.168.64.182",user "gao",password "gao",port "5723"' ;
        ```

    * 验证

        * spider
        
            ```
        MariaDB [test_db]> select * from t1;
+----+------+
| id | code |
+----+------+
|  1 | test |
+----+------+
1 row in set (0.004 sec)
MariaDB [test_db]> insert into t1 values(0,'test');
Query OK, 1 row affected (0.010 sec)
MariaDB [test_db]> insert into t1 values(0,'test');
Query OK, 1 row affected (0.004 sec)
MariaDB [test_db]> select * from t1;               
+----+------+
| id | code |
+----+------+
|  1 | test |
|  2 | test |
|  3 | test |
+----+------+
3 rows in set (0.031 sec)
            ```
        
        * backend2

            ```
            mysql(root@localhost:test_db)>select * from t1;
+----+------+
| id | code |
+----+------+
|  1 | test |
|  2 | test |
|  3 | test |
+----+------+
3 rows in set (0.00 sec)
            ```
    

*  创建spider后端DB server的配置

    * sql形式创建

        ```
        create server backend2 foreign data wrapper mysql options(host '192.168.64.182',database 'test_db',user 'gao',password 'gao',port 5723);
        验证
        MariaDB [test_db]> select * from mysql.servers where Server_name in( 'backend2');           
+-------------+----------------+---------+----------+----------+------+--------+---------+-------+
| Server_name | Host           | Db      | Username | Password | Port | Socket | Wrapper | Owner |
+-------------+----------------+---------+----------+----------+------+--------+---------+-------+
| backend2    | 192.168.64.182 | test_db | gao      | gao      | 5723 |        | mysql   |       |
+-------------+----------------+---------+----------+----------+------+--------+---------+-------+
1 row in set (0.001 sec)
        ```
        
    * 直接插入mysql.servers表，flush hosts 生效 。

        ```
    MariaDB [test_db]> insert into mysql.servers (Server_name,Host,Db,Username,Password,Port,Socket,Wrapper,Owner) values('backend1','192.168.64.157','test_db','gao','gao',3307,'','mysql','');
Query OK, 1 row affected (0.001 sec)
验证
MariaDB [test_db]> select * from mysql.servers where Server_name = 'backend1';
+-------------+----------------+---------+----------+----------+------+--------+---------+-------+
| Server_name | Host           | Db      | Username | Password | Port | Socket | Wrapper | Owner |
+-------------+----------------+---------+----------+----------+------+--------+---------+-------+
| backend1    | 192.168.64.157 | test_db | gao      | gao      | 3307 |        | mysql   |       |
+-------------+----------------+---------+----------+----------+------+--------+---------+-------+
1 row in set (0.001 sec)
        ```


# Reference

[https://mariadb.com/kb/en/library/spider-storage-engine-overview/](https://mariadb.com/kb/en/library/spider-storage-engine-overview/)

[https://www.jianshu.com/p/b96a8c90689a](https://www.jianshu.com/p/b96a8c90689a)

[https://zhuanlan.zhihu.com/p/47418626?utm_source=qq&utm_medium=social&utm_oi=72613187551232]()

[https://www.centos.bz/2017/12/mariadb-galera-cluster%E9%9B%86%E7%BE%A4%E4%BC%98%E7%BC%BA%E7%82%B9/](https://www.centos.bz/2017/12/mariadb-galera-cluster%E9%9B%86%E7%BE%A4%E4%BC%98%E7%BC%BA%E7%82%B9/)