# etcd

## 下载

```
https://github.com/etcd-io/etcd/releases
```

## 解压安装

```shell
[root@artron-local-110 ~]# cd etcd-v3.4.3-linux-amd64/
[root@artron-local-110 etcd-v3.4.3-linux-amd64]# ls
Documentation  etcd  etcdctl  README-etcdctl.md  README.md  READMEv2-etcdctl.md
[root@artron-local-110 etcd-v3.4.3-linux-amd64]# mv etcd etcdctl /usr/local/bin/
[root@artron-local-110 etcd-v3.4.3-linux-amd64]# ls
Documentation  README-etcdctl.md  README.md  READMEv2-etcdctl.md
[root@artron-local-110 etcd-v3.4.3-linux-amd64]# ll /usr/local/bin/etcd*
-rwxr-xr-x 1 lwq lwq 23712096 Oct 24 01:41 /usr/local/bin/etcd
-rwxr-xr-x 1 lwq lwq 17542688 Oct 24 01:41 /usr/local/bin/etcdctl
```

## 配置文件


## 启动

```


etcd --name 'etcd01' --data-dir=/data/etcd/data.etcd --wal-dir '/data/etcd/wal' \
	--initial-advertise-peer-urls 'http://192.168.64.110:2380' --listen-peer-urls 'http://192.168.64.110:2380' \
	--advertise-client-urls 'http://192.168.64.110:2379' --listen-client-urls 'http://192.168.64.110:2379' \
	--initial-cluster 'etcd01=http://192.168.64.110:2380,etcd02=http://192.168.64.183:2380,etcd03=http://192.168.64.185:2380' \
	--initial-cluster-state 'new' --initial-cluster-token 'etcd-cluster' --logger 'zap' --log-outputs '/data/etcd/etcd01.log'
	
	
	



etcd --name 'etcd03' --data-dir=/data/etcd/data.etcd --wal-dir '/data/etcd/wal' \
	--initial-advertise-peer-urls 'http://192.168.64.185:2380' --listen-peer-urls 'http://192.168.64.185:2380' \
	--advertise-client-urls 'http://192.168.64.185:2379' --listen-client-urls 'http://192.168.64.185:2379' \
	--initial-cluster 'etcd01=http://192.168.64.110:2380,etcd02=http://192.168.64.183:2380,etcd03=http://192.168.64.185:2380' \
	--initial-cluster-state 'new' --initial-cluster-token 'etcd-cluster' --logger 'zap' --log-outputs '/data/etcd/etcd03.log'
	
	
	


etcd --name 'etcd02' --data-dir=/data/etcd/data.etcd --wal-dir '/data/etcd/wal' \
	--initial-advertise-peer-urls 'http://192.168.64.183:2380' --listen-peer-urls 'http://192.168.64.183:2380' \
	--advertise-client-urls 'http://192.168.64.183:2379' --listen-client-urls 'http://192.168.64.183:2379' \
	--initial-cluster 'etcd01=http://192.168.64.110:2380,etcd02=http://192.168.64.183:2380,etcd03=http://192.168.64.185:2380' \
	--initial-cluster-state 'new' --initial-cluster-token 'etcd-cluster' --logger 'zap' --log-outputs '/data/etcd/etcd03.log'


```

## 检查集群

```
[root@localhost etcd]# etcdctl --endpoints="http://192.168.64.101:2379,http://192.168.64.183:2379,http://192.168.64.185:2379"  endpoint status  --write-out="table"
+----------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
|          ENDPOINT          |        ID        | VERSION | DB SIZE | IS LEADER | IS LEARNER | RAFT TERM | RAFT INDEX | RAFT APPLIED INDEX | ERRORS |
+----------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
| http://192.168.64.101:2379 | f2de9d180d47650c |   3.4.3 |   22 MB |     false |      false |        19 |       9013 |               9013 |        |
| http://192.168.64.183:2379 | e6ce75bd2bb1fbe9 |   3.4.3 |   22 MB |      true |      false |        19 |       9013 |               9013 |        |
| http://192.168.64.185:2379 | 35bc7cc16b544d95 |   3.4.3 |   22 MB |     false |      false |        19 |       9013 |               9013 |        |
+----------------------------+------------------+---------+---------+-----------+------------+-----------+------------+--------------------+--------+
[root@localhost etcd]# ETCDCTL_API=3  etcdctl --endpoints="http://192.168.64.101:2379,http://192.168.64.183:2379,http://192.168.64.185:2379"  put test abcde
OK
[root@localhost etcd]# ETCDCTL_API=3  etcdctl --endpoints="http://192.168.64.101:2379,http://192.168.64.183:2379,http://192.168.64.185:2379"  get test    
test
abcde
[root@localhost etcd]# ETCDCTL_API=3  etcdctl --endpoints="http://192.168.64.101:2379,http://192.168.64.183:2379,http://192.168.64.185:2379"  del test    
1
```

查询所有key

```shell
[root@localhost etcd]# ETCDCTL_API=3  etcdctl --endpoints="http://192.168.64.101:2379,http://192.168.64.183:2379,http://192.168.64.185:2379"  get --from-key ""
foo
hello
[root@localhost etcd]# ETCDCTL_API=3  etcdctl --endpoints="http://192.168.64.101:2379,http://192.168.64.183:2379,http://192.168.64.185:2379"  get foo
foo
hello
```

### reference

[https://www.cnblogs.com/li-peng/p/9259793.html](https://www.cnblogs.com/li-peng/p/9259793.html)

[https://blog.51cto.com/hequan/2327820](https://blog.51cto.com/hequan/2327820)