# mysql profiling

## MySQL5.0以后加入SQL分析查询语句重要工具，profiling


* 开启查询

```
set profiling=1;
```

执行SQL

```
exec SQL;
```

查看SQL执行总时间

```
show profilings;
```

查看SQL详细执行时间

```
show profiles for query 1;
```

关闭性能分析

```
set profiling=0

```