# MySQL binlog server

## cmd 

```shell
/usr/local/mysql3310/bin/mysqlbinlog -h 192.168.64.210 -P3307 -ugao -pxxxxx --raw -R --stop-never mysql-bin.000139 --result-file=/data/backup/binlogset/1603307/ -vv
```



## trace

```shell
strace -T -tt -p `pidof mysqlbinlog` -o  /data/backup/1603307/t.log
```

