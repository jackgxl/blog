# MySQL恢复root用户超级权限

1、配置文件添加

```
skip-grant-tables
```

2、重启MySQL服务，无密码登录。手动修改用户权限。

```
update mysql.user set Grant_priv='Y',Super_priv='Y' where User='root' ;
```

```sql
UPDATE `mysql`.`user` 
SET `Select_priv` = 'Y',
`Insert_priv` = 'Y',
`Update_priv` = 'Y',
`Delete_priv` = 'Y',
`Create_priv` = 'Y',
`Drop_priv` = 'Y',
`Reload_priv` = 'Y',
`Shutdown_priv` = 'Y',
`Process_priv` = 'Y',
`File_priv` = 'Y',
`Grant_priv` = 'Y',
`References_priv` = 'Y',
`Index_priv` = 'Y',
`Alter_priv` = 'Y',
`Show_db_priv` = 'Y',
`Super_priv` = 'Y',
`Create_tmp_table_priv` = 'Y',
`Lock_tables_priv` = 'Y',
`Execute_priv` = 'Y',
`Repl_slave_priv` = 'Y',
`Repl_client_priv` = 'Y',
`Create_view_priv` = 'Y',
`Show_view_priv` = 'Y',
`Create_routine_priv` = 'Y',
`Alter_routine_priv` = 'Y',
`Create_user_priv` = 'Y',
`Event_priv` = 'Y',
`Trigger_priv` = 'Y',
`Create_tablespace_priv` = 'Y',
`ssl_type` = '',
`ssl_cipher` = '',
`x509_issuer` = '',
`x509_subject` = '',
`max_questions` = 0,
`max_updates` = 0,
`max_connections` = 0,
`max_user_connections` = 0,
`account_locked` = 'N' 
WHERE
	`Host` = 'localhost' 
	AND `User` = 'root';
```

3、刷新缓冲区

```
flush privileges;
```

4、注销skip-grant-tables配置，重启MySQL

5、授权
```
grant all on *.* to root@'localhost' with grant option;
```

6、查看用户权限

```
select * from mysql.user ;
```
