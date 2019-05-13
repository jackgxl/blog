# RocksDB_Installation

## 依赖关系安装

```
yum install zlib zlib-devel bzip2 bzip2-devel lz4-devel libasan snappy snappy-devel -y
```
## 编译安装

```
wget https://github.com/facebook/rocksdb/archive/v6.0.2.tar.gz
mv v6.0.2.tar.gz rocksdb-v6.0.2.tar.gz
tar zxf rocksdb-6.0.2.tar.gz
cd rocksdb-6.0.2

make static_lib

make shared_lib

mkdir build
cd build

mkdir -pv /usr/local/rocksdb
cmake -DCMAKE_INSTALL_PREFIX=/usr/local/rocksdb ..
make -j 16
make install

```

加入环境变量

```
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/rocksdb/include/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/rocksdb/lib64/
export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/rocksdb/lib64/
```

## 安装go客户端

下载
```
go get github.com/tecbot/gorocksdb
```

报错类型

```shell
[root@local-153 src]# go get github.com/tecbot/gorocksdb
# github.com/tecbot/gorocksdb
github.com/tecbot/gorocksdb/array.go:4:11: fatal error: rocksdb/c.h: No such file or directory
 // #include "rocksdb/c.h"
           ^~~~~~~~~~~~~
compilation terminated.
[root@local-153 src]# go build -tags=embed
can't load package: package .: no Go files in /data/backup/go_workspace/src
```

解决方法

```
export CGO_CFLAGS="-I/usr/local/rocksdb/include"
export CGO_LDFLAGS="-L/usr/local/rocksdb -lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy -llz4 -lzstd"

go build -tags=embed 
```


## references

[https://www.cnblogs.com/freeweb/p/10697246.html](https://www.cnblogs.com/freeweb/p/10697246.html)

[https://github.com/facebook/rocksdb/wiki/RocksDB-Compatibility-Between-Different-Releases](https://github.com/facebook/rocksdb/wiki/RocksDB-Compatibility-Between-Different-Releases)


[https://blog.csdn.net/TaroYoVen/article/details/88813386]()