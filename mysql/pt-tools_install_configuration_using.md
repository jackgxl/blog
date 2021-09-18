# pt-tools 安装配置 使用
---
## 安装配置
### 下载pt-tools 安装包

```
wget percona.com/get/percona-toolkit.tar.gz

```
### 解决环境依赖

```
yum install perl perl-devel perl-Time-HiRes perl-DBI perl-DBD-MySQL perl-Digest-MD5

```
### 解压安装

```
cd percona-toolkit-2.2.20/
perl Makefile.PL
make
make test
make install

```
### 验证安装

```
pt-table-checksum --version
返回版本信息 即表明安装正确

```
## pt-tools 使用说明

### pt-table-checksum

参数须知

```
--replicate-check：执行完 checksum 查询在percona.checksums表中，不一定马上查看结果呀 —— yes则马上比较chunk的crc32值并输出DIFFS列，否则不输出。默认yes，如果指定为--noreplicate-check，一般后续使用下面的--replicate-check-only去输出DIFF结果。

--replicate-check-only：不在主从库做 checksum 查询，只在原有 percona.checksums 表中查询结果，并输出数据不一致的信息。周期性的检测一致性时可能用到。

--nocheck-binlog-format：不检测日志格式。这个选项对于 ROW 模式的复制很重要，因为pt-table-checksum会在 Master和Slave 上设置binlog_format=STATEMENT（确保从库也会执行 checksum SQL），MySQL限制从库是无法设置的，所以假如行复制从库，再作为主库复制出新从库时（A->B->C），B的checksums数据将无法传输。（没验证）

--replicate= 指定 checksum 计算结果存到哪个库表里，如果没有指定，默认是 percona.checksums 。

#-h -u -p -P -S -d 连接信息

--nocheck-replication-filters 检测中忽略mysql 配置参数binlog_ignore_db等。
--nocheck-binlog-format 不检测日志格式
--replicate 指定checksum 存储的db和表， 如test.checksum
 --chunk-size， --chunk-size-limit 用于指定检测块的大小。 可控性更强
 --ignore-databases/tables/column 跳出指定元素的过滤
--lock-wait-timeout innodb 锁的超时设定， 默认为1
--max-load 设置最大并发连接数
--replicate-check-only 只输出数据不一致的信息。
--help 有这个就行了， 以及其他的详见文档。

```


#### 主库操作 所有从库全部更新（适合一主一从）

```
检查d1库t1下表的数据 主从是否一致
/usr/local/bin/pt-table-checksum --nocheck-binlog-format --nocheck-replication-filters --replicate=gao.checksums  --set-vars innodb_lock_wait_timeout=50  --databases=gao --tables=t1 --host=localhost --port=3306 --user=root --password=213456 -S /data/mysql5172_3306/tmp/mysql.sock

不一致结果
            TS ERRORS  DIFFS     ROWS  CHUNKS SKIPPED    TIME TABLE
03-08T15:48:50      0      1       85       1       0   0.274 d1.t1

一致的结果
            TS ERRORS  DIFFS     ROWS  CHUNKS SKIPPED    TIME TABLE
03-08T15:55:02      0      0   859733     122       0 129.391 d1.t1

查看检查不一致的结果
select db, tbl, sum(this_cnt) as total_rows, count(*) as chunks from checksums where ( master_cnt <> this_cnt OR master_crc <> this_crc OR isnull(master_crc) <> isnull(this_crc) ) group by db, tbl; 

+-----+-----+------------+--------+
| db  | tbl | total_rows | chunks |
+-----+-----+------------+--------+
| gao | t1  |         50 |      1 |
+-----+-----+------------+--------+

```
#### 一主多从 检查单个从库数据一致性 从库操作

* 主库创建用户：

    ```
    GRANT SELECT,LOCK TABLES,PROCESS,SUPER on *.* to pt_user@'192.168.%';
    
    ```
    
* 从库创建用户：

    ```
    GRANT ALL PRIVILEGEES on percona.* to pt_user@'%' IDENTIFIED BY 'pt_pass';

    GRANT SELECT,LOCK TABLES,PROCESS,SUPER on *.* to pt_user@'%';

    ```

*  <b style="color: red;">从库</b>创建数据校验信息表，从库路由表dsns：

    ```shell
    use percona;

    CREATE TABLE `dsns` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `parent_id` int(11) DEFAULT NULL,  `dsn` varchar(255) NOT NULL,  PRIMARY KEY (`id`));

    插入从库信息：

    insert into dsns(id,parent_id,dsn) values(1,null,'h=192.168.1.159,P=3306,u=pt_user,p=pt_pass');

    ```

* 校验数据 在<b style="color: red;">从库</b>上执行

    ```
    pt-table-checksum --replicate=oa_gallery.checksums --nocheck-replication-filters --no-check-binlog-format --set-vars innodb_lock_wait_timeout=50 h=192.168.1.152,u=pt_user,p='pt_pass',P=3306 --databases=v71 --tables=t1 --recursion-method dsn=h=192.168.1.159,u=pt_user,p='pt_pass',P=3306,D=percona,t=dsns

    ```

* 同步数据

    ```
    先查看不一致的数据：
    pt-table-sync --charset=utf8 --replicate=percona.checksums h=192.168.1.152,u=pt_user,p=pt_pass h=192.168.1.159,u=pt_user,p=pt_pass  --print
    
    同步不一致的数据：
    pt-table-sync --charset=utf8 --replicate=percona.checksums h=192.168.1.152,u=pt_user,p=pt_pass h=192.168.1.159,u=pt_user,p=pt_pass  --execute
    
    ```


### pt-table-sync

```
修复数据不一致的表
pt-table-sync --replicate=gao.checksums --charset=utf8 h=192.168.1.152,u=pt_user,p=pt_pass  h=192.168.1.159,u=pt_user,p=pt_pass --execute --print

```

## tips

pt-table-check pt-table-sync 从3.0.5版本开始支持 mysql channel 模式复制，示例如下：

```
pt-table-checksum  --nocheck-replication-filters --no-check-binlog-format --channel=artron_60 --replicate=test_ajl.checksums  --host=192.168.1.6 --user=gao --password='$passwd' --port=3306 --set-vars innodb_lock_wait_timeout=5 --databases=${i}  --recursion-method dsn=h=192.168.1.2,u=gao,p=123456,P=3306,D=test,t=dsns
```


```
pt-table-sync --channel=channel_name --replicate=test_ajl.checksums  --sync-to-master --charset=utf8   --database=db_name  h=192.168.1.2,u=gao,p=123456,P=3306   --print 
先查看，再执行
--execute 
```


## reference

[https://blog.csdn.net/melody_mr/article/details/45224249](https://blog.csdn.net/melody_mr/article/details/45224249)

[https://www.cnblogs.com/erisen/p/5971420.html](https://www.cnblogs.com/erisen/p/5971420.html)