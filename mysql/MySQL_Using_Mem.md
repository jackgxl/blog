# MySQL占用内存计算
## session

```
select VARIABLE_NAME,VARIABLE_VALUE,VARIABLE_VALUE/1024/1024 as 'MB'  from performance_schema.session_variables where VARIABLE_NAME in ('sort_buffer_size','read_buffer_size','read_rnd_buffer_size','join_buffer_size','thread_stack','binlog_cache_size');
```

## global

```
select  VARIABLE_NAME,VARIABLE_VALUE, VARIABLE_VALUE/1024/1024 as 'MB' from performance_schema.global_variables where VARIABLE_NAME in ('key_buffer_size','query_cache_size','tmp_table_size','innodb_buffer_pool_size','innodb_log_buffer_size','max_connections');
```

### reference

<a>http://www.mysqlcalculator.com/
