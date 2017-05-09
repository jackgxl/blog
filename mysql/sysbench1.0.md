# sysbench1.0

### download tarball

```
wget https://codeload.github.com/akopytov/sysbench/tar.gz/1.0.4
```

### install steps

* unpack the tar packages

```
tar xf sysbench-1.0.4.tar.gz

cd sysbench-1.0.4/

```
* autoconfig && install

```
./autogen.sh 

dependencies:

./autogen.sh: running `autoconf' 
Libtoolized with: libtoolize (GNU libtool) 2.4.2
Automade with: automake (GNU automake) 1.13.4
Configured with: autoconf (GNU Autoconf) 2.69


./configure --with-mysql-libs=/ssd/mysql3306/lib/ --with-mysql-includes=/ssd/mysql3306/include/

make -j 12

make install


test for install

sysbench -V
sysbench 1.0.4 (using bundled LuaJIT 2.1.0-beta2)

Cannot find script -V: No such file or directory

installed successed
```

### use sysbench test mysql5.6.34

```
sysbench /root/sysbench-1.0.4/src/lua/oltp_read_write.lua  --mysql-host=localhost --mysql-port=3306  --mysql-user=root --mysql-password=213456 --mysql-socket=/ssd/mysql3306/tmp/mysql.sock --mysql-db=db1  --tables=10 --table-size=500000 --threads=50 --report-interval=5 --time=300 prepare


sysbench /root/sysbench-1.0.4/src/lua/oltp_write_only.lua  --mysql-host=localhost --mysql-port=3306  --mysql-user=root --mysql-password=213456 --mysql-socket=/ssd/mysql3306/tmp/mysql.sock --mysql-db=db1  --tables=10 --table-size=500000 --threads=50 --report-interval=5 --time=300 run

SQL statistics:    queries performed:        read:                            4128628        write:                           1179608        other:                           589804        total:                           5898040    transactions:                        294902 (982.88 per sec.)    queries:                             5898040 (19657.55 per sec.)    ignored errors:                      0      (0.00 per sec.)    reconnects:                          0      (0.00 per sec.)General statistics:    total time:                          300.0347s    total number of events:              294902
```



