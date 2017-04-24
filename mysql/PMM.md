# <center>Percona Monitoring and Management </center>
# <center>(PMM)</center>

## 环境配置

```
cat /etc/redhat-release 
CentOS Linux release 7.3.1611 (Core)
```

## docker安装

```
yum install docker -y

systemctl start docker.service
systemctl status docker

```

## PMM安装

```
docker create  \
-v /data/pmm/prometheus/data \
-v /data/pmm/consul-data \
-v /var/lib/mysql \
-v /var/lib/grafana \
--name pmm-data percona/pmm-server:1.0.7 /bin/true

```

```
docker run -d  -p 80:80 --volumes-from pmm-data --name pmm-server --restart always percona/pmm-server:1.0.7
```

```

```


