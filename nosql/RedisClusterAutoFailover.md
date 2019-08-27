# Redis Cluster Auto Failover

## 参数解释

```
Redis Cluster的相关参数

cluster-enabled <yes/no>：是否开启集群模式。

cluster-config-file <filename>：集群配置文件，由集群自动维护，不建议手动编辑。

cluster-node-timeout <milliseconds>：集群中每个节点都会定期向其他节点发送ping消息，接收节点回复pong消息作为响应。如果在cluster-node-timeout时间内通信一直失败，则发送节点会认为接收节点存在故障，把接收节点标记为主观下线（pfail）状态。默认15000，即15s。

cluster-slave-validity-factor <factor>：每个从节点都要检查最后与主节点断线时间，判断其是否有资格替换故障的主节点。如果从节点与主节点断线时间超过cluster-node-time*cluster-slave-validity-factor，则当前从节点不具备故障转移资格。

cluster-migration-barrier <count>：主节点需要的最小从节点数，只有达到这个数，才会将多余的从节点迁移给其它孤立的主节点使用。

cluster-require-full-coverage <yes/no>：默认情况下当集群中16384个槽，有任何一个没有指派到节点时，整个集群是不可用的。对应在线上，如果某个主节点宕机，而又没有从节点的话，是不允许对外提供服务的。建议将该参数设置为no，避免某个主节点的故障导致其它主节点不可用。
```


## 集群管理

* 集群

```shell
clustr info 打印集群信息
cluster nodes  列出集群当前已知的节点，以及节点信息。
```

* 节点

```
cluster meet
192.168.64.182:6002> CLUSTER MEET 192.168.64.185 8001
OK
```

* 槽(slot)

**slot 迁移**

```

192.168.64.182:6003> cluster setslot 5461 migrating d8510f2ffccf98c1a3c7e332ae7457c023a37ac5

192.168.64.182:6003> cluster setslot 5462 migrating d8510f2ffccf98c1a3c7e332ae7457c023a37ac5

192.168.64.182:6003> cluster nodes
298b59cd5860c324d91a161d26f8232e2c46e015 192.168.64.185:8002@18002 slave d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 0 1566894422298 11 connected
3c197ab455c39aa8d599c6ead766ea0e42c3cf9a 192.168.64.183:7001@17001 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1566894420289 10 connected
1ee084d2d749c6f07eca0a8270a00dd48851780a 192.168.64.182:6001@16001 slave a9e61e278f81b15e9784c2c123c5f9de1d410b6e 0 1566894419000 9 connected
a9e61e278f81b15e9784c2c123c5f9de1d410b6e 192.168.64.183:7003@17003 master - 0 1566894420000 9 connected 0-5460
bec5a2d7d4d5d5fda1c891e079791d32a1526650 192.168.64.183:7002@17002 master - 0 1566894420000 7 connected 10923-16383
d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 192.168.64.185:8001@18001 master - 0 1566894420000 0 connected
0e2ed18c17e71568376fab40243421e3a1655686 192.168.64.182:6003@16003 myself,master - 0 1566894418000 10 connected 5461-10922 [5461->-d8510f2ffccf98c1a3c7e332ae7457c023a37ac5] [5462->-d8510f2ffccf98c1a3c7e332ae7457c023a37ac5]
bb5e192d7960660bdcd868ec71b39a239159a728 192.168.64.182:6002@16002 slave bec5a2d7d4d5d5fda1c891e079791d32a1526650 0 1566894421294 7 connected
```

* 键

```

```

## reference

[https://redis.io/topics/cluster-tutorial](https://redis.io/topics/cluster-tutorial)

[https://www.cnblogs.com/ivictor/p/9762394.html](https://www.cnblogs.com/ivictor/p/9762394.html)

