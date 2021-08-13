# MySQL8.0.12\_alter\_algorithm

## 表结构

```
mysql(root@localhost:d1)>desc t1;
+---------+--------------+------+-----+---------+----------------+
| Field   | Type         | Null | Key | Default | Extra          |
+---------+--------------+------+-----+---------+----------------+
| id      | bigint(20)   | NO   | PRI | NULL    | auto_increment |
| context | varchar(155) | NO   |     |         |                |
+---------+--------------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

mysql(root@localhost:d1)>select count(*) from t1;
+----------+
| count(*) |
+----------+
|  3145728 |
+----------+
1 row in set (1.01 sec)
```

## 添加字段

```
mysql(root@localhost:d1)>alter table t1 add d1 varchar(20) not null  ,algorithm=inplace;  
Query OK, 0 rows affected (1 min 10.53 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql(root@localhost:d1)>alter table t1 add e1 varchar(20) not null  ,algorithm=copy;
Query OK, 3145728 rows affected (56.77 sec)
Records: 3145728  Duplicates: 0  Warnings: 0

mysql(root@localhost:d1)>alter table t1 add f1 varchar(20) not null  ,algorithm=instant;
Query OK, 0 rows affected (0.42 sec)
Records: 0  Duplicates: 0  Warnings: 0

```

## 删除字段

```
mysql(root@localhost:d1)>alter table t1 drop d1 ,algorithm=inplace;
```


```

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00  722.00   98.00     2.82     5.31    20.32     1.43    1.82    0.11   14.42   0.52  42.80
dm-1              0.00     0.00  722.00   72.00     2.82     4.31    18.40     1.43    1.87    0.10   19.61   0.54  42.80

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00  793.00   99.00     3.10     6.04    20.99     1.84    2.07    0.08   18.02   0.52  46.60
dm-1              0.00     0.00  793.00   82.00     3.10     6.05    21.41     1.84    2.11    0.08   21.74   0.53  46.80

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00  816.00   98.00     3.19     5.57    19.62     1.85    2.03    0.08   18.21   0.51  46.40
dm-1              0.00     0.00  816.00   80.00     3.19     5.57    20.01     1.85    2.06    0.08   22.31   0.52  46.40

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00  812.00   82.00     3.17     2.26    12.45     1.03    1.15    0.08   11.66   0.53  47.70
dm-1              0.00     0.00  812.00   62.00     3.17     2.26    12.73     1.04    1.17    0.09   15.42   0.55  47.90

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00  957.00  107.00     3.74     5.74    18.24     1.61    1.52    0.10   14.21   0.46  48.80
dm-1              0.00     0.00  957.00   85.00     3.74     5.73    18.61     1.64    1.54    0.09   17.88   0.47  48.60
```



```
mysql(root@localhost:d1)>alter table t1 drop e1 ,algorithm=inplace;
```

```
dm-1              0.00     0.00    3.00  720.00     0.01    13.72    38.89    18.35   25.60    0.67   25.71   1.37  98.90

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    0.00  787.00     0.00    10.69    27.82    19.24   24.36    0.00   24.36   1.26  98.90
dm-1              0.00     0.00    0.00  764.00     0.00    10.72    28.74    19.24   25.10    0.00   25.10   1.29  98.90

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    3.00  425.00     0.01    11.64    55.76     9.15   21.32    0.33   21.47   2.32  99.30
dm-1              0.00     0.00    3.00  404.00     0.01    12.61    63.52     9.16   22.42    0.33   22.58   2.44  99.40

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    7.00  473.00     0.03    15.24    65.15    14.56   30.18    0.14   30.62   1.88  90.40
dm-1              0.00     0.00    7.00  473.00     0.03    14.56    62.25    14.55   30.18    0.14   30.62   1.88  90.30

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    4.00  568.00     0.02    16.48    59.06    17.80   31.10    0.25   31.32   1.75 100.00
dm-1              0.00     0.00    4.00  536.00     0.02    16.38    62.17    17.80   32.95    0.25   33.19   1.85 100.00

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    5.00  627.00     0.02    14.54    47.17    19.57   31.12    0.20   31.36   1.58  99.70
dm-1              0.00     0.00    5.00  593.00     0.02    14.48    49.64    19.57   32.89    0.20   33.17   1.67  99.70

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    4.00  610.00     0.02    15.87    52.99    17.45   28.36    0.00   28.54   1.62  99.50
dm-1              0.00     0.00    4.00  587.00     0.02    16.09    55.81    17.45   29.47    0.25   29.66   1.68  99.50

Device:         rrqm/s   wrqm/s     r/s     w/s    rMB/s    wMB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sda               0.00     0.00    5.00  636.00     0.02    15.36    49.12    18.58   28.62    5.00   28.81   1.55  99.60
dm-1              0.00     0.00    5.00  636.00     0.02    16.09    51.47    18.60   28.62    5.00   28.81   1.56  99.70

```

```
mysql(root@localhost:d1)>alter table t1 drop f1 ,algorithm=instant;
ERROR 1845 (0A000): ALGORITHM=INSTANT is not supported for this operation. Try ALGORITHM=COPY/INPLACE.
```