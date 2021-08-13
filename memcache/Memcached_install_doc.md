## Memcached

```
* 说明：Memcached 编译安装文档
* 作者：高学亮
* 邮箱：13716361153@163.com
* 时间：20170222
* 版本：1.0
```

### 下载安装包

```
yum install libevent.x86_64 libevent-devel.x86_64 -y

wget http://memcached.org/files/memcached-1.4.34.tar.gz

wget https://cloud.github.com/downloads/libevent/libevent/libevent-2.0.21-stable.tar.gz

```

### 解决依赖关系

```
tar zxf libevent-2.0.21-stable.tar.gz
cd libevent-2.0.21-stable
./configure --prefix=/home/libevent
make && make install
```

### 编译安装

```
./configure --with-libevent=/home/libevent/
make && make install
```

### 验证安装

```
[root@localhost ~]# memcached -V
memcached 1.4.34
```

### 启动服务

```
/usr/local/bin/memcached -d -m 500 -u root -l 192.168.64.153 -p 11211 -c 256 -P /tmp/memcached.pid
```

**安装完毕**
***