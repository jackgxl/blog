# mysql 显示执行的sql 和 结果

-D  库名
-v  显示
-vvv  显示更详细内容
-e 执行SQL


```
/usr/local/mysql3308/bin/mysql -S /data/mysql3308/tmp/mysql.sock -uroot -p213456 -v -D mysql -e 'source /home/gaoxueliang/154.sql';
```