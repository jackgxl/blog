# Redis安装
```
* 说明：Redis 编译安装文档
* 作者：高学亮
* 邮箱：13716361153@163.com
* 时间：20170222
* 版本：1.0
```

### 下载安装包
```
wget http://download.redis.io/releases/redis-3.2.8.tar.gz
```
### 解决依赖关系
```
yum install gcc gcc-c++ tcl.x86_64 tcl-devel.x86_64 -y
```

### 内核调整

```
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo 1024 >/proc/sys/net/core/somaxconn

```

### 编译安装
```
cd redis-3.2.8
make
make test
make PREFIX=/usr/local/redis328 install
```
### 验证安装
```
[root@localhost ~]# redis-server --version
Redis server v=3.2.8 sha=00000000:0 malloc=jemalloc-4.0.3 bits=64 build=7a3e826ff5d9ad94
```
### 启动服务
```
创建目录
mkdir  -p /data/redis328
cd  /data/redis328
mkdir etc var log tmp
修改配置文件
cd redis-3.2.8
cp redis.conf /data/redis328/etc
cd /data/redis328/etc

vim redis.conf

redis-server etc/redis.conf
```
### 关闭服务

```
/usr/local/bin/redis-cli -p port -h ipv4 -a 123 shutdown
```
### 监控

```
/usr/local/bin/redis-cli -p port -h ipv4 -a 123 info 

```
**安装完毕**

# redis-sentinel

### sentinel 配置
```
port 5000
daemonize yes
logfile "/data/redis7001/log/sentinel.log"
dir "/data/redisi7001"
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel auth-pass mymaster 123456
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1
```

### sentinel启动

```
redis-sentinel /data/redis/etc/sentinel.conf
```

###  sentinel关闭