# NSQ

## 下载

[NSQ Docs 1.2.1](https://nsq.io/deployment/installing.html)

##  安装部署


```shell
tar zxf nsq-1.2.1.linux-amd64.go1.16.6.tar.gz -C /usr/local
ln -sv nsq-1.2.1.linux-amd64.go1.16.6 nsq
```


```shell
mkdir -pv /data/nsq_data/
```



```shell
nohup /usr/local/nsq/bin/nsqlookupd  > lookup.out 2>&1 &

nohup /usr/local/nsq/bin/nsqd --lookupd-tcp-address=127.0.0.1:4160 > nsqd.out 2>&1 &
        
nohup /usr/local/nsq/bin/nsqadmin --lookupd-http-address=0.0.0.0:4161 --http-address=192.168.64.219:8761 > admin.out 2>&1 &

```









