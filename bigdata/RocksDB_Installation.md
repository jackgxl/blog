# RocksDB_Installation



## Tips

```shell
先检查 cpu 是否支持
yum 安装依赖
解压make
配置库 ldconfig
```



## 依赖关系安装

安装epel

```shell
rpm -ivh http://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
```

查看 cpu是否支持

```shell
cat /proc/cpuinfo| grep aes	
```



```shell
yum install -y python3 snappy snappy-devel  zlib zlib-devel  bzip2 bzip2-devel libasan libzstd-devel  lz4-devel  bzip2 lz4 ASAN zstd gcc-c++  gflags-devel readline-devel ncurses-devel openssl-devel  gdb git cmake gcc-c++ bzip2-devel libaio-devel bison  gflags 
```

epel8

```shell
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo rpm -ql epel-release
yum install -y python3 snappy git snappy-devel  zlib zlib-devel  bzip2 bzip2-devel  lz4-devel  libasan libzstd-devel gcc-c++ 
rocksdb-6.0.2.tar.gz  
zstd-1.5.0.tar.gz
tar zxf zstd-1.5.0.tar.gz
cd zstd-1.5.0/
make && sudo make install

git clone https://github.com/gflags/gflags.git
cd gflags
git checkout v2.0
./configure && make && sudo make install

vim /etc/ld.so.conf
echo "/usr/local/lib" >> /etc/ld.so.conf
ldconfig

tar zxf rocksdb-6.0.2.tar.gz
cd rocksdb-6.0.2/
make static_lib && sudo make install-static
make shared_lib && sudo make install-shared

```

test

```c++
#include <cstdio>
#include <string>

#include "rocksdb/db.h"
#include "rocksdb/slice.h"
#include "rocksdb/options.h"

using namespace std;
using namespace rocksdb;

const std::string PATH = "/tmp/rocksdb_tmp";

int main(){
    DB* db;
    Options options;
    options.create_if_missing = true;
    Status status = DB::Open(options, PATH, &db);
    assert(status.ok());
    Slice key("foo");
    Slice value("bar");
    
    std::string get_value;
    status = db->Put(WriteOptions(), key, value);
    if(status.ok()){
        status = db->Get(ReadOptions(), key, &get_value);
        if(status.ok()){
            printf("get %s success!!\n", get_value.c_str());
        }else{
            printf("get failed\n"); 
        }
    }else{
        printf("put failed\n");
    }

    delete db;
}
```

动态编译

```shell
g++ -std=c++11 -o rocksdbtest test.cpp -lrocksdb  -lpthread
./rocksdbtest
```



静态编译

```shell
g++ -std=c++11 -o rocksdbtest test.cpp ./librocksdb.a -lpthread -lsnappy  -lz -lbz2 -lzstd /usr/lib/x86_64-linux-gnu/liblz4.a
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

[RocksDB安装](https://xonlab.com/2020/11/08/rocksDB安装/)

[https://www.cnblogs.com/freeweb/p/10697246.html](https://www.cnblogs.com/freeweb/p/10697246.html)

[https://github.com/facebook/rocksdb/wiki/RocksDB-Compatibility-Between-Different-Releases](https://github.com/facebook/rocksdb/wiki/RocksDB-Compatibility-Between-Different-Releases)

[https://blog.csdn.net/TaroYoVen/article/details/88813386](https://blog.csdn.net/TaroYoVen/article/details/88813386)

