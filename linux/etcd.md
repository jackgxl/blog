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

```


