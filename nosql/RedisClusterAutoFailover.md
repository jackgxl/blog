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


## reference

[https://redis.io/topics/cluster-tutorial](https://redis.io/topics/cluster-tutorial)

[https://www.cnblogs.com/ivictor/p/9762394.html](https://www.cnblogs.com/ivictor/p/9762394.html)

