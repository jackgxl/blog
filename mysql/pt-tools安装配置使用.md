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
## tp-tools 使用说明
### pt-table-checksum
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
###pt-table-sync
```
修复数据不一致的表
pt-table-sync --replicate=gao.checksums h=192.168.64.152,u=root,p=213456 h=192.168.64.159,u=root,p=213456 --execute --print
```

