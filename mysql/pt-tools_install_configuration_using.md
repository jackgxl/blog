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

*  从库创建数据校验信息表，从库路由表dsns：

    ```
    use percona;

    CREATE TABLE `dsns` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `parent_id` int(11) DEFAULT NULL,  `dsn` varchar(255) NOT NULL,  PRIMARY KEY (`id`));

    插入从库信息：

    insert into dsns(id,parent_id,dsn) values(1,null,'h=192.168.1.159,P=3306,u=pt_user,p=pt_pass');

    ```

* 校验数据

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
    
