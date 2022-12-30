#  MySQL\_REPLICATE\_REWRITE\_DB

## MySQL_INSTALL

```
tar zxf  mysql-boost-5.7.20.tar.gz 
cd mysql-5.7.20/
```

```
[root@SYQ-94 mysql-5.7.20]# ls
boost   CMakeLists.txt   COPYING              extra            libbinlogstandalone  libservices  mysys_ssl  README   sql-common     testclients  win
BUILD   cmd-line-utils   dbug                 include          libevent             man          packaging  regex    storage        unittest     zlib
client  config.h.cmake   Docs                 INSTALL          libmysql             mysql-test   plugin     scripts  strings        VERSION
cmake   configure.cmake  Doxyfile-perfschema  libbinlogevents  libmysqld            mysys        rapid      sql      support-files  vio
```
```
tar zxf cmake-2.8.10.2.tar.gz 
mkdir -pv /usr/local/cmake28
cd cmake-2.8.10.2
./bootstrap --prefix=/usr/local/cmake28/
gmake
gmake install
```
```
mkdir -pv /data/mysql3307
cd mysql3307
mkdir etc var log tmp
```

```
cd mysql-5.7.20/

/usr/local/cmake28/bin/cmake  \
-DCMAKE_INSTALL_PREFIX=/data/mysql3308 \
-DMYSQL_UNIX_ADDR=/data/mysql3308/tmp/mysql.sock \
-DEXTRA_CHARSETS=all \
-DDEFAULT_CHARSET=utf8mb4 \
-DDEFAULT_COLLATION=utf8mb4_general_ci \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
-DWITH_BLACKHOLE_STORAGE_ENGINE=1 \
-DSYSCONFDIR=/data/mysql3308/etc    \
-DWITH_READLINE=1 \
-DENABLED_LOCAL_INFILE=1 \
-DMYSQL_DATADIR=/data/mysql3308/var \
-DMYSQL_USER=mysql \
-DMYSQL_TCP_PORT=3308 \
-DENABLE_DOWNLOADS=1 \
-DWITH_BOOST=boost/boost_1_59_0/ 

```

```
cd /data/mysql3307/etc

rz my.cnf

cd ..

./bin/mysqld --defaults-file=etc/my.cnf --user=mysql --initialize

tail -f log/mysql.err

cp support-files/mysql.server bin/

启动脚本中加入 --defaults-file=/data/mysql3307/etc/my.cnf

./bin/mysql.server start

启动mysql 修改password

```
## MySQL\_REPLICATE_CONFIG

```
CHANGE MASTER TO
  MASTER_HOST='master2.mycompany.com',
  MASTER_USER='replication',
  MASTER_PASSWORD='bigs3cret',
  MASTER_PORT=3306,
  MASTER_LOG_FILE='master2-bin.001',
  MASTER_LOG_POS=4,
  MASTER_CONNECT_RETRY=10 for channel 'channel_1';
  
 CHANGE REPLICATION FILTER REPLICATE_REWRITE_DB = ((db1, new_db2));
 
 start slave for channel 'channel_1'; 

tips:
MySQL 重启后rewrite配置清空，需要重新配置；最好写入配置文件
```



