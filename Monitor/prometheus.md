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

## reference

[https://yuerblog.cc/2019/01/04/grafana-usage/#post-4045-_Toc534383110](https://yuerblog.cc/2019/01/04/grafana-usage/#post-4045-_Toc534383110)

**Prometheus监控实战 （澳）詹姆斯·特恩布尔（James Turnbull） 著**