# mydumper

# 下载

```
https://launchpad.net/mydumper/+download
wget https://launchpadlibrarian.net/225370879/mydumper-0.9.1.tar.gz
```

# 安装

```
yum install glib2-devel mysql-devel zlib-devel pcre-devel openssl-devel cmake gcc gcc-c++ -y

tar zxf mydumper-0.9.1.tar.gz 

cd mydumper-0.9.1

cmake .
make -j 12
make install
```

```
[root@mgr4 ~]# mydumper --version
mydumper 0.9.1, built against MySQL 5.5.60-MariaDB
[root@mgr4 ~]# myloader --version
myloader 0.9.1, built against MySQL 5.5.60-MariaDB
```

# 参数解释

### mydumper


```shell
Usage:
  mydumper [OPTION...] multi-threaded MySQL dumping

Help Options:
  -?, --help                  Show help options

Application Options:
  -B, --database              Database to dump
  -T, --tables-list           Comma delimited table list to dump (does not exclude regex option)
  -O, --omit-from-file        File containing a list of database.table entries to skip, one per line (skips before applying regex option)
  -o, --outputdir             Directory to output files to
  -s, --statement-size        Attempted size of INSERT statement in bytes, default 1000000
  -r, --rows                  Try to split tables into chunks of this many rows. This option turns off --chunk-filesize
  -F, --chunk-filesize        Split tables into chunks of this output file size. This value is in MB
  -c, --compress              Compress output files
  -e, --build-empty-files     Build dump files even if no data available from table
  -x, --regex                 Regular expression for 'db.table' matching
  -i, --ignore-engines        Comma delimited list of storage engines to ignore
  -N, --insert-ignore         Dump rows with INSERT IGNORE
  -m, --no-schemas            Do not dump table schemas with the data
  -d, --no-data               Do not dump table data
  -G, --triggers              Dump triggers
  -E, --events                Dump events
  -R, --routines              Dump stored procedures and functions
  -W, --no-views              Do not dump VIEWs
  -k, --no-locks              Do not execute the temporary shared read lock.  WARNING: This will cause inconsistent backups
  --no-backup-locks           Do not use Percona backup locks
  --less-locking              Minimize locking time on InnoDB tables.
  -l, --long-query-guard      Set long query timer in seconds, default 60
  -K, --kill-long-queries     Kill long running queries (instead of aborting)
  -D, --daemon                Enable daemon mode
  -I, --snapshot-interval     Interval between each dump snapshot (in minutes), requires --daemon, default 60
  -L, --logfile               Log file name to use, by default stdout is used
  --tz-utc                    SET TIME_ZONE='+00:00' at top of dump to allow dumping of TIMESTAMP data when a server has data in different time zones or data is being moved between servers with different time zones, defaults to on use --skip-tz-utc to disable.
  --skip-tz-utc               
  --use-savepoints            Use savepoints to reduce metadata locking issues, needs SUPER privilege
  --success-on-1146           Not increment error count and Warning instead of Critical in case of table doesn't exist
  --lock-all-tables           Use LOCK TABLE for all, instead of FTWRL
  -U, --updated-since         Use Update_time to dump only tables updated in the last U days
  --trx-consistency-only      Transactional consistency only
  --complete-insert           Use complete INSERT statements that include column names
  -h, --host                  The host to connect to
  -u, --user                  Username with the necessary privileges
  -p, --password              User password
  -a, --ask-password          Prompt For User password
  -P, --port                  TCP/IP port to connect to
  -S, --socket                UNIX domain socket file to use for connection
  -t, --threads               Number of threads to use, default 4
  -C, --compress-protocol     Use compression on the MySQL connection
  -V, --version               Show the program version and exit
  -v, --verbose               Verbosity of output, 0 = silent, 1 = errors, 2 = warnings, 3 = info, default 2
  --defaults-file             Use a specific defaults file
  --ssl                       Connect using SSL
  --key                       The path name to the key file
  --cert                      The path name to the certificate file
  --ca                        The path name to the certificate authority file
  --capath                    The path name to a directory that contains trusted SSL CA certificates in PEM format
  --cipher                    A list of permissible ciphers to use for SSL encryption
```

```
--database 指定需要备份的库

--tables-list 指定需要备份的表，用，分隔（与regex option冲突时，以regex为准）

--regex '^(?!(mysql|test))'：数据库过滤选项

--outputdir=/backupdir：备份文件输出路径

--compress：压缩方式输出文件（.gz后缀）

--verbose=3：输出日志级别info，便于观察备份情况（0 = silent, 1 = errors, 2 = warnings, 3 = info, default 2）

--logfile=/backupdir/mydumper.log：指定mydumper运行日志文件的位置

--threads 指定备份时使用的线程数，默认为4

--statement-size：限制sql语句的最大长度（mydumper在备份时会合并sql）
--rows ： 按行数分割表。提高myloader时的并发性能
--chunk-filesize ： 按输出文件的大小分割表数据。提高myloader时的并发性能
--no-locks ： 不锁表（可能数据不一致）
--binlogs ： 备份binlog。当备份失败时，可以查看备份的binlog，在备份时位置点附近寻找出错原因


```

### myloader

```shell
[root@artron_local_152 ~]# myloader --help
Usage:
  myloader [OPTION...] multi-threaded MySQL loader

Help Options:
  -?, --help                        Show help options

Application Options:
  -d, --directory                   Directory of the dump to import
  -q, --queries-per-transaction     Number of queries per transaction, default 1000
  -o, --overwrite-tables            Drop tables if they already exist
  -B, --database                    An alternative database to restore into
  -s, --source-db                   Database to restore
  -e, --enable-binlog               Enable binary logging of the restore data
  -h, --host                        The host to connect to
  -u, --user                        Username with the necessary privileges
  -p, --password                    User password
  -a, --ask-password                Prompt For User password
  -P, --port                        TCP/IP port to connect to
  -S, --socket                      UNIX domain socket file to use for connection
  -t, --threads                     Number of threads to use, default 4
  -C, --compress-protocol           Use compression on the MySQL connection
  -V, --version                     Show the program version and exit
  -v, --verbose                     Verbosity of output, 0 = silent, 1 = errors, 2 = warnings, 3 = info, default 2
  --defaults-file                   Use a specific defaults file
```


```
--directory 备份文件位置

--queries-per-transaction 每个事务执行的sql数，默认为1000

--overwrite-tables 已存在的表先drop掉再恢复（要求备份文件时候要备份表结构）

--database 指定需要还原的数据库

--enable-binlog 为还原数据的操作记录binlog

--threads 指定还原时使用的线程数，默认为4

--enable-binlog：恢复已备份的binlog

注：myloader只能在库级别层面进行恢复，单表恢复可以直接调用备份文件中对应的含有sql语句的文件

```


# 备份

* mydumper

备份test库test表
```
mydumper -t 12 -h 192.168.11.111 -u 'test' -p 'test' -P 3309 -B dbname -o /backup/db
```

备份app库，排除log表

```
mydumper --user=$user -a -S /mysql.sock -B app -x '^(?!(app.log))' -o /home/ --compress --verbose=3 --logfile=m.log 
```

备份多个数据库

```
--regex="db1.*|db2.*"
```

* 备份文件

```shell
* 库结构：dbname-schema-create.sql.gz
* 表结构：dbname.tblname1-schema.sql.gz
* 表数据：dbname.tblname1.sql.gz
（每个库、表都有自己独立的备份文件。当仅需进行单表恢复时，通过mydumper恢复单表全量数据+binlog恢复增量）
* metadata：包含备份时，binlog当前位置点
```

# 恢复  
  
* myloader
*  myloader 一般做库级别的恢复，表的恢复可以到备份文件夹中直接拿到单表数据进行恢复

```shell
myloader -h 192.168.11.100 -u test -p '123456' -P 3308 -d /backup/db -t 12 -B dbname
```

```
myloader --socket=//mysql.sock --user=$user --password=$password  -t 12 -B app -d /data/backup -v 3
```

## reference

[https://blog.csdn.net/leonpenn/article/details/82114604](https://blog.csdn.net/leonpenn/article/details/82114604)