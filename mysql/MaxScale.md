# MaxScale Read/Write Splitting

## 配置环境变量

RHEL and CentOS
```
yum install -y gcc gcc-c++ ncurses-devel bison flex glibc-devel cmake libgcc perl make libtool openssl-devel libaio libaio-devel librabbitmq-devel libcurl-devel pcre-devel
```

下载安装包

```
最新版
wget https://downloads.mariadb.com/MaxScale/2.3.2/centos/7server/x86_64/maxscale-2.3.2.centos.7.tar.gz
稳定版
wget https://downloads.mariadb.com/MaxScale/latest/centos/7server/x86_64/maxscale-2.2.18.centos.7.tar.gz
```

解压安装包

```
tar zxf maxscale-2.3.2.centos.7.tar.gz -C /usr/local/
cd /usr/local
ln -sv maxscale-2.3.2.centos.7 maxscale
cd maxscale
chown -R maxscale:maxscale .
```

创建maxscale用户和数据目录

```
useradd -g maxscale maxscale
mkdir -pv /data/maxscale/{etc,data,tmp,log,cache}
cd /data/maxscale
chown -R maxscale:maxscale .
```

配置maxscale

```
cp /usr/local/maxscale/share/maxscale/maxscale.conf /data/maxscale/etc/maxscale.cnf
```

修改maxscale.cnf文件

```
[maxscale]
threads=1
log_info=1
maxlog=1
log_warning=1
log_debug=0
log_augmentation=1
libdir=/usr/local/maxscale/lib64/maxscale
execdir=/usr/local/maxscale/bin
logdir=/data/maxscale/log
datadir=/data/maxscale/data
cachedir=/data/maxscale/cache
piddir=/data/maxscale/pid
persistdir=/data/maxscale/etc/maxscale.cnf.d
module_configdir=/data/maxscale/etc/maxscale.modules.d
[server1]
type=server
address=192.168.64.152
port=3309
protocol=MySQLBackend
serv_weight=1
[server2]
type=server
address=192.168.64.159
port=3309
protocol=MySQLBackend
serv_weight=5
[MariaDB-Monitor]
type=monitor
module=mysqlmon
servers=server1,server2
user=maxscale_monitor
password=213456
monitor_interval=5000
detect_replication_lag=true
detect_stale_master=true
[Read-Write-Service]
type=service
router=readwritesplit
servers=server1,server2
user=maxscale_router
password=213456
max_slave_connections=100%
max_slave_replication_lag = 5
use_sql_variables_in = all
[MaxAdmin-Service]
type=service
router=cli
[Read-Write-Listener]
type=listener
service=Read-Write-Service
protocol=MySQLClient
port=4006
[MaxAdmin-Listener]
type=listener
service=MaxAdmin-Service
protocol=maxscaled
socket=/data/maxscale/tmp/maxadmin.sock
```

启动

```
/usr/local/maxscale/bin/maxscale --user=maxscale -f /data/maxscale/etc/maxscale.cnf 
```

maxadmin 入口

```
/usr/local/maxscale/bin/maxadmin -S /var/run/maxscale/maxadmin.sock 
```

# Referance

[https://mariadb.com/kb/en/mariadb-enterprise/maxscale-20-tutorials/](https://mariadb.com/kb/en/mariadb-enterprise/maxscale-20-tutorials/)

[https://renwole.com/archives/253](https://renwole.com/archives/253)

[https://www.cnblogs.com/galengao/p/5841384.html](https://www.cnblogs.com/galengao/p/5841384.html)

[http://blog.51cto.com/lee90/1945504](http://blog.51cto.com/lee90/1945504)

