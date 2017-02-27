#mysql安装文档
```
* 说明：mysql5.1 5.5 5.6 编译安装文档
* 作者：高学亮
* 邮箱：13716361153@163.com
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
yum install gcc gcc-c++ cmake  make  autoconf automake ncurses-devel  libaio.x86_64 libaio-devel.x86_64 readline.x86_64 readline-devel.x86_64
```
配置系统环境：
		
	echo vm.swappiness = 0 >>/etc/sysctl.conf
	sysctl -p
	echo deadline> /sys/block/sda/queue/scheduler
	vim /etc/security/limits.conf 
		* soft nofile 65536
		* hard nofile 65536
		* soft nproc 65535
		* hard nproc 65535

##mysql5.1

####下载安装包
```
mysql5.1版本 mysql-5.1.72.tar.gz，请到官方网站下载移动到/home 并验证md5值 
```
####解压
```
cd /home
tar xf mysql-5.1.72.tar.gz
```
####创建目录
```
mkdir /data/mysql5172_3306 -p
```
####编译安装
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
####数据文件单独存放的编译方式
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

####初始化
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

####启动mysql：

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
 
###mysql5.1.72 安装完毕
***
##mysql5.5

####下载安装包
```
mysql5.5版本 mysql-5.5.51.tar.gz，请到官方网站下载移动到/home 并验证md5值 
```
####解压
```
cd /home/
tar xf mysql-5.5.51.tar.gz
```
####创建目录
```
mkdir -p /data/mysql5551_3307
```
####编译安装
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
####初始化
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
####启动mysql
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
###mysql5.5.51 安装完毕
***

##mysql5.6
####下载安装包
```
mysql5.6版本 mysql-5.6.34.tar.gz，请到官方网站下载移动到/home 并验证md5值 
```
####解压
```
cd /home/
tar xf mysql-5.6.34.tar.gz
```
####创建目录
```
mkdir -p /data/mysql5634_3308
```
####编译安装
```
export bpath=/data/mysql5634_3308

cmake . \
-DCMAKE_INSTALL_PREFIX=${bpath}  \
-DINSTALL_MYSQLDATADIR=${bpath}/var  \
-DMYSQL_DATADIR=${bpath}/var \
-DSYSCONFDIR=${bpath}/etc    \
-DWITH_INNOBASE_STORAGE_ENGINE=1  \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_MEMORY_STORAGE_ENGINE=1 \
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
####初始化
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
####启动mysql
```
./bin/mysql.server start
设置密码：
./bin/mysql -uroot
set password=password('123456');
flush privileges;

```
###mysql5.6.34 安装完毕