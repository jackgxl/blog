## MySQLServer优化内核参数

### /etc/sysctl.conf
```
 net.nf_conntrack_max=104857600
 net.core.somaxconn=65535
 net.netfilter.nf_conntrack_tcp_timeout_established = 300
 net.netfilter.nf_conntrack_tcp_timeout_time_wait = 120
 net.netfilter.nf_conntrack_tcp_timeout_close_wait = 60
 net.netfilter.nf_conntrack_tcp_timeout_fin_wait = 120
 net.core.rmem_max=1677721600
 net.core.rmem_default=167772160
 net.core.wmem_max=1677721600
 net.core.wmem_default=167772160
 net.core.optmem_max= 2048000
 net.ipv4.tcp_rmem= 1024000 8738000 1677721600
 net.ipv4.tcp_wmem= 1024000 8738000 1677721600
 net.ipv4.tcp_mem= 1024000 8738000 1677721600
 net.ipv4.udp_mem= 1024000 8738000 1677721600
 net.ipv4.tcp_keepalive_intvl = 75
 net.ipv4.tcp_keepalive_probes = 9
 net.ipv4.tcp_keepalive_time = 7200
 vm.dirty_background_ratio = 5
 vm.dirty_ratio = 10
```
### /etc/security/limits.conf
```
 * soft nofile 65535
 * hard nofile 65535
 * soft nproc 65535
 * hard nproc 65535
 * soft fsize unlimited
 * hard fsize unlimited
 * soft cpu unlimited
 * hard cpu unlimited
 * soft rss unlimited
 * hard rss unlimited
```

### /etc/security/limits.d/90-nproc.conf (如果是centos6)
```
 * hard nproc unlimited
 * soft nproc unlimited
```