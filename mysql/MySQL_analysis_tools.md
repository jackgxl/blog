# MySQL 分析工具

## strace

## pstack

用法：
pstack $pid

用例：
ps -ef | grep mysql

```
root     66079     1  0 Jun25 ?        00:00:00 /bin/sh /usr/local/mysql8011_3310/bin/mysqld_safe --defaults-file=/data/mysql8011_3310/etc/my.cnf --datadir=/data/mysql8011_3310/var --pid-file=/data/mysql8011_3310/var/mysql.pid

mysql    67436 66079  0 Jun25 ?        03:31:47 /usr/local/mysql8011_3310/bin/mysqld --defaults-file=/data/mysql8011_3310/etc/my.cnf --basedir=/usr/local/mysql8011_3310 --datadir=/data/mysql8011_3310/var --plugin-dir=/usr/local/mysql8011_3310/lib/plugin --user=mysql --log-error=/data/mysql8011_3310/log/mysql.err --pid-file=/data/mysql8011_3310/var/mysql.pid --socket=/data/mysql8011_3310/tmp/mysql.sock --port=3310
```

pstack 66079

```
[root@mgr3 ~]# pstack 67436
Thread 60 (Thread 0x7f20d2ffd700 (LWP 67450)):
#0  0x00007f2107a13644 in __io_getevents_0_4 () from /lib64/libaio.so.1
#1  0x0000000001d33da7 in LinuxAIOHandler::collect (this=this@entry=0x7f20d2ffcb90) at /root/mysql-8.0.11/storage/innobase/os/os0file.cc:2325
#2  0x0000000001d34645 in LinuxAIOHandler::poll (this=this@entry=0x7f20d2ffcb90, m1=m1@entry=0x7f20d2ffcc30, m2=m2@entry=0x7f20d2ffcc38, request=request@entry=0x7f20d2ffcc40) at /root/mysql-8.0.11/storage/innobase/os/os0file.cc:2456
#3  0x0000000001d3a770 in os_aio_linux_handler (request=0x7f20d2ffcc40, m2=0x7f20d2ffcc38, m1=0x7f20d2ffcc30, global_segment=0) at /root/mysql-8.0.11/storage/innobase/os/os0file.cc:2505
#4  os_aio_handler (segment=segment@entry=0, m1=m1@entry=0x7f20d2ffcc30, m2=m2@entry=0x7f20d2ffcc38, request=request@entry=0x7f20d2ffcc40) at /root/mysql-8.0.11/storage/innobase/os/os0file.cc:5812
#5  0x0000000001f19444 in fil_aio_wait (segment=segment@entry=0) at /root/mysql-8.0.11/storage/innobase/fil/fil0fil.cc:7270
#6  0x0000000001dd0af8 in io_handler_thread (segment=0) at /root/mysql-8.0.11/storage/innobase/srv/srv0start.cc:264
#7  0x0000000001dd0de8 in __call<void, 0ul> (__args=<optimized out>, this=<synthetic pointer>) at /usr/include/c++/4.8.2/functional:1296
#8  operator()<, void> (this=<synthetic pointer>) at /usr/include/c++/4.8.2/functional:1355
#9  operator()<void (*)(long unsigned int), long unsigned int> (f=<unknown type in /usr/local/mysql8011_3310/bin/mysqld, CU 0x125bae1d, DIE 0x12667137>, this=0x7f20e4220380) at /root/mysql-8.0.11/storage/innobase/include/os0thread-create.h:92
#10 _M_invoke<0ul, 1ul> (this=0x7f20e4220370) at /usr/include/c++/4.8.2/functional:1732
#11 operator() (this=0x7f20e4220370) at /usr/include/c++/4.8.2/functional:1720
#12 std::thread::_Impl<std::_Bind_simple<Runnable (void (*)(unsigned long), unsigned long)> >::_M_run() (this=0x7f20e4220358) at /usr/include/c++/4.8.2/thread:115
#13 0x00007f210691a070 in ?? () from /lib64/libstdc++.so.6
#14 0x00007f2107c1cdc5 in start_thread () from /lib64/libpthread.so.0
#15 0x00007f210608373d in clone () from /lib64/libc.so.6
```
 