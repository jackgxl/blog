# PostgreSQL 笔记

[TOC]

## psql工具

**psql工具\开头**

```shell
\?
\n?
\d
\l

postgres-# \?
General
  \copyright             show PostgreSQL usage and distribution terms
  \errverbose            show most recent error message at maximum verbosity
  \g [FILE] or ;         execute query (and send results to file or |pipe)
  \gexec                 execute query, then execute each value in its result
  \gset [PREFIX]         execute query and store results in psql variables
  \q                     quit psql
  \crosstabview [COLUMNS] execute query and display results in crosstab
  \watch [SEC]           execute query every SEC seconds

Help
  \? [commands]          show help on backslash commands
  \? options             show help on psql command-line options
  \? variables           show help on special variables
  \h [NAME]              help on syntax of SQL commands, * for all commands

Query Buffer
  \e [FILE] [LINE]       edit the query buffer (or file) with external editor
  \ef [FUNCNAME [LINE]]  edit function definition with external editor
  \ev [VIEWNAME [LINE]]  edit view definition with external editor
  \p                     show the contents of the query buffer
  \r                     reset (clear) the query buffer
  \s [FILE]              display history or save it to file
  \w FILE                write query buffer to file

Input/Output
  \copy ...              perform SQL COPY with data stream to the client host
  \echo [STRING]         write string to standard output
  \i FILE                execute commands from file
  \ir FILE               as \i, but relative to location of current script
  \o [FILE]              send all query results to file or |pipe
  \qecho [STRING]        write string to query output stream (see \o)

Informational
  (options: S = show system objects, + = additional detail)
  \d[S+]                 list tables, views, and sequences
  \d[S+]  NAME           describe table, view, sequence, or index
  \da[S]  [PATTERN]      list aggregates
  \dA[+]  [PATTERN]      list access methods
  \db[+]  [PATTERN]      list tablespaces
  \dc[S+] [PATTERN]      list conversions
  \dC[+]  [PATTERN]      list casts
  \dd[S]  [PATTERN]      show object descriptions not displayed elsewhere
  \ddp    [PATTERN]      list default privileges
  \dD[S+] [PATTERN]      list domains
  \det[+] [PATTERN]      list foreign tables
  \des[+] [PATTERN]      list foreign servers
  \deu[+] [PATTERN]      list user mappings
  \dew[+] [PATTERN]      list foreign-data wrappers
  \df[antw][S+] [PATRN]  list [only agg/normal/trigger/window] functions
  \dF[+]  [PATTERN]      list text search configurations
  \dFd[+] [PATTERN]      list text search dictionaries
  \dFp[+] [PATTERN]      list text search parsers
  \dFt[+] [PATTERN]      list text search templates
  \dg[S+] [PATTERN]      list roles
  \di[S+] [PATTERN]      list indexes
  \dl                    list large objects, same as \lo_list
  \dL[S+] [PATTERN]      list procedural languages
  \dm[S+] [PATTERN]      list materialized views
  \dn[S+] [PATTERN]      list schemas
  \do[S]  [PATTERN]      list operators
  \dO[S+] [PATTERN]      list collations
  \dp     [PATTERN]      list table, view, and sequence access privileges
  \drds [PATRN1 [PATRN2]] list per-database role settings
  \ds[S+] [PATTERN]      list sequences
  \dt[S+] [PATTERN]      list tables
  \dT[S+] [PATTERN]      list data types
  \du[S+] [PATTERN]      list roles
  \dv[S+] [PATTERN]      list views
  \dE[S+] [PATTERN]      list foreign tables
  \dx[+]  [PATTERN]      list extensions
  \dy     [PATTERN]      list event triggers
  \l[+]   [PATTERN]      list databases
  \sf[+]  FUNCNAME       show a function's definition
  \sv[+]  VIEWNAME       show a view's definition
  \z      [PATTERN]      same as \dp

Formatting
  \a                     toggle between unaligned and aligned output mode
  \C [STRING]            set table title, or unset if none
  \f [STRING]            show or set field separator for unaligned query output
  \H                     toggle HTML output mode (currently off)
  \pset [NAME [VALUE]]   set table output option
                         (NAME := {format|border|expanded|fieldsep|fieldsep_zero|footer|null|
                         numericlocale|recordsep|recordsep_zero|tuples_only|title|tableattr|pager|
                         unicode_border_linestyle|unicode_column_linestyle|unicode_header_linestyle})
  \t [on|off]            show only rows (currently off)
  \T [STRING]            set HTML <table> tag attributes, or unset if none
  \x [on|off|auto]       toggle expanded output (currently off)

Connection
  \c[onnect] {[DBNAME|- USER|- HOST|- PORT|-] | conninfo}
                         connect to new database (currently "postgres")
  \encoding [ENCODING]   show or set client encoding
  \password [USERNAME]   securely change the password for a user
  \conninfo              display information about current connection

Operating System
  \cd [DIR]              change the current working directory
  \setenv NAME [VALUE]   set or unset environment variable
  \timing [on|off]       toggle timing of commands (currently off)
  \! [COMMAND]           execute command in shell or start interactive shell

Variables
  \prompt [TEXT] NAME    prompt user to set internal variable
  \set [NAME [VALUE]]    set internal variable, or list all if no parameters
  \unset NAME            unset (delete) internal variable

Large Objects
  \lo_export LOBOID FILE
  \lo_import FILE [COMMENT]
  \lo_list
  \lo_unlink LOBOID      large object operations
  


```

```
postgres-# \db
       List of tablespaces
    Name    |  Owner   | Location 
------------+----------+----------
 pg_default | postgres | 
 pg_global  | postgres | 
(2 rows)

postgres-# \dg
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 admin     | Cannot login                                               | {}
 dml       | Cannot login                                               | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 root      |                                                            | {}
 slave     | Cannot login                                               | {}

postgres-# \dn
  List of schemas
  Name  |  Owner   
--------+----------
 public | postgres
(1 row)

postgres-# \dt
        List of relations
 Schema | Name | Type  |  Owner   
--------+------+-------+----------
 public | t1   | table | postgres
 public | t2   | table | postgres
(2 rows)

```

```
  
postgres=# \timing on
Timing is on.
postgres=# select count(*) from t1;
 count 
-------
     2
(1 row)

Time: 0.797 ms
postgres=# \timing off
Timing is off.
postgres=# select count(*) from t1;
 count 
-------
     2
(1 row)

```


查看实例中数据库情况

```sql
[postgres@localhost ~]$ /usr/local/postgresql/bin/psql --host 127.0.0.1 -p 5432 -l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 d1        | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(4 rows)
```
结果显示边界

```
postgres=# \pset border 0;  
Border style is 0.
postgres=# select * from t1;
id name 
-- ----
 1 a
 2 a
(2 rows)

postgres=# \pset border 1;  
Border style is 1.
postgres=# select * from t1;
 id | name 
----+------
  1 | a
  2 | a
(2 rows)

postgres=# \pset border 2;  
Border style is 2.
postgres=# select * from t1;
+----+------+
| id | name |
+----+------+
|  1 | a    |
|  2 | a    |
+----+------+
(2 rows)

postgres=# \pset border 3;  
Border style is 3.
postgres=# select * from t1;
+----+------+
| id | name |
+----+------+
|  1 | a    |
|  2 | a    |
+----+------+
(2 rows)

```
\x 每一行数据拆开为单列分行显示(类似MySQL \G)
```
postgres=# \x
Expanded display is on.
postgres=# select * from t1;
+-[ RECORD 1 ]-+
| id   | 1 |
| name | a |
+-[ RECORD 2 ]-+
| id   | 2 |
| name | a |
+------+---+
```
\echo 显示一行

```
postgres=# \echo hello world
hello world
postgres=# 
```

事务

```

postgres=# \set AUTOCOMMIT off
postgres=# begin;                       
BEGIN
postgres=# select * from t1;  
 id | name 
----+------
  1 | a
  2 | a
  5 | c
(3 rows)

postgres=# insert into t1 values(3,'d');
INSERT 0 1
postgres=# select * from t1;            
 id | name 
----+------
  1 | a
  2 | a
  5 | c
  3 | d
(4 rows)

postgres=# rollback ;
ROLLBACK
postgres=# insert into t1 values(6,'e');
INSERT 0 1
postgres=# select * from t1;            
 id | name 
----+------
  1 | a
  2 | a
  5 | c
  6 | e
(4 rows)

postgres=# commit ;
COMMIT
postgres=# select * from t1;
 id | name 
----+------
  1 | a
  2 | a
  5 | c
  6 | e
(4 rows)

postgres=# \set AUTOCOMMIT on
postgres=# 
```

开启psql中命令实际执行的SQL

方法一、

```sql
[postgres@localhost ~]$ /usr/local/postgresql/bin/psql --host 127.0.0.1 -p 5432 -E
```
方法二、

```sql
\set ECHO_HIDDEN [on|off]

postgres=# \dn
  List of schemas
  Name  |  Owner   
--------+----------
 public | postgres
(1 row)

postgres=# \set ECHO_HIDDEN on
postgres=# \dn
********* QUERY **********
SELECT n.nspname AS "Name",
  pg_catalog.pg_get_userbyid(n.nspowner) AS "Owner"
FROM pg_catalog.pg_namespace n
WHERE n.nspname !~ '^pg_' AND n.nspname <> 'information_schema'
ORDER BY 1;
**************************

  List of schemas
  Name  |  Owner   
--------+----------
 public | postgres
(1 row)

postgres=# \set ECHO_HIDDEN off
postgres=# \dn
  List of schemas
  Name  |  Owner   
--------+----------
 public | postgres
(1 row)
```

## 数据类型：

boolean:

| Name    | Storage Size | Description            |
|:--:|:--:|:--:|
| boolean | 1byte        | state of true or false |

Numberic Types:

|Name|Storage Size|Description|Range|
|:--:|:--:|:--:|:--:|
|smallint	|2 bytes|	small-range integer	|-32768 to +32767|
|integer    |4 bytes|typical choice for integer|-2147483648 to +2147483647|
|bigint|8 bytes|large-range integer	|-9223372036854775808 to +9223372036854775807|
|decimal|	variable|	user-specified precision, exact	|up to 131072 digits before the decimal point; up to 16383 digits after the decimal point|
|numeric|	variable	|user-specified precision, exact|	up to 131072 digits before the decimal point; up to 16383 digits after the decimal point|
|real|	4 bytes	|variable-precision, inexact|	6 decimal digits precision|
|double precision|	8 bytes	|variable-precision, inexact|	15 decimal digits precision|
|smallserial |	2 bytes	|small autoincrementing integer|	1 to 32767|
|serial |	4 bytes	|autoincrementing integer|	1 to 2147483647|
|bigserial|	8 bytes|	large autoincrementing integer|	1 to 9223372036854775807|

Monetary Types:

|Name|Storage Size| Description | Range |
|:--:|:--:|:--:|:--:|
|money|8 bytes|currency amount|-92233720368547758.08 to +92233720368547758.07|


##  逻辑结构

**锁**

* 查看锁

    ```sql
    select * from pg_locks;
    ``` 
    

## 核心架构

Postmaster 主进程

查看服务进程 pid 

```sql
select pid from pg_stat_activity ;

```

Syslogger (系统日志)进程

```
开启配置文件postgresql.conf中logging_collect设置为on
```

BgWriter(后台写)进程

WalWriter(预写式日志写)进程

PgArch(归档)进程

AutoVacuum(自动清理)进程

Pgstat(统计数据收集)进程

共享内存

本地内存

## 服务管理

* 配置文件

* 备份恢复

* 逻辑备份

    ```
    pg_dump
    pg_restore
    ```

* 物理备份
    
    ```
    Standby
    LVM
    ```

## 执行计划
* explain

```
explain (format json) select * from test;
xml
YAML
```

* 




