#MySQL8.0.11 编译安装


###下载源码包

###配置编译环境
```
yum install  gcc gcc-c++ cmake  make  autoconf automake \
ncurses-devel zlib zlib-devel libxml2 libxml2-devel \
libaio.x86_64 libaio-devel.x86_64 \
readline.x86_64 readline-devel.x86_64 \
numactl numactl-devel.x86_64 numactl-libs.x86_64

useradd -M -s /sbin/nologin  mysql

mkdir -pv /data/mysql3308

cd /data/mysql3308

mkdir etc var log tmp 

cp /root/my.cnf  etc/
```
###编译安装
```
cmake \
-DCMAKE_INSTALL_PREFIX=/data/mysql3308 \
-DSYSCONFDIR=/data/mysql3308/etc    \
-DMYSQL_DATADIR=/data/mysql3308/var \
-DSYSTEMD_PID_DIR=/data/mysql3308/var/mysql.pid \
-DMYSQL_UNIX_ADDR=/data/mysql3308/tmp/mysql.sock \
-DMYSQLX_UNIX_ADDR=/data/mysql3308/tmp/mysqlx.sock \
-DTMPDIR=/data/mysql3308/tmp \
-DDEFAULT_CHARSET=utf8mb4 \
-DDEFAULT_COLLATION=utf8mb4_general_ci \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DWITH_READLINE=1 \
-DENABLED_LOCAL_INFILE=1 \
-DMYSQL_USER=mysql \
-DMYSQL_TCP_PORT=3308 \
-DMYSQLX_TCP_PORT=33080 \
-DWITH_NUMA=1 \
-DENABLE_DOWNLOADS=1 \
-DWITH_BOOST=boost/boost_1_66_0/

make 

make install
```
###初始化
```
cd /data/mysql3308
chown -R mysql:mysql .
cp support-files/mysql.server bin/
修改 mysql.server  mysqld_safe 加入 --defaults-file=/data/mysql3308/etc/my.cnf 参数
./bin/mysqld --defaults-file=etc/my.cnf --user=mysql --initialize
```

###启动实例
```
./bin/mysql.server start
```

###连接实例
```
/data/mysql3308/bin/mysql -uroot -pXXXXXXX
使用--initialize 初始化 会在error日志中产生随机密码
使用error日志初始化的随机密码登录，然后set password = 'XXXX' ;修改密码
或者使用skip_grant_tables,重启实例
alter user root@'lcoalhost' identified by 'XXXX'; 
也可以 update mysql.user set authentication_string='';不使用密码

```

##参数文件
```

[client]
port                   = 3308
socket                 = /data/mysql3308/tmp/mysql.sock
[mysqld]

###############basic setting#################
#skip-grant-tables
sql_mode = 'TRADITIONAL'
#ngram_token_size       = 1

basedir = /data/mysql3308
datadir = /data/mysql3308/var
port = 3308
mysqlx_port = 33080
server_id = 1603
socket = /data/mysql3308/tmp/mysql.sock
pid-file = /data/mysql3308/var/mysql.pid
tmpdir = /data/mysql3308/tmp
secure-file-priv = '/data/mysql3308/tmp'
 
explicit_defaults_for_timestamp = 1
auto_increment_increment = 1
auto_increment_offset = 1
#lower_case_table_names = 1 

default-time-zone        = system
character-set-server     = utf8mb4
default-storage-engine   = InnoDB

interactive_timeout = 1800
wait_timeout = 1800
max_connections          = 2000
max_allowed_packet = 64M

#####skip
#skip-name-resolve
#skip-grant-tables
#skip-external-locking
#skip-networking
skip-slave-start

thread_cache_size = 64

####log settings###############

expire_logs_days = 7

log-bin                  = mysql-bin
log-bin-index            = mysql-bin.index
relay-log                = relay-log
relay_log_index          = relay-log.index

#log-warnings             = 1
log_error_verbosity      = 3
log-error       = /data/mysql3308/log/mysql.err

slow_query_log           = 1
long-query-time          = 2
log_queries_not_using_indexes = 1
log_throttle_queries_not_using_indexes = 10
log_slow_admin_statements = 1
log_slow_slave_statements = 1
#min_examined_row_limit = 100
slow_query_log_file      = /data/mysql3308/log/slow.log

general_log              = 0
general_log_file         = /data/mysql3308/log/mysql.log
max_binlog_size          = 1G
max_relay_log_size       = 1G

#####InnoDB setting###########

innodb_page_size = 8192
default_storage_engine            = innodb
default_tmp_storage_engine       = innodb
innodb_buffer_pool_size = 4G
innodb_data_home_dir            = /data/mysql3308/var
innodb_data_file_path           = ibdata1:1G:autoextend
innodb_temp_data_file_path      = ibtmp1:12M:autoextend:max:1G
innodb_lru_scan_depth  = 2000
innodb_file_per_table = 1
innodb_write_io_threads = 8
innodb_read_io_threads = 8
innodb_purge_threads = 8
innodb_thread_concurrency = 0
innodb_flush_log_at_trx_commit = 1
innodb_log_buffer_size = 16M
innodb_log_file_size = 1G
innodb_log_files_in_group = 3
innodb_log_group_home_dir = /data/mysql3308/var
innodb_flush_neighbors = 1
innodb_print_all_deadlocks = 1
#innodb_large_prefix = 1
innodb_strict_mode = 1
innodb_sort_buffer_size = 67108864
innodb_undo_tablespaces = 3
innodb_max_dirty_pages_pct = 75
innodb_flush_method = O_DIRECT
innodb_lock_wait_timeout = 5
innodb_open_files=65535
innodb_use_native_aio   = on
innodb_buffer_pool_dump_pct = 40
innodb_page_cleaners = 4
innodb_undo_log_truncate = 1
innodb_purge_rseg_truncate_frequency = 128
binlog_gtid_simple_recovery=1
innodb_io_capacity=2000
innodb_io_capacity_max = 3000


log_timestamps=system

###replication settings###########

master_info_repository           = table
relay_log_info_repository        = table

binlog_format = row
#binlog_checksum = none
#binlog_rows_query_log_events = on
sync_binlog =1
transaction_isolation = READ-COMMITTED
log_slave_updates = on
relay_log_recovery = 1
#slave_skip_errors = ddl_exist_errors

#for gtid
gtid_mode = off
enforce_gtid_consistency = on
binlog_gtid_simple_recovery = 1


#####MyISAM setting##########
key_buffer_size =  128M
read_buffer_size = 16M
read_rnd_buffer_size = 32M
join_buffer_size = 128M
bulk_insert_buffer_size = 256M
sort_buffer_size = 32M
myisam_sort_buffer_size = 1G
myisam_max_sort_file_size = 10G
myisam_repair_threads = 8

table_open_cache = 4096


# for sysbench
#max_prepared_stmt_count = 1000000
#max_prepared_stmt_count = 16382
[mysqldump]
quick
max_allowed_packet = 256M

[mysql]
no-auto-rehash
default-character-set = utf8mb4
prompt=mysql(\\u@\\h:\\d)>

[myisamchk]
key_buffer_size = 64M 
sort_buffer_size = 16M
read_buffer_size = 64M
write_buffer_size = 64M

[mysqlhotcopy]
interactive-timeout


```