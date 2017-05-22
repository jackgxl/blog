# mysql安装文档
```
* 说明：mysql5.1 5.5 5.6 5.7 编译安装文档 5.7.17 MGR 配置文档
* 作者：高学亮
* 邮箱：gao.xueliang@qq.com
* 时间：20170217
* 版本：1.0


```

**安装前环境配置**：

创建用户：

```
useradd -M -s /sbin/nologin  mysql 
```

配置依赖环境：

```
yum install  gcc gcc-c++ cmake  make  autoconf automake ncurses-devel zlib zlib-devel libxml2 libxml2-devel libaio.x86_64 libaio-devel.x86_64 readline.x86_64 readline-devel.x86_64
```
配置系统环境：
	
	关闭NUMA
	echo vm.swappiness = 0 >>/etc/sysctl.conf
	sysctl -p
	echo deadline> /sys/block/sda/queue/scheduler
	vim /etc/security/limits.conf 
		* soft nofile 65536
		* hard nofile 65536
		* soft nproc 65535
		* hard nproc 65535

## mysql5.1

#### 下载安装包
```
mysql5.1版本 mysql-5.1.72.tar.gz，请到官方网站下载移动到/home 并验证md5值 
```
#### 解压
```
cd /home
tar xf mysql-5.1.72.tar.gz
```
#### 创建目录
```
mkdir /data/mysql5172_3306 -p
```
#### 编译安装
```
export bpath=/data/mysql5172_3306

./configure  --prefix=${bpath} --with-unix-socket-path=${bpath}/tmp/mysql.sock \
--with-plugins=partition,csv,archive,federated,innobase,innodb_plugin,myisam,heap \
--with-charset=utf8 \
--without-docs \
--without-man \
--without-debug \
--with-readline \
--with-client-ldflags=-static 'CFLAGS=-g -O3' 'CXXFLAGS=-g -O3' \
--with-extra-charsets=all \
--enable-assembler \
--enable-local-infile \
--enable-profiling  \
--enable-thread-safe-client

make -j `cat /proc/cpuinfo |grep processor|wc -l`

make install

make 和 make install看到 Making all in win 证明成功 也可以同步执行命令make && make install
```
#### 数据文件单独存放的编译方式
```
./configure  \
--prefix=/usr/local/mysql5172 \
--localstatedir=/data/mysql5172 \
--with-unix-socket-path=/usr/local/mysql5172/tmp/mysql.sock \
--with-plugins=partition,csv,archive,federated,innobase,innodb_plugin,myisam,heap \
--with-charset=utf8 \
--without-docs \
--without-man \
--without-debug \
--with-readline \
--with-client-ldflags=-static 'CFLAGS=-g -O3' 'CXXFLAGS=-g -O3' \
--with-extra-charsets=all \
--enable-assembler \
--enable-local-infile \
--enable-profiling  \
--enable-thread-safe-client

初始化
/usr/local/mysql5172/bin/mysql_install_db --user=mysql --basedir=/usr/local/mysql5172 --datadir=/data/mysql5172
```

#### 初始化
~~~
查看make结果：
[root@localhost mysql-5.1.72]# ll /data/mysql5172_3306/
drwxr-xr-x  2 root  root  4096 Feb 14 11:38 bin
drwxr-xr-x  3 root  root    19 Feb 14 11:38 include
drwxr-xr-x  3 root  root    19 Feb 14 11:38 lib
drwxr-xr-x  2 root  root    40 Feb 14 11:38 libexec
drwxr-xr-x 10 root  root   218 Feb 14 11:38 mysql-test
drwxr-xr-x  4 root  root    34 Feb 14 11:38 share
drwxr-xr-x  5 root  root  4096 Feb 14 11:38 sql-bench
新建目录：
[root@localhost mysql5172_3306]# mkdir  /data/mysql5172_3306/{etc,var,log,tmp} -p
或者
[root@localhost mysql5172_3306]# cd /data/mysql5172_3306/
[root@localhost mysql5172_3306]# mkdir etc var log tmp

修改配置文件：
cp /usr/local/mysql5172_3306/share/mysql/my-large.cnf /data/mysql5172_3306/etc/my.cnf

vim /data/mysql5172_3306/etc/my.cnf

socket                   = /data/mysql5172_3306/tmp/mysql.sock
pid-file                 = /data/mysql5172_3306/var/mysql.pid
basedir                  = /data/mysql5172_3306/
datadir                  = /data/mysql5172_3306/var/
tmpdir                   = /data/mysql5172_3306/tmp/
slave-load-tmpdir        = /data/mysql5172_3306/tmp/ 
language                 = /data/mysql5172_3306/share/mysql/english/
character-sets-dir       = /data/mysql5172_3306/share/mysql/charsets/
log-error                = /data/mysql5172_3306/log/mysql.err
slow_query_log_file      = /data/mysql5172_3306/log/slow.log
general_log_file         = /data/mysql5172_3306/log/mysql.log
innodb_data_home_dir            = /data/mysql5172_3306/var/
innodb_log_group_home_dir       = /data/mysql5172_3306/var/
路径信息必须正确

修改文件属主:
[root@localhost mysql5172_3306]# chown -R mysql:mysql .
[root@localhost mysql5172_3306]# chown -R mysql:mysql /data/mysql5172_3306/
[root@localhost mysql5172_3306]# ll /data/mysql5172_3306/
total 0
drwxr-xr-x 2 mysql mysql 20 Feb 14 11:16 etc
drwxr-xr-x 2 mysql mysql  6 Feb 14 10:56 log
drwxr-xr-x 2 mysql mysql  6 Feb 14 10:56 tmp
drwxr-xr-x 2 mysql mysql  6 Feb 14 10:56 var

初始化数据文件：
/data/mysql5172_3306/bin/mysql_install_db --defaults-file=/data/mysql5172_3306/etc/my.cnf --user=mysql

~~~ 

#### 启动mysql：

```
cd /data/mysql5172_3306

cp share/mysql/mysql.server bin/
修改启动脚本：
vim bin/mysql.server

$bindir/mysqld_safe --defaults-file=/data/mysql5172_3306/etc/my.cnf --datadir=$datadir --pid-file=$server_pid_file $other_args >/dev/null 2>&1 &

启动mysql：
/data/mysql5172_3306/bin/msyql.server start

修改密码：
/data/mysql5172_3306/bin/msyql -u root

mysql> set password=password('123456');
mysql> flush privileges;
```
 
### mysql5.1.72 安装完毕
***
## mysql5.5

#### 下载安装包
```
mysql5.5版本 mysql-5.5.51.tar.gz，请到官方网站下载移动到/home 并验证md5值 
```
#### 解压
```
cd /home/
tar xf mysql-5.5.51.tar.gz
```
#### 创建目录
```
mkdir -p /data/mysql5551_3307
```
#### 编译安装
```
export bpath=/data/mysql5551_3307

cmake . \
-DCMAKE_INSTALL_PREFIX=${bpath}  \
-DINSTALL_MYSQLDATADIR=${bpath}/var  \
-DMYSQL_DATADIR=${bpath}/var \
-DSYSCONFDIR=${bpath}/etc    \
-DMYSQL_UNIX_ADDR=${bpath}/tmp/mysql.sock  \
-DWITH_INNOBASE_STORAGE_ENGINE=1  \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_MEMORY_STORAGE_ENGINE=1 \
-DDEFAULT_CHARSET=utf8   \
-DDEFAULT_COLLATION=utf8_general_ci  \
-DMYSQL_TCP_PORT=3307  \
-DWITH_READLINE=1 \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_EXTRA_CHARSETS=all \
-DMYSQL_USER=mysql

make -j `cat /proc/cpuinfo |grep processor|wc -l`

make install

也可以同步执行命令make && make install

```
#### 初始化
```
进入安装目录
cd /data/mysql5551_3307/
创建数据目录：
mkdir etc var log tmp
修改配置文件：
vim etc/my.cnf
修改文件属主：
chown -R mysql:mysql .
初始化数据文件：
./scripts/mysql_install_db --defaults-file=etc/my.cnf --user=mysql

```
#### 启动mysql
```
拷贝启动文件；
cp support-files/mysql.server bin/
修改启动文件：
vim bin/mysql.server
修改的语句：
$bindir/mysqld_safe --defaults-file=/data/mysql5551_3307/etc/my.cnf --datadir="$datadir" --pid-file="$mysqld_pid_f
ile_path" $other_args >/dev/null 2>&1 &
启动数据库：
./bin/mysql.server start
设置密码：
./bin/mysql -uroot
set password=password('123456');
flush privileges;
```
### mysql5.5.51 安装完毕
***

## mysql5.6
#### 下载安装包
```
mysql5.6版本 mysql-5.6.34.tar.gz，请到官方网站下载移动到/home 并验证md5值 
```
#### 解压
```
cd /home/
tar xf mysql-5.6.34.tar.gz
```
#### 创建目录
```
mkdir -p /data/mysql5634_3308
```
#### 编译安装
```
export bpath=/data/mysql5634_3308

cmake . \
-DCMAKE_INSTALL_PREFIX=${bpath}  \
-DINSTALL_MYSQLDATADIR=${bpath}/var  \
-DMYSQL_DATADIR=${bpath}/var \
-DSYSCONFDIR=${bpath}/etc    \
-DWITH_INNOBASE_STORAGE_ENGINE=1  \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DDEFAULT_CHARSET=utf8   \
-DDEFAULT_COLLATION=utf8_general_ci  \
-DMYSQL_TCP_PORT=3308  \
-DMYSQL_UNIX_ADDR=${bpath}/tmp/mysql.sock  \
-DWITH_READLINE=1 \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_EXTRA_CHARSETS=all \
-DMYSQL_USER=mysql

make -j `cat /proc/cpuinfo |grep processor|wc -l`

make install

也可以同步执行命令make && make install
```
#### 初始化
```
进入安装目录：
cd /data/mysql5634_3308

查看安装目录文件：
[root@localhost mysql5634_3308]# ll
total 44
drwxr-xr-x  2 root root  4096 Feb 15 15:01 bin
-rw-r--r--  1 root root 17987 Sep 30 19:41 COPYING
drwxr-xr-x  3 root root    18 Feb 15 15:01 data
drwxr-xr-x  2 root root    55 Feb 15 15:01 docs
drwxr-xr-x  3 root root  4096 Feb 15 15:01 include
drwxr-xr-x  3 root root   291 Feb 15 15:01 lib
drwxr-xr-x  4 root root    30 Feb 15 15:01 man
drwxr-xr-x 10 root root  4096 Feb 15 15:01 mysql-test
-rw-r--r--  1 root root  2496 Sep 30 19:41 README
drwxr-xr-x  2 root root    30 Feb 15 15:01 scripts
drwxr-xr-x 28 root root  4096 Feb 15 15:01 share
drwxr-xr-x  4 root root  4096 Feb 15 15:01 sql-bench
drwxr-xr-x  2 root root   136 Feb 15 15:01 support-files

建立配置文件、数据文件、日志文件、临时文件目录：
mkdir etc var log tmp

创建配置文件：
vim etc/my.cnf

初始化数据文件：
./scripts/mysql_install_db --defaults-file=etc/my.cnf --user=mysql

查看数据文件：
[root@localhost mysql5634_3308]# ll var/
total 1574100
-rw-rw---- 1 mysql mysql 1073741824 Feb 15 16:29 ibdata1
-rw-rw---- 1 mysql mysql  268435456 Feb 15 16:29 ib_logfile0
-rw-rw---- 1 mysql mysql  268435456 Feb 15 16:29 ib_logfile1
drwx------ 2 mysql mysql       4096 Feb 15 16:29 mysql
-rw-rw---- 1 mysql mysql      65444 Feb 15 16:29 mysql-bin.000001
-rw-rw---- 1 mysql mysql    1184568 Feb 15 16:29 mysql-bin.000002
-rw-rw---- 1 mysql mysql         38 Feb 15 16:29 mysql-bin.index
drwx------ 2 mysql mysql       4096 Feb 15 16:29 performance_schema
drwx------ 2 mysql mysql          6 Feb 15 16:29 test
```
#### 启动mysql
```
./bin/mysql.server start
设置密码：
./bin/mysql -uroot
set password=password('123456');
flush privileges;

```
### mysql5.6.34 安装完毕

## mysql5.7.17 && MGR

#### 下载安装包

```
wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-boost-5.7.17.tar.gz

```

#### 解压

```
tar xf mysql-boost-5.7.17.tar.gz
```

#### 创建目录

```
mkdir -p /data/mysql3306/
cd /data/mysql3306
mkdir log var etc tmp
```

#### 编译安装

```
cmake \
-DCMAKE_INSTALL_PREFIX=/data/mysql3306 \
-DMYSQL_UNIX_ADDR=/data/mysql3306/tmp/mysql.sock \
-DEXTRA_CHARSETS=all \
-DDEFAULT_CHARSET=utf8mb4 \
-DDEFAULT_COLLATION=utf8mb4_general_ci \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DSYSCONFDIR=/data/mysql3306/etc    \
-DWITH_READLINE=1 \
-DENABLED_LOCAL_INFILE=1 \
-DMYSQL_DATADIR=/data/mysql3306/var \
-DMYSQL_USER=mysql \
-DMYSQL_TCP_PORT=3306 \
-DENABLE_DOWNLOADS=1 \
-DWITH_BOOST=boost/boost_1_59_0/ 
```

#### 初始化

```
可以根据配置文件定制化innodb参数
初始化时在error log随机生成密码
/data/msyql3306/bin/mysqld --defaults-file=etc/my.cnf --user=mysql --initialize
初始化不生成密码
/data/msyql3306/bin/mysqld --defaults-file=etc/my.cnf --user=mysql --initialize-insecure 
```

#### 配置文件

**主库配置文件**

```
[client]
 default-character-set = utf8
 port                   = 3306
 socket                 = /data/mysql3306/tmp/mysql.sock
[mysqld]

sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER

# ngram_token_size      = 1


# These are commonly set, remove the # and set as required.
 basedir = /data/mysql3306
 datadir = /data/mysql3306/var
 port = 3306
 server_id = 1
 socket = /data/mysql3306/tmp/mysql.sock
 pid-file = /data/mysql3306/var/mysql.pid
 
 auto_increment_increment = 1
 auto_increment_offset = 1
# lower_case_table_names = 1 
 

default-time-zone        = system
character-set-server     = utf8
default-storage-engine   = InnoDB

log-bin                  = mysql-bin
log-bin-index            = mysql-bin.index
relay-log                = relay-log
relay_log_index          = relay-log.index

log-warnings             = 1
log-error       = /data/mysql3306/log/mysql.err

slow_query_log           = 2
long-query-time          = 1
slow_query_log_file      = /data/mysql3306/log/slow.log

general_log              = 0
general_log_file         = /data/mysql3306/log/mysql.log
max_binlog_size          = 1G
max_relay_log_size       = 1G

max_connections          = 2000
#####InnoDB setting###########

default_storage_engine          = innodb
default_tmp_storage_engine      = innodb
innodb_buffer_pool_size = 4G
innodb_data_home_dir            = /data/mysql3306/var/
innodb_data_file_path           = ibdata1:1G:autoextend
innodb_temp_data_file_path      = ibtmp1:512M:autoextend
innodb_file_per_table = 1
innodb_write_io_threads = 8
innodb_read_io_threads = 8
innodb_thread_concurrency = 0
innodb_flush_log_at_trx_commit = 1
innodb_log_buffer_size = 16M
innodb_log_file_size = 256M
innodb_log_files_in_group = 3
innodb_log_group_home_dir = /data/mysql3306/var/
innodb_max_dirty_pages_pct = 75
innodb_flush_method=O_DIRECT
innodb_lock_wait_timeout = 30
innodb_open_files=65535
innodb_use_native_aio   = on


#####skip
#skip-name-resolve
skip-external-locking
#skip-networking
query_cache_size = 0
query_cache_type = 0

###for group replication~~~~~

binlog_format = row
binlog_checksum = none
binlog_rows_query_log_events = on
sync_binlog =1
transaction_isolation = READ-COMMITTED
log_slave_updates = on
expire_logs_days = 7

#for gtid
gtid_mode = on
enforce_gtid_consistency = on

# for replication

master_info_repository           = table
relay_log_info_repository        = table



#for group replication


transaction_write_set_extraction    =XXHASH64 
loose-group_replication_group_name    ="cccccccc-cccc-cccc-cccc-cccccccccccc"
loose-group_replication_start_on_boot    =off
loose-group_replication_local_address    ="192.168.64.156:4001"
loose-group_replication_group_seeds    ="192.168.64.156:4001,192.168.64.157:4002,192.168.64.158:4003"
loose-group_replication_bootstrap_group    =off
#loose-group_replication_single_primary_mode = true

#####MyISAM setting##########
key_buffer_size = 2048M
read_buffer_size = 256M
join_buffer_size = 128M
sort_buffer_size = 8M
read_rnd_buffer_size = 2M
bulk_insert_buffer_size = 256M
myisam_sort_buffer_size = 1G
myisam_max_sort_file_size = 10G
myisam_repair_threads = 8
##thread setting~~~~~~
thread_cache_size = 64

table_open_cache = 4096


max_allowed_packet = 512M

# for sysbench
max_prepared_stmt_count = 1000000
#max_prepared_stmt_count = 16382
[mysqldump]
quick
max_allowed_packet = 512M

[mysql]
no-auto-rehash
default-character-set = utf8

[myisamchk]
key_buffer_size = 512M
sort_buffer_size = 512M
read_buffer = 512M
write_buffer = 512M

[mysqlhotcopy]
interactive-timeout
```

### MGR

#### MGR配置

**主库**

```
#for gtid
gtid_mode = on
enforce_gtid_consistency = on

# for replication

master_info_repository           = table
relay_log_info_repository        = table



#for group replication


transaction_write_set_extraction    =XXHASH64 
loose-group_replication_group_name    ="cccccccc-cccc-cccc-cccc-cccccccccccc"
loose-group_replication_start_on_boot    =off
loose-group_replication_local_address    ="192.168.64.156:4001"
loose-group_replication_group_seeds    ="192.168.64.156:4001,192.168.64.157:4002,192.168.64.158:4003"
loose-group_replication_bootstrap_group    =off
#loose-group_replication_single_primary_mode = true

```
**从库**

```
auto_increment_increment = 1
auto_increment_offset = 1
binlog_checksum = none
binlog_rows_query_log_events = on
sync_binlog =1
binlog_format=row
transaction_isolation = READ-COMMITTED
log_slave_updates = on
expire_logs_days = 7

gtid_mode = on
enforce_gtid_consistency = on

master_info_repository           = table
relay_log_info_repository        = table
table_open_cache = 4096

transaction_write_set_extraction    =XXHASH64
loose-group_replication_start_on_boot    =off
loose-group_replication_bootstrap_group    =off
loose-group_replication_group_name    ="cccccccc-cccc-cccc-cccc-cccccccccccc"
** 注意localaddress端口不能和mysql的冲突 **
loose-group_replication_local_address    ="192.168.64.158:4003"
loose-group_replication_group_seeds    ="192.168.64.156:4001,192.168.64.157:4002,192.168.64.158:4003"

```

#### single-primary
**主库操作**

```
set sql_log_bin=0;
create user backup@'192.168.64.%' identified by 'backup';
grant replication slave,replication client on *.* to backup@'192.168.64.%';
set sql_log_bin=1;


set sql_log_bin=0;
change master to  master_user='backup',master_password='backup' for channel 'group_replication_recovery';
set sql_log_bin=1;


install plugin group_replication soname 'group_replication.so';


set global group_replication_bootstrap_group=on;
start group_replication;
set global group_replication_bootstrap_group=off;

```

**从库操作**


```
从库上操作是一致的

set sql_log_bin=0;
create user backup@'192.168.64.%' identified by 'backup';
grant replication slave,replication client on *.* to backup@'192.168.64.%';
set sql_log_bin=1;


set sql_log_bin=0;
change master to  master_user='backup',master_password='backup' for channel 'group_replication_recovery';
set sql_log_bin=1;


install plugin group_replication soname 'group_replication.so';

start group_replication;

```
**TIPS**

```
group_replication_allow_local_disjoint_gtids_join= on 强制加入兼容组 进入复制组(适用于gtid模式主从切换至group_replication模式)

```
```
跳过一个gtid复制
stop slave;
set next_gtid='';
begin;commmit;
set next_gtid='AUTOMATIC'
start slave;

```