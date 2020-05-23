# mongodb best practices 2020 edition

## OS Settings

**Swappiness**


```shell
重启后重新设置
echo 1 > /proc/sys/vm/swappiness
生效命令
sudo sysctl -w vm.swappiness=1
```


**NUMA Architecture**

```
numactl --interleave=all mongod -f /etc/mongod.conf
```

查看mongo在 numa 内存分布

```
sudo numastat -p $(pidof mongod)
```



**zone_reclaim_mode**

echo 0 > /proc/sys/vm/zone_reclaim_mode


**IO Scheduler**

```
# Verifying
$ cat /sys/block/xvda/queue/scheduler
noop [deadline] cfq

# Adjusting the value dynamically
$ echo "noop" > /sys/block/xvda/queue/scheduler
```



**Transparent Huge Pages**

```
echo "never" > /sys/kernel/mm/transparent_hugepage/enabled
echo "never" > /sys/kernel/mm/transparent_hugepage/defrag
```



**Dirty Ratio**

```
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5
```

**Filesystems mount options**

```
mount -oremount,rw,noatime/mnt/db
```

```
UUID=f41e390f-835b-4223-a9bb-9b45984ddf8d /                       xfs     rw,noatime,attr2,inode64,noquota        0 0
```


**Unix ulimit Settings**

```
/etc/security/limits.conf
mongo hard nofile 64000
mongo soft nofile 64000
mongo hard nproc 192276
mongo soft nproc 192276
```


**Network Stack**

```
net.core.somaxconn = 4096
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_intvl = 30
net.ipv4.tcp_keepalive_time = 120
net.ipv4.tcp_max_syn_backlog = 4096
net.ipv4.tcp_keepalive_probes = 6
```



## MongoDB Settings

**Journal commit interval**

```shell
# edit /etc/mongod.conf
storage:
  journal:
    enabled: true
    commitIntervalMs: 300
```

**WiredTiger cache**

```
# edit /etc/mongod.conf
wiredTiger:
   engineConfig:
      cacheSizeGB: 50
```


**Read/Write tickets**

```
use admin
db.adminCommand( { setParameter: 1, wiredTigerConcurrentReadTransactions: 256 } )
db.adminCommand( { setParameter: 1, wiredTigerConcurrentWriteTransactions: 256 } )
```


##reference

[percona](https://www.percona.com/blog/2020/04/17/mongodb-best-practices-2020-edition/)    