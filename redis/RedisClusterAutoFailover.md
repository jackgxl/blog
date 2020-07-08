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

操作步骤

```shell
1、目标实例
cluster setslot {slot} importing {source_node_id} //让目标实例准备导入槽的数据
2、源实例
cluster setslot {slot} migrating {target_node_id} //让源实例准备迁出槽的数据
3、源实例
cluster getkeysinslot {slot} {count} // 获取要迁移槽的key
4、源实例
migrate {target_node_ip} {target_node_port} key 0 {timeout} auth {pass} keys ... //MIGRATE 192.168.64.182 6003 "" 0 5000 auth {password} keys 3461 6313
5、通知集群中所有主节点，槽分配给目标实例
cluster setslot {slot} node {target_node_id}

```

cluster nodes

```
192.168.64.182:6003> cluster nodes
298b59cd5860c324d91a161d26f8232e2c46e015 192.168.64.185:8002@18002 slave d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 0 1567411034000 12 connected
3c197ab455c39aa8d599c6ead766ea0e42c3cf9a 192.168.64.183:7001@17001 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1567411032000 10 connected
1ee084d2d749c6f07eca0a8270a00dd48851780a 192.168.64.182:6001@16001 slave a9e61e278f81b15e9784c2c123c5f9de1d410b6e 0 1567411032000 9 connected
a9e61e278f81b15e9784c2c123c5f9de1d410b6e 192.168.64.183:7003@17003 master - 0 1567411034804 9 connected 1-5460
bec5a2d7d4d5d5fda1c891e079791d32a1526650 192.168.64.183:7002@17002 master - 0 1567411031794 7 connected 10923-16383
bb5e192d7960660bdcd868ec71b39a239159a728 192.168.64.182:6002@16002 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1567411033801 10 connected
d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 192.168.64.185:8001@18001 master - 0 1567411032797 12 connected 0 5461-5462
0e2ed18c17e71568376fab40243421e3a1655686 192.168.64.182:6003@16003 myself,master - 0 1567411033000 10 connected 5463-10922
```

需要迁移的slot

```
192.168.64.182:6002> CLUSTER GETKEYSINSLOT 10001 100
1) "3461"
2) "6313"

```

迁移步骤

* 实例名称
    
```
原实例
bec5a2d7d4d5d5fda1c891e079791d32a1526650 192.168.64.183:7002

目标实例

d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 192.168.64.185:8001

```

* 操作步骤


```
原实例

192.168.64.182:6003> mget 3461 6313
1) "3461"
2) "6313"

```

```
目的实例

192.168.64.185:8001> keys *
(empty list or set)
192.168.64.185:8001> CLUSTER GETKEYSINSLOT 0 100
(empty list or set)
192.168.64.185:8001> CLUSTER GETKEYSINSLOT 5461 100
(empty list or set)
192.168.64.185:8001> CLUSTER GETKEYSINSLOT 5462 100
(empty list or set)
192.168.64.185:8001> 

```


目标节点准备导入10001槽

```
192.168.64.185:8001> CLUSTER SETSLOT 10001 importing d8510f2ffccf98c1a3c7e332ae7457c023a37ac5
OK
```

确认槽10001倒入状态开启

```
192.168.64.185:8001> cluster nodes
3c197ab455c39aa8d599c6ead766ea0e42c3cf9a 192.168.64.183:7001@17001 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1567414276992 10 connected
bec5a2d7d4d5d5fda1c891e079791d32a1526650 192.168.64.183:7002@17002 master - 0 1567414275989 7 connected 10923-16383
0e2ed18c17e71568376fab40243421e3a1655686 192.168.64.182:6003@16003 master - 0 1567414275000 10 connected 5463-10922
bb5e192d7960660bdcd868ec71b39a239159a728 192.168.64.182:6002@16002 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1567414273000 10 connected
298b59cd5860c324d91a161d26f8232e2c46e015 192.168.64.185:8002@18002 slave d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 0 1567414276000 12 connected
1ee084d2d749c6f07eca0a8270a00dd48851780a 192.168.64.182:6001@16001 slave a9e61e278f81b15e9784c2c123c5f9de1d410b6e 0 1567414274987 9 connected
d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 192.168.64.185:8001@18001 myself,master - 0 1567414272000 12 connected 0 5461-5462 [10001-<-d8510f2ffccf98c1a3c7e332ae7457c023a37ac5]
a9e61e278f81b15e9784c2c123c5f9de1d410b6e 192.168.64.183:7003@17003 master - 0 1567414274000 9 connected 1-5460
192.168.64.185:8001> 
```

源节点准备导出槽10001

```
192.168.64.182:6003> CLUSTER SETSLOT 10001 migrating d8510f2ffccf98c1a3c7e332ae7457c023a37ac5
OK
192.168.64.182:6003> cluster nodes
298b59cd5860c324d91a161d26f8232e2c46e015 192.168.64.185:8002@18002 slave d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 0 1567414649000 12 connected
3c197ab455c39aa8d599c6ead766ea0e42c3cf9a 192.168.64.183:7001@17001 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1567414650000 10 connected
1ee084d2d749c6f07eca0a8270a00dd48851780a 192.168.64.182:6001@16001 slave a9e61e278f81b15e9784c2c123c5f9de1d410b6e 0 1567414650000 9 connected
a9e61e278f81b15e9784c2c123c5f9de1d410b6e 192.168.64.183:7003@17003 master - 0 1567414651784 9 connected 1-5460
bec5a2d7d4d5d5fda1c891e079791d32a1526650 192.168.64.183:7002@17002 master - 0 1567414649000 7 connected 10923-16383
bb5e192d7960660bdcd868ec71b39a239159a728 192.168.64.182:6002@16002 slave 0e2ed18c17e71568376fab40243421e3a1655686 0 1567414650781 10 connected
d8510f2ffccf98c1a3c7e332ae7457c023a37ac5 192.168.64.185:8001@18001 master - 0 1567414649000 12 connected 0 5461-5462
0e2ed18c17e71568376fab40243421e3a1655686 192.168.64.182:6003@16003 myself,master - 0 1567414648000 10 connected 5463-10922 [10001->-d8510f2ffccf98c1a3c7e332ae7457c023a37ac5]
192.168.64.182:6003> 
```

确认源节点槽10001导出状态开启

```

```

迁移槽10001keys到目的节点

```
192.168.64.182:6003> mget 3461 6313
1) "3461"
2) "6313"
192.168.64.182:6003> MIGRATE 192.168.64.185 8001 "" 0 5000 auth password keys 3461 6313

192.168.64.183:7003> mget 3461 6313
-> Redirected to slot [10001] located at 192.168.64.182:6003
1) "3461"
2) "6313"
192.168.64.182:6003> 
```

确认数据迁移完成

```
192.168.64.185:8001> mget 3461 6313
-> Redirected to slot [10001] located at 192.168.64.182:6003
1) "3461"
2) "6313"
192.168.64.182:6003> 
```


**取消槽迁移**

```
 CLUSTER SETSLOT {slot} stable
```



* 键

获取slot中的key

```
192.168.64.182:6003> CLUSTER GETKEYSINSLOT 10001 1000
1) "3461"
2) "6313"
```

## reference


[https://redis.io/topics/cluster-tutorial](https://redis.io/topics/cluster-tutorial)

[https://redis.io/commands/migrate](https://redis.io/commands/migrate)

[https://www.cnblogs.com/kevingrace/p/7910692.html](https://www.cnblogs.com/kevingrace/p/7910692.html)

[https://www.cnblogs.com/ivictor/p/9762394.html](https://www.cnblogs.com/ivictor/p/9762394.html)

[https://www.jianshu.com/p/15ec6e870f2d](https://www.jianshu.com/p/15ec6e870f2d)

[https://www.cnblogs.com/Cherry-Linux/p/8046276.html](https://www.cnblogs.com/Cherry-Linux/p/8046276.html)




