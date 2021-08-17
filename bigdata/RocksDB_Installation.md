# RocksDB_Installation

## 依赖关系安装

安装epel

```
rpm -ivh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install -y python3 snappy snappy-devel  zlib zlib-devel  bzip2 bzip2-devel  lz4-devel  libasan libzstd-devel
```

```
yum install -y zlib zlib-devel bzip2 bzip2-devel lz4-devel libasan snappy snappy-devel snappy zlib bzip2 lz4 ASAN zstd gcc-c++  gflags-devel readline-devel ncurses-devel openssl-devel lz4-devel gdb git cmake gcc-c++ bzip2-devel libaio-devel bison zlib-devel snappy-devel

yum install zlib zlib-devel bzip2 bzip2-devel lz4-devel libasan snappy snappy-devel snappy zlib bzip2 lz4 gflags zstd gcc-c++ python3 -y 


yum install libzstd-devel -y

```
## 编译安装

下载安装包
```
wget https://github.com/facebook/rocksdb/archive/v6.0.2.tar.gz
mv v6.0.2.tar.gz rocksdb-v6.0.2.tar.gz
tar zxf rocksdb-6.0.2.tar.gz
cd rocksdb-6.0.2
```

编译静态库，release mode，获得librocksdb.a

```
make static_lib
```

编译动态库，获得librocksdb.so，release mode，获得lbrocksdb.so

```
make shared_lib
```

编译到指定目录

```
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

* 报错类型

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


* 解决方法

```
export CGO_CFLAGS="-I/usr/local/rocksdb/include"
export CGO_LDFLAGS="-L/usr/local/rocksdb -lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy -llz4 -lzstd"

go build -tags=embed 
```


* 报错类型


```
[root@syq-133 src]# go get github.com/tecbot/gorocksdb                                                              
# runtime/cgo
/bin/ld: cannot find -lzstd
collect2: error: ld returned 1 exit status
```

* 解决办法

```
export CGO_LDFLAGS="-L/usr/local/rocksdb -lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy -llz4"

新版本取消了lzstd ？
```

环境变量问题
```
CGO_CFLAGS="-I/opt/rocksdb/include" CGO_LDFLAGS="-L/opt/rocksdb -lrocksdb -lstdc++ -lm -lz -lbz2 -lsnappy" go install
```



## references

[https://www.cnblogs.com/freeweb/p/10697246.html](https://www.cnblogs.com/freeweb/p/10697246.html)

[https://github.com/facebook/rocksdb/wiki/RocksDB-Compatibility-Between-Different-Releases](https://github.com/facebook/rocksdb/wiki/RocksDB-Compatibility-Between-Different-Releases)


[https://blog.csdn.net/TaroYoVen/article/details/88813386](https://blog.csdn.net/TaroYoVen/article/details/88813386)
