# MongoDB\_install\_doc

## MongoDB 下载

```
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-4.0.5.tgz

```

## CentOS7 配置

```
never > /sys/kernel/mm/transparent_hugepage/enabled
never > /sys/kernel/mm/transparent_hugepage/defrag
echo "vm.swappiness = 5" >>/etc/sysctl.conf
echo "vm.dirty_background_ratio = 5" >>/etc/sysctl.conf
echo "vm.dirty_ratio = 10" >>/etc/sysctl.conf
echo "net.ipv4.tcp_tw_recycle = 1" >> /etc/sysctl.conf
echo "net.ipv4.tcp_tw_reuse = 1" >> /etc/sysctl.conf
sysctl -p
```

## MongoDB 副本集配置

```

```


## mongos 配置

```


```

## mongod 配置

```

```