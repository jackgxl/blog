# Redis Cluster 部署

## 分布

|IP地址|端口号|
|:-:|:-:|
| 192.168.64.182|6001 |
| 192.168.64.182| 6002|
| 192.168.64.182| 6003|
|192.168.64.183|7001|
|192.168.64.183|7002|
|192.168.64.183|7003|


## 下载

```
wget http://download.redis.io/releases/redis-5.0.5.tar.gz

```


**安装请参考**

[Redis编译安装](https://github.com/jackgxl/blog/blob/master/nosql/Redis_install_doc.md)

## 配置

其中之一的配置文件，修改端口号，路径即可。

```shell
bind 0.0.0.0
protected-mode yes
port 7003
tcp-backlog 511
unixsocket /data/redis7003/tmp/redis.sock
unixsocketperm 700
timeout 0
tcp-keepalive 300
daemonize yes
supervised no
pidfile /data/redis7003/var/redis_7003.pid
loglevel notice
logfile "/data/redis7003/log/redis_7003.log"
databases 16
always-show-logo yes
save 86400000 1
stop-writes-on-bgsave-error yes
rdbcompression yes
rdbchecksum yes
dbfilename dump7003.rdb
dir "/data/redis7003/var"
replica-serve-stale-data yes
replica-read-only yes
repl-diskless-sync no
repl-diskless-sync-delay 5
repl-timeout 180
repl-disable-tcp-nodelay no
repl-backlog-size 10mb
repl-backlog-ttl 100
replica-priority 100
requirepass 123
maxclients 50000
maxmemory 500*1024*1024
maxmemory-policy noeviction
lazyfree-lazy-eviction no
lazyfree-lazy-expire no
lazyfree-lazy-server-del no
replica-lazy-flush no
appendonly no
appendfilename "appendonly.aof"
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
aof-load-truncated yes
aof-use-rdb-preamble yes
lua-time-limit 5000

cluster-enabled yes
cluster-config-file nodes-7003.conf
cluster-node-timeout 15000


slowlog-log-slower-than 1000
slowlog-max-len 1024
latency-monitor-threshold 0
notify-keyspace-events ""
hash-max-ziplist-entries 512
hash-max-ziplist-value 64
list-max-ziplist-size -2
list-compress-depth 0
set-max-intset-entries 512
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
hll-sparse-max-bytes 3000
stream-node-max-bytes 4096
stream-node-max-entries 100
activerehashing yes
client-output-buffer-limit normal 1gb 1gb 60
client-output-buffer-limit replica 512mb 512mb 60
client-output-buffer-limit pubsub 32mb 8mb 60
hz 10
dynamic-hz yes
aof-rewrite-incremental-fsync yes
rdb-save-incremental-fsync yes
```

## 启动

创建集群

```
/usr/local/redis/bin/redis-cli --cluster create 192.168.64.182:6001 192.168.64.182:6002 192.168.64.182:6003 192.168.64.183:7001 192.168.64.183:7002 192.168.64.183:7003 --cluster-replicas 1  --verbose -a 123   --no-auth-warning
```

连接集群

```
/usr/local/redis/bin/redis-cli -c -h 192.168.64.182 -p 6001
```

设置密码

```
config set masterauth 123
config set requirepass 123
config rewrite
```



## 监控



### reference

[官方文档](https://redis.io/topics/cluster-tutorial)

[https://blog.51cto.com/andyxu/2319767](https://blog.51cto.com/andyxu/2319767)

[https://blog.51cto.com/kerry/2316700](https://blog.51cto.com/kerry/2316700)