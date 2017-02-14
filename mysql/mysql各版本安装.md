#mysql安装文档
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
mkdir /usr/local/mysql5172_3306 -p
```
####编译安装
```
export bpath=/data/mysql5172_3306

./configure  --prefix=${bpath} --with-unix-socket-path=${bpath}/tmp/mysql.sock \
--with-plugins=partition,csv,archive,federated,innobase,innodb_plugin,myisam,heap \
--with-charset=utf8 \
--without-docs \
--without-man \
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
启动mysql：

```
cd /data/mysql5172_3306

cp share/mysql/mysql.server bin
修改启动脚本：
vim bin/mysql.server

$bindir/mysqld_safe --defaults-file=/data/mysql5172_3306/etc/my.cnf --datadir=$datadir --pid-file=$server_pid_file $other_args >/dev/null 2>&1 &

启动mysql：
/data/mysql5172_3306/bin/msyql.server start

修改密码：
/data/mysql5172_3306/bin/msyql -u root

mysql> set password=password('213456');
```

**mysql5.1.72 安装完毕**

------------------------------------------
##msyql5.5



------------------------------------------
##mysql5.6