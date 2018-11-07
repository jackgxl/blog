# MySQL隐式类型转换

## 一条慢SQL的
```
select * from t_xxx where PK = 0 ;

返回了t_xxx表所有数据
```
## 验证SQL环境
* 表结构

    ``` sql
    mysql(root@localhost)[zz](15:17:02)>show create table t1 \G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `a` char(32) NOT NULL,
  `b` char(4) NOT NULL,
  `c` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
mysql(root@localhost)[zz](15:17:08)>show create table t2 \G
*************************** 1. row ***************************
       Table: t2
Create Table: CREATE TABLE `t2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `sexy` tinyint(1) NOT NULL DEFAULT '0',
  `addr` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
mysql(root@localhost)[zz](15:18:41)>show create table t3 \G
*************************** 1. row ***************************
       Table: t3
Create Table: CREATE TABLE `t3` (
  `a` char(20) NOT NULL,
  `b` char(5) NOT NULL,
  `c` char(30) NOT NULL,
  `d` int(11) NOT NULL,
  PRIMARY KEY (`a`,`b`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
mysql(root@localhost)[zz](15:18:46)>show create table t4 \G
*************************** 1. row ***************************
       Table: t4
Create Table: CREATE TABLE `t4` (
  `P_C` char(20) NOT NULL,
  `a` int(11) DEFAULT NULL,
  `b` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`P_C`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
1 row in set (0.00 sec)

    ```
    
* 表数据

    ``` sql
mysql(root@localhost)[zz](15:18:50)>select * from t1;
+--------------------+------+---+
| a                  | b    | c |
+--------------------+------+---+
| aaaaaaaa           | 12ab | 1 |
| aaaaaaaa           | 12ab | 1 |
| bbbbbbbb           | tra3 | 2 |
| 123abcdree         | dddd | 4 |
| aaaaeett123abcdree | deee | 5 |
+--------------------+------+---+
5 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:19:51)>select * from t2;
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
|  6 | aaaaa |    1 | addraddraddr |
|  7 | aaaaa |    1 | addraddraddr |
|  8 | aaaaa |    1 | addraddraddr |
|  9 | aaaaa |    1 | addraddraddr |
+----+-------+------+--------------+
9 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:19:54)>select * from t3;
+----------------------+-------+-------------------------+-----+
| a                    | b     | c                       | d   |
+----------------------+-------+-------------------------+-----+
| a123bceete234256dd99 | ccccc | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd99 | zh-cn | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd9g | ccccc | adkjaoiefialkdali       | 333 |
| a123bceetedddd9999gg | zh-cn | adkjaoiefialkdalifefne  | 333 |
| aaaa                 | us-en | akjfaoiefjalsidfaoie    |   1 |
| aaaa                 | zh-cn | akjfaoiefjalsidfaoie    |   1 |
| yndii123456789       | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | us-en | k12345677laidianfeofnie |  44 |
+----------------------+-------+-------------------------+-----+
9 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:19:58)>select * from t4;
+----------+------+------------+
| P_C      | a    | b          |
+----------+------+------------+
| a        | 1111 | 23         |
| ab       | 1111 | 234asdv    |
| ba       | 1111 | gggg000    |
| clsidkdk | 1111 | 678g       |
| da       | 1111 | 9amgjie    |
| e        | 1111 | 9amgjie    |
| f        | 1111 | 123        |
| z        | 1111 | 9amgji123e |
+----------+------+------------+
8 rows in set (0.00 sec)
    ```


## 验证

* sql_mode 为空

    * t1

        ```sql
mysql(root@localhost)[zz](15:25:57)>select @@sql_mode;
+------------+
| @@sql_mode |
+------------+
|            |
+------------+
1 row in set (0.00 sec)
```
        ```  
mysql(root@localhost)[zz](17:03:03)>select * from t1 where a = 0;
+--------------------+------+---+
| a                  | b    | c |
+--------------------+------+---+
| aaaaaaaa           | 12ab | 1 |
| aaaaaaaa           | 12ab | 1 |
| bbbbbbbb           | tra3 | 2 |
| aaaaeett123abcdree | deee | 5 |
+--------------------+------+---+
4 rows in set, 5 warnings (0.00 sec)
mysql(root@localhost)[zz](17:03:43)>show warnings;
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
| Level   | Code | Message                                                                                                                              |
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaaaaa                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaaaaa                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'bbbbbbbb                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: '123abcdree                                                                                      ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaeett123abcdree                                                                              ' |
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
5 rows in set (0.00 sec)
```
        ```
        mysql(root@localhost)[zz](15:25:04)>select * from t1 where a = '00';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:25:29)>select * from t1 where a = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:25:31)>select * from t1 where a = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:25:36)>select * from t1 where a = 'a0';
Empty set (0.00 sec)
```
        ```
mysql(root@localhost)[zz](15:25:42)>select * from t1 where a = -1;
Empty set, 5 warnings (0.00 sec)
mysql(root@localhost)[zz](15:25:51)>show warnings;
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
| Level   | Code | Message                                                                                                                              |
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaaaaa                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaaaaa                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'bbbbbbbb                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: '123abcdree                                                                                      ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaeett123abcdree                                                                              ' |
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
5 rows in set (0.00 sec)
```

        ```
        mysql(root@localhost)[zz](15:27:30)>select * from t1 where b = 0;
+--------------------+------+---+
| a                  | b    | c |
+--------------------+------+---+
| bbbbbbbb           | tra3 | 2 |
| 123abcdree         | dddd | 4 |
| aaaaeett123abcdree | deee | 5 |
+--------------------+------+---+
3 rows in set, 5 warnings (0.00 sec)
mysql(root@localhost)[zz](15:48:10)>select * from t1 where b = -1;
Empty set, 5 warnings (0.00 sec)
mysql(root@localhost)[zz](15:48:22)>show warnings;
+---------+------+--------------------------------------------------+
| Level   | Code | Message                                          |
+---------+------+--------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: '12ab        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: '12ab        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'tra3        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'dddd        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'deee        ' |
+---------+------+--------------------------------------------------+
5 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:48:29)>select * from t1 where b = 2;
Empty set, 5 warnings (0.00 sec)
mysql(root@localhost)[zz](15:48:34)>show warnings;
+---------+------+--------------------------------------------------+
| Level   | Code | Message                                          |
+---------+------+--------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: '12ab        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: '12ab        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'tra3        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'dddd        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'deee        ' |
+---------+------+--------------------------------------------------+
5 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:48:40)>select * from t1 where b = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:48:56)>select * from t1 where b = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:49:00)>select * from t1 where b = '123';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:49:03)>select * from t1 where b = 'abc';
Empty set (0.00 sec)
        ```
        
        ```
        mysql(root@localhost)[zz](15:50:51)>select * from t1 where c =0;
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:50:59)>select * from t1 where c ='0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:51:03)>select * from t1 where c ='a';
Empty set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](15:51:07)>show warnings;
+---------+------+---------------------------------------+
| Level   | Code | Message                               |
+---------+------+---------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a' |
+---------+------+---------------------------------------+
1 row in set (0.00 sec)
        
        ```
  
    * t2

        ```
        mysql(root@localhost)[zz](15:52:35)>select * from t2 where id =0;
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:52:43)>select * from t2 where id ='a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:52:48)>select * from t2 where id ='0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:52:53)>select * from t2 where name = 0;
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
|  6 | aaaaa |    1 | addraddraddr |
|  7 | aaaaa |    1 | addraddraddr |
|  8 | aaaaa |    1 | addraddraddr |
|  9 | aaaaa |    1 | addraddraddr |
+----+-------+------+--------------+
9 rows in set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:53:00)>select * from t2 where name = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:53:10)>select * from t2 where name = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:53:12)>select * from t2 where sexy =0;
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
+----+-------+------+--------------+
5 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:53:34)>select * from t2 where sexy =-1;
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:53:37)>select * from t2 where sexy ='a';
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
+----+-------+------+--------------+
5 rows in set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](15:53:41)>select * from t2 where sexy ='b';
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
+----+-------+------+--------------+
5 rows in set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](15:53:45)>select * from t2 where sexy ='ab';
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
+----+-------+------+--------------+
5 rows in set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](15:53:48)>select * from t2 where sexy ='tttt';
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
+----+-------+------+--------------+
5 rows in set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](15:53:56)>select * from t2 where addr = 0;
+----+-------+------+--------------+
| id | name  | sexy | addr         |
+----+-------+------+--------------+
|  1 | aaaaa |    0 | addraddraddr |
|  2 | aaaaa |    0 | addraddraddr |
|  3 | aaaaa |    0 | addraddraddr |
|  4 | aaaaa |    0 | addraddraddr |
|  5 | aaaaa |    0 | addraddraddr |
|  6 | aaaaa |    1 | addraddraddr |
|  7 | aaaaa |    1 | addraddraddr |
|  8 | aaaaa |    1 | addraddraddr |
|  9 | aaaaa |    1 | addraddraddr |
+----+-------+------+--------------+
9 rows in set, 9 warnings (0.01 sec)
mysql(root@localhost)[zz](15:54:10)>select * from t2 where addr = 1;
Empty set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:54:15)>show warnings;
+---------+------+--------------------------------------------------+
| Level   | Code | Message                                          |
+---------+------+--------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'addraddraddr' |
+---------+------+--------------------------------------------------+
9 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:54:20)>select * from t2 where addr = 'a';
Empty set (0.00 sec)
        ```

    
    * t3

        ```
        mysql(root@localhost)[zz](15:56:34)>select * from t3 where a = 0;
+----------------------+-------+-------------------------+-----+
| a                    | b     | c                       | d   |
+----------------------+-------+-------------------------+-----+
| a123bceete234256dd99 | ccccc | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd99 | zh-cn | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd9g | ccccc | adkjaoiefialkdali       | 333 |
| a123bceetedddd9999gg | zh-cn | adkjaoiefialkdalifefne  | 333 |
| aaaa                 | us-en | akjfaoiefjalsidfaoie    |   1 |
| aaaa                 | zh-cn | akjfaoiefjalsidfaoie    |   1 |
| yndii123456789       | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | us-en | k12345677laidianfeofnie |  44 |
+----------------------+-------+-------------------------+-----+
9 rows in set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:56:50)>select * from t3 where a = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:56:54)>select * from t3 where a = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:56:57)>select * from t3 where a = '11';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:57:01)>select * from t3 where a = 1;
Empty set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:57:09)>show warnings;
+---------+------+--------------------------------------------------------------------------------------------------+
| Level   | Code | Message                                                                                          |
+---------+------+--------------------------------------------------------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a123bceete234256dd99                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a123bceete234256dd99                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a123bceete234256dd9g                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a123bceetedddd9999gg                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaa                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaa                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'yndii123456789                                              ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'yndii1234567890p                                            ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'yndii1234567890p                                            ' |
+---------+------+--------------------------------------------------------------------------------------------------+
9 rows in set (0.00 sec)
mysql(root@localhost)[zz](15:57:14)>select * from t3 where a = -1;
Empty set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:57:18)>select * from t3 where b = -1; 
Empty set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:57:28)>select * from t3 where b = 0;
+----------------------+-------+-------------------------+-----+
| a                    | b     | c                       | d   |
+----------------------+-------+-------------------------+-----+
| a123bceete234256dd99 | ccccc | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd99 | zh-cn | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd9g | ccccc | adkjaoiefialkdali       | 333 |
| a123bceetedddd9999gg | zh-cn | adkjaoiefialkdalifefne  | 333 |
| aaaa                 | us-en | akjfaoiefjalsidfaoie    |   1 |
| aaaa                 | zh-cn | akjfaoiefjalsidfaoie    |   1 |
| yndii123456789       | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | us-en | k12345677laidianfeofnie |  44 |
+----------------------+-------+-------------------------+-----+
9 rows in set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:57:30)>select * from t3 where b = 1;
Empty set, 9 warnings (0.00 sec)
mysql(root@localhost)[zz](15:57:33)>select * from t3 where b = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:57:39)>select * from t3 where c = 0;
+----------------------+-------+-------------------------+-----+
| a                    | b     | c                       | d   |
+----------------------+-------+-------------------------+-----+
| a123bceete234256dd99 | ccccc | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd99 | zh-cn | adkjaoiefialkdalifefne  | 333 |
| a123bceete234256dd9g | ccccc | adkjaoiefialkdali       | 333 |
| a123bceetedddd9999gg | zh-cn | adkjaoiefialkdalifefne  | 333 |
| aaaa                 | us-en | akjfaoiefjalsidfaoie    |   1 |
| aaaa                 | zh-cn | akjfaoiefjalsidfaoie    |   1 |
| yndii123456789       | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | bcdes | k12345677laidianfeofnie |  44 |
| yndii1234567890p     | us-en | k12345677laidianfeofnie |  44 |
+----------------------+-------+-------------------------+-----+
9 rows in set, 9 warnings (0.01 sec)
mysql(root@localhost)[zz](15:57:52)>select * from t3 where c = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:57:55)>select * from t3 where c = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:57:58)>select * from t3 where d = 0 ;
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:58:06)>select * from t3 where d = '0' ;
Empty set (0.00 sec)
mysql(root@localhost)[zz](15:58:11)>select * from t3 where d = 'a' ;
Empty set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](15:58:13)>show warnings;
+---------+------+---------------------------------------+
| Level   | Code | Message                               |
+---------+------+---------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a' |
+---------+------+---------------------------------------+
1 row in set (0.00 sec)

        ```

    * t4

        ```
        mysql(root@localhost)[zz](15:59:58)>select * from t4 where P_C =0;
+----------+------+------------+
| P_C      | a    | b          |
+----------+------+------------+
| a        | 1111 | 23         |
| ab       | 1111 | 234asdv    |
| ba       | 1111 | gggg000    |
| clsidkdk | 1111 | 678g       |
| da       | 1111 | 9amgjie    |
| e        | 1111 | 9amgjie    |
| f        | 1111 | 123        |
| z        | 1111 | 9amgji123e |
+----------+------+------------+
8 rows in set, 8 warnings (0.00 sec)
mysql(root@localhost)[zz](16:06:12)>select * from t4 where P_C ='0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:06:21)>select * from t4 where P_C ='a';
+-----+------+------+
| P_C | a    | b    |
+-----+------+------+
| a   | 1111 | 23   |
+-----+------+------+
1 row in set (0.00 sec)
mysql(root@localhost)[zz](16:06:27)>select * from t4 where P_C ='ab';
+-----+------+---------+
| P_C | a    | b       |
+-----+------+---------+
| ab  | 1111 | 234asdv |
+-----+------+---------+
1 row in set (0.00 sec)
mysql(root@localhost)[zz](16:06:38)>select * from t4 where P_C ='abc';
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:06:49)>select * from t4 where P_C =-1;
Empty set, 8 warnings (0.00 sec)
mysql(root@localhost)[zz](16:06:54)>show warnings;
+---------+------+--------------------------------------------------------------------------------------------------+
| Level   | Code | Message                                                                                          |
+---------+------+--------------------------------------------------------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a                                                           ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'ab                                                          ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'ba                                                          ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'clsidkdk                                                    ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'da                                                          ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'e                                                           ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'f                                                           ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'z                                                           ' |
+---------+------+--------------------------------------------------------------------------------------------------+
8 rows in set (0.00 sec)
mysql(root@localhost)[zz](16:06:58)>select * from t4 where a =-1;   
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:07:08)>select * from t4 where a = 0;
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:07:13)>select * from t4 where a = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:07:17)>select * from t4 where a = 'a';
Empty set, 1 warning (0.00 sec)
mysql(root@localhost)[zz](16:07:33)>show warnings;
+---------+------+---------------------------------------+
| Level   | Code | Message                               |
+---------+------+---------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'a' |
+---------+------+---------------------------------------+
1 row in set (0.00 sec)
mysql(root@localhost)[zz](16:07:38)>select * from t4 where a = 1111;
+----------+------+------------+
| P_C      | a    | b          |
+----------+------+------------+
| a        | 1111 | 23         |
| ab       | 1111 | 234asdv    |
| ba       | 1111 | gggg000    |
| clsidkdk | 1111 | 678g       |
| da       | 1111 | 9amgjie    |
| e        | 1111 | 9amgjie    |
| f        | 1111 | 123        |
| z        | 1111 | 9amgji123e |
+----------+------+------------+
8 rows in set (0.00 sec)
mysql(root@localhost)[zz](16:07:44)>select * from t4 where b = 0;
+-----+------+---------+
| P_C | a    | b       |
+-----+------+---------+
| ba  | 1111 | gggg000 |
+-----+------+---------+
1 row in set, 6 warnings (0.00 sec)
mysql(root@localhost)[zz](16:07:52)>select * from t4 where b = '0';
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:07:58)>select * from t4 where b = 'a';
Empty set (0.00 sec)
mysql(root@localhost)[zz](16:08:01)>select * from t4 where b = 23;
+-----+------+------+
| P_C | a    | b    |
+-----+------+------+
| a   | 1111 | 23   |
+-----+------+------+
1 row in set, 6 warnings (0.00 sec)
mysql(root@localhost)[zz](16:08:16)>select * from t4 where b = 523;
Empty set, 6 warnings (0.00 sec)
mysql(root@localhost)[zz](16:08:21)>show warnings;
+---------+------+------------------------------------------------+
| Level   | Code | Message                                        |
+---------+------+------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: '234asdv'    |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'gggg000'    |
| Warning | 1292 | Truncated incorrect DOUBLE value: '678g'       |
| Warning | 1292 | Truncated incorrect DOUBLE value: '9amgjie'    |
| Warning | 1292 | Truncated incorrect DOUBLE value: '9amgjie'    |
| Warning | 1292 | Truncated incorrect DOUBLE value: '9amgji123e' |
+---------+------+------------------------------------------------+
6 rows in set (0.00 sec)
        ```
    

* sql_mode 严格模式

    ```sql
    mysql(root@localhost)[zz](17:05:45)>select @@sql_mode;
+------------------------------------------------------------------------------------------------------------------------------------------+
| @@sql_mode                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------+
| STRICT_TRANS_TABLES,STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
mysql(root@localhost)[zz](17:05:39)>select * from t1 where a = 0;
+--------------------+------+---+
| a                  | b    | c |
+--------------------+------+---+
| aaaaaaaa           | 12ab | 1 |
| aaaaaaaa           | 12ab | 1 |
| bbbbbbbb           | tra3 | 2 |
| aaaaeett123abcdree | deee | 5 |
+--------------------+------+---+
4 rows in set, 5 warnings (0.00 sec)
mysql(root@localhost)[zz](17:05:42)>show warnings;
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
| Level   | Code | Message                                                                                                                              |
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaaaaa                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaaaaa                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'bbbbbbbb                                                                                        ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: '123abcdree                                                                                      ' |
| Warning | 1292 | Truncated incorrect DOUBLE value: 'aaaaeett123abcdree                                                                              ' |
+---------+------+--------------------------------------------------------------------------------------------------------------------------------------+
5 rows in set (0.00 sec)
    ```
**sql_mode 无影响**

## 隐式类型转换
* 官方文档解释

```
   The following rules describe how conversion occurs for comparison operations:

If one or both arguments are NULL, the result of the comparison is NULL, except for the NULL-safe <=> equality comparison operator. For NULL <=> NULL, the result is true. No conversion is needed.

If both arguments in a comparison operation are strings, they are compared as strings.

If both arguments are integers, they are compared as integers.

Hexadecimal values are treated as binary strings if not compared to a number.

If one of the arguments is a TIMESTAMP or DATETIME column and the other argument is a constant, the constant is converted to a timestamp before the comparison is performed. This is done to be more ODBC-friendly. This is not done for the arguments to IN(). To be safe, always use complete datetime, date, or time strings when doing comparisons. For example, to achieve best results when using BETWEEN with date or time values, use CAST() to explicitly convert the values to the desired data type.

A single-row subquery from a table or tables is not considered a constant. For example, if a subquery returns an integer to be compared to a DATETIME value, the comparison is done as two integers. The integer is not converted to a temporal value. To compare the operands as DATETIME values, use CAST() to explicitly convert the subquery value to DATETIME.

If one of the arguments is a decimal value, comparison depends on the other argument. The arguments are compared as decimal values if the other argument is a decimal or integer value, or as floating-point values if the other argument is a floating-point value.

In all other cases, the arguments are compared as floating-point (real) numbers.

For information about conversion of values from one temporal type to another, see Section 11.3.7, “Conversion Between Date and Time Types”.

Comparison of JSON values takes place at two levels. The first level of comparison is based on the JSON types of the compared values. If the types differ, the comparison result is determined solely by which type has higher precedence. If the two values have the same JSON type, a second level of comparison occurs using type-specific rules. For comparison of JSON and non-JSON values, the non-JSON value is converted to JSON and the values compared as JSON values. For details, see Comparison and Ordering of JSON Values.
```


* 如果字符串的第一个字符就是非数字的字符，那么转换为数字就是0
* 如果字符串以数字开头
    * 如果字符串中都是数字，那么转换为数字就是整个字符串对应的数字
    * 如果字符串中存在非数字，那么转换为的数字就是开头的那些数字对应的值



### references

[https://dev.mysql.com/doc/refman/5.7/en/type-conversion.html](https://dev.mysql.com/doc/refman/5.7/en/type-conversion.html)

[https://dev.mysql.com/doc/refman/5.7/en/cast-functions.html](https://dev.mysql.com/doc/refman/5.7/en/cast-functions.html)

[https://www.cnblogs.com/rollenholt/p/5442825.html](https://www.cnblogs.com/rollenholt/p/5442825.html)

