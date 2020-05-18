# prometheus


## maproad

```
192.168.64.185 prometheus 
192.168.64.154 node grafana 
192.168.64.160 node 
192.168.64.152 node 
```

## reload prometheus


```
kill -1 pid

curl -XPOST http://ip:9090/-/reload
```



## mysqld_export 集中部署

```
 mysqld_exporter --web.listen-address=192.168.64.154:19101 --config.my-cnf=/data/mysql_export/conf/dev_160_3306.cnf --collect.slave_status --collect.slave_hosts --collect.global_status --collect.global_variables --collect.engine_innodb_status --collect.info_schema.processlist 
```

```
[root@mgr-154 backup]# cd /data/mysql_export/
[root@mgr-154 mysql_export]# ll
total 0
drwxr-xr-x 2 root root 54 Apr 27 09:07 conf
drwxr-xr-x 2 root root 54 Apr 26 16:20 log
drwxr-xr-x 2 root root 52 Apr 27 09:17 sh
[root@mgr-154 mysql_export]# cat conf/dev_160_330
dev_160_3306.cnf  dev_160_3307.cnf  
[root@mgr-154 mysql_export]# cat conf/dev_160_330
dev_160_3306.cnf  dev_160_3307.cnf  
[root@mgr-154 mysql_export]# cat conf/dev_160_3306.cnf 
[client]
user=xxxx
password=xxxx
host=192.168.64.160
prot=3306
```

## reference

[https://yuerblog.cc/2019/01/04/grafana-usage/#post-4045-_Toc534383110](https://yuerblog.cc/2019/01/04/grafana-usage/#post-4045-_Toc534383110)

**Prometheus监控实战 （澳）詹姆斯·特恩布尔（James Turnbull） 著**