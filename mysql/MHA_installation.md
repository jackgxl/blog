# MHA_installation

[TOC]

## 下载地址
```shell
https://github.com/yoshinorim/mha4mysql-manager/releases
```
## 环境依赖

```shell
[root@localhost ~]# cat /etc/redhat-release 
CentOS Linux release 7.3.1611 (Core) 

Install dependent Perl modules

yum install perl perl-DBD-MySQL perl-Config-Tiny perl-Log-Dispatch perl-Parallel-ForkManager perl-DBD-MySQL perl-Config-Tiny perl-Log-Dispatch perl-Parallel-ForkManager perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker perl-CPAN
```

## node节点

* node编译安装

```shell
[root@mgr1 mha4mysql-node-0.58]# perl Makefile.PL
*** Module::AutoInstall version 1.06
*** Checking for Perl dependencies...
[Core Features]
- DBI        ...loaded. (1.627)
- DBD::mysql ...loaded. (4.023)
*** Module::AutoInstall configuration finished.
Checking if your kit is complete...
Looks good
Writing Makefile for mha4mysql::node
[root@mgr1 mha4mysql-node-0.58]# make -j 8
cp bin/filter_mysqlbinlog blib/script/filter_mysqlbinlog
cp bin/apply_diff_relay_logs blib/script/apply_diff_relay_logs
cp bin/purge_relay_logs blib/script/purge_relay_logs
cp bin/save_binary_logs blib/script/save_binary_logs
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/purge_relay_logs
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/filter_mysqlbinlog
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/apply_diff_relay_logs
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/save_binary_logs
cp lib/MHA/BinlogManager.pm blib/lib/MHA/BinlogManager.pm
cp lib/MHA/BinlogPosFindManager.pm blib/lib/MHA/BinlogPosFindManager.pm
cp lib/MHA/BinlogPosFinderXid.pm blib/lib/MHA/BinlogPosFinderXid.pm
cp lib/MHA/BinlogHeaderParser.pm blib/lib/MHA/BinlogHeaderParser.pm
cp lib/MHA/BinlogPosFinder.pm blib/lib/MHA/BinlogPosFinder.pm
cp lib/MHA/BinlogPosFinderElp.pm blib/lib/MHA/BinlogPosFinderElp.pm
cp lib/MHA/NodeUtil.pm blib/lib/MHA/NodeUtil.pm
cp lib/MHA/SlaveUtil.pm blib/lib/MHA/SlaveUtil.pm
cp lib/MHA/NodeConst.pm blib/lib/MHA/NodeConst.pm
Manifying blib/man1/filter_mysqlbinlog.1
Manifying blib/man1/apply_diff_relay_logs.1
Manifying blib/man1/purge_relay_logs.1
Manifying blib/man1/save_binary_logs.1
[root@mgr1 mha4mysql-node-0.58]# make install
Installing /usr/local/share/perl5/MHA/BinlogManager.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFindManager.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFinderXid.pm
Installing /usr/local/share/perl5/MHA/BinlogHeaderParser.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFinder.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFinderElp.pm
Installing /usr/local/share/perl5/MHA/NodeUtil.pm
Installing /usr/local/share/perl5/MHA/SlaveUtil.pm
Installing /usr/local/share/perl5/MHA/NodeConst.pm
Installing /usr/local/share/man/man1/filter_mysqlbinlog.1
Installing /usr/local/share/man/man1/apply_diff_relay_logs.1
Installing /usr/local/share/man/man1/purge_relay_logs.1
Installing /usr/local/share/man/man1/save_binary_logs.1
Installing /usr/local/bin/save_binary_logs
Installing /usr/local/bin/purge_relay_logs
Installing /usr/local/bin/apply_diff_relay_logs
Installing /usr/local/bin/filter_mysqlbinlog
Appending installation info to /usr/lib64/perl5/perllocal.pod
[root@mgr1 mha4mysql-node-0.58]# 
```
* 验证安装

```shell
[root@mgr1 ~]# purge_relay_logs --version
purge_relay_logs version 0.58.
```



## manager节点

* node编译安装

```shell
[root@localhost mnt]# ls
mha4mysql-manager-0.58  mha4mysql-manager-0.58.tar.gz  mha4mysql-node-0.58  mha4mysql-node-0.58.tar.gz
[root@localhost mnt]# cd mha4mysql-node-0.58
[root@localhost mha4mysql-node-0.58]# ll
total 40
-rw-r--r-- 1 mockbuild mockbuild    78 Mar 23 05:53 AUTHORS
drwxr-xr-x 2 mockbuild mockbuild   105 Mar 23 06:03 bin
-rw-r--r-- 1 mockbuild mockbuild 17987 Mar 23 05:53 COPYING
drwxr-xr-x 2 mockbuild mockbuild    77 Mar 23 06:03 debian
drwxr-xr-x 3 mockbuild mockbuild    19 Mar 23 06:03 inc
drwxr-xr-x 3 mockbuild mockbuild    16 Mar 23 06:03 lib
-rwxr-xr-x 1 mockbuild mockbuild   704 Mar 23 05:53 Makefile.PL
-rw-r--r-- 1 mockbuild mockbuild   877 Mar 23 05:53 MANIFEST
-rw-r--r-- 1 mockbuild mockbuild   533 Mar 23 06:00 META.yml
-rw-r--r-- 1 mockbuild mockbuild   288 Mar 23 05:53 README
drwxr-xr-x 2 mockbuild mockbuild    31 Mar 23 06:03 rpm
drwxr-xr-x 2 mockbuild mockbuild    47 Mar 23 06:03 t
[root@localhost mha4mysql-node-0.58]# perl Makefile.PL
*** Module::AutoInstall version 1.06
*** Checking for Perl dependencies...
[Core Features]
- DBI        ...loaded. (1.627)
- DBD::mysql ...loaded. (4.023)
*** Module::AutoInstall configuration finished.
Checking if your kit is complete...
Looks good
Writing Makefile for mha4mysql::node
[root@localhost mha4mysql-node-0.58]# make -j 8
cp bin/filter_mysqlbinlog blib/script/filter_mysqlbinlog
cp bin/apply_diff_relay_logs blib/script/apply_diff_relay_logs
cp bin/purge_relay_logs blib/script/purge_relay_logs
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/filter_mysqlbinlog
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/apply_diff_relay_logs
cp bin/save_binary_logs blib/script/save_binary_logs
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/purge_relay_logs
/usr/bin/perl "-Iinc" -MExtUtils::MY -e 'MY->fixin(shift)' -- blib/script/save_binary_logs
cp lib/MHA/BinlogManager.pm blib/lib/MHA/BinlogManager.pm
cp lib/MHA/BinlogPosFindManager.pm blib/lib/MHA/BinlogPosFindManager.pm
cp lib/MHA/BinlogPosFinderXid.pm blib/lib/MHA/BinlogPosFinderXid.pm
cp lib/MHA/BinlogHeaderParser.pm blib/lib/MHA/BinlogHeaderParser.pm
cp lib/MHA/BinlogPosFinder.pm blib/lib/MHA/BinlogPosFinder.pm
cp lib/MHA/BinlogPosFinderElp.pm blib/lib/MHA/BinlogPosFinderElp.pm
cp lib/MHA/NodeUtil.pm blib/lib/MHA/NodeUtil.pm
cp lib/MHA/SlaveUtil.pm blib/lib/MHA/SlaveUtil.pm
cp lib/MHA/NodeConst.pm blib/lib/MHA/NodeConst.pm
Manifying blib/man1/filter_mysqlbinlog.1
Manifying blib/man1/apply_diff_relay_logs.1
Manifying blib/man1/purge_relay_logs.1
Manifying blib/man1/save_binary_logs.1
[root@localhost mha4mysql-node-0.58]# sudo make install
Installing /usr/local/share/perl5/MHA/BinlogManager.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFindManager.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFinderXid.pm
Installing /usr/local/share/perl5/MHA/BinlogHeaderParser.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFinder.pm
Installing /usr/local/share/perl5/MHA/BinlogPosFinderElp.pm
Installing /usr/local/share/perl5/MHA/NodeUtil.pm
Installing /usr/local/share/perl5/MHA/SlaveUtil.pm
Installing /usr/local/share/perl5/MHA/NodeConst.pm
Installing /usr/local/share/man/man1/filter_mysqlbinlog.1
Installing /usr/local/share/man/man1/apply_diff_relay_logs.1
Installing /usr/local/share/man/man1/purge_relay_logs.1
Installing /usr/local/share/man/man1/save_binary_logs.1
Installing /usr/local/bin/filter_mysqlbinlog
Installing /usr/local/bin/apply_diff_relay_logs
Installing /usr/local/bin/purge_relay_logs
Installing /usr/local/bin/save_binary_logs
Appending installation info to /usr/lib64/perl5/perllocal.pod
[root@localhost mha4mysql-node-0.58]# 
```


* manager编译安装

```shell
[root@localhost mha4mysql-manager-0.58]# perl Makefile.PL
*** Module::AutoInstall version 1.06
*** Checking for Perl dependencies...
[Core Features]
- DBI                   ...loaded. (1.627)
- DBD::mysql            ...loaded. (4.023)
- Time::HiRes           ...loaded. (1.9725)
- Config::Tiny          ...loaded. (2.14)
- Log::Dispatch         ...missing.
- Parallel::ForkManager ...missing.
- MHA::NodeConst        ...missing.
==> Auto-install the 3 mandatory module(s) from CPAN? [y] y
*** Dependencies will be installed the next time you type 'make'.
*** Module::AutoInstall configuration finished.
Checking if your kit is complete...
Looks good
Warning: prerequisite Log::Dispatch 0 not found.
Warning: prerequisite MHA::NodeConst 0 not found.
Warning: prerequisite Parallel::ForkManager 0 not found.
Writing Makefile for mha4mysql::manager
[root@localhost mha4mysql-manager-0.58]# echo $?
0
```

```shell
make

[root@localhost mha4mysql-manager-0.58]# make
/usr/bin/perl "-Iinc" Makefile.PL --config= --installdeps=Log::Dispatch,0,Parallel::ForkManager,0,MHA::NodeConst,0
*** Installing dependencies...
*** Installing Log::Dispatch...

CPAN.pm requires configuration, but most of it can be done automatically.
If you answer 'no' below, you will enter an interactive dialog for each
configuration option instead.

Would you like to configure as much as possible automatically? [yes] yes

 <install_help>

Warning: You do not have write permission for Perl library directories.

To install modules, you need to configure a local Perl library directory or
escalate your privileges.  CPAN can help you by bootstrapping the local::lib
module or by configuring itself to use 'sudo' (if available).  You may also
resolve this problem manually if you need to customize your setup.

What approach do you want?  (Choose 'local::lib', 'sudo' or 'manual')
 [local::lib] 

Autoconfigured everything but 'urllist'.

Now you need to choose your CPAN mirror sites.  You can let me
pick mirrors for you, you can select them from a list or you
can enter them by hand.

Would you like me to automatically choose some CPAN mirror
sites for you? (This means connecting to the Internet) [yes] yes
Trying to fetch a mirror list from the Internet
Fetching with HTTP::Tiny:
http://www.perl.org/CPAN/MIRRORED.BY
HTTP::Tiny failed with an internal error: IO::Socket::SSL 1.42 must be installed for https support

Fetching with HTTP::Tiny:
http://www.perl.org/CPAN/MIRRORED.BY.gz
HTTP::Tiny failed with an internal error: IO::Socket::SSL 1.42 must be installed for https support

Fetching with Net::FTP:
ftp://ftp.perl.org/pub/CPAN/MIRRORED.BY
......

```

```shell
[root@localhost mha4mysql-manager-0.58]# make install
/usr/bin/perl "-Iinc" Makefile.PL --config= --installdeps=Log::Dispatch,0,Parallel::ForkManager,0,MHA::NodeConst,0
*** Installing dependencies...
*** Installing MHA::NodeConst...
Reading '/root/.cpan/Metadata'
  Database was generated on Fri, 10 Aug 2018 03:54:19 GMT
*** Could not find a version 0 or above for MHA::NodeConst; skipping.
*** Module::AutoInstall installation finished.
Installing /usr/local/share/perl5/MHA/ManagerUtil.pm
Installing /usr/local/share/perl5/MHA/Config.pm
Installing /usr/local/share/perl5/MHA/HealthCheck.pm
Installing /usr/local/share/perl5/MHA/ServerManager.pm
Installing /usr/local/share/perl5/MHA/ManagerConst.pm
Installing /usr/local/share/perl5/MHA/FileStatus.pm
Installing /usr/local/share/perl5/MHA/ManagerAdmin.pm
Installing /usr/local/share/perl5/MHA/ManagerAdminWrapper.pm
Installing /usr/local/share/perl5/MHA/MasterFailover.pm
Installing /usr/local/share/perl5/MHA/MasterRotate.pm
Installing /usr/local/share/perl5/MHA/MasterMonitor.pm
Installing /usr/local/share/perl5/MHA/Server.pm
Installing /usr/local/share/perl5/MHA/SSHCheck.pm
Installing /usr/local/share/perl5/MHA/DBHelper.pm
Installing /usr/local/share/man/man1/masterha_stop.1
Installing /usr/local/share/man/man1/masterha_conf_host.1
Installing /usr/local/share/man/man1/masterha_check_repl.1
Installing /usr/local/share/man/man1/masterha_check_status.1
Installing /usr/local/share/man/man1/masterha_master_monitor.1
Installing /usr/local/share/man/man1/masterha_check_ssh.1
Installing /usr/local/share/man/man1/masterha_master_switch.1
Installing /usr/local/share/man/man1/masterha_secondary_check.1
Installing /usr/local/share/man/man1/masterha_manager.1
Installing /usr/local/bin/masterha_stop
Installing /usr/local/bin/masterha_conf_host
Installing /usr/local/bin/masterha_check_repl
Installing /usr/local/bin/masterha_check_status
Installing /usr/local/bin/masterha_master_monitor
Installing /usr/local/bin/masterha_check_ssh
Installing /usr/local/bin/masterha_master_switch
Installing /usr/local/bin/masterha_secondary_check
Installing /usr/local/bin/masterha_manager
Appending installation info to /usr/lib64/perl5/perllocal.pod
```

* 验证安装

```shell
[root@localhost mha4mysql-node-0.58]# masterha_manager --version
masterha_manager version 0.58.
```


## 错误

```
安装出现问题1
[root@localhost mha4mysql-manager-0.58]# perl Makefile.PL
*** Module::AutoInstall version 1.06
*** Checking for Perl dependencies...
Can't locate CPAN.pm in @INC (@INC contains: inc /usr/local/lib64/perl5 /usr/local/share/perl5 /usr/lib64/perl5/vendor_perl /usr/share/perl5/vendor_perl /usr/lib64/perl5 /usr/share/perl5 .) at inc/Module/AutoInstall.pm line 304.

解决步骤：
yum update perl
继续解决问题1
yum install -y rrdtool perl-rrdtool rrdtool-devel perl-Params-Validate
继续解决问题1
yum install perl-DBD-MySQL perl-Config-Tiny perl-Log-Dispatch perl-Parallel-ForkManager perl-ExtUtils-CBuilder perl-ExtUtils-MakeMaker perl-CPAN
问题1 解决
```




## 参考

[github\_wiki](https://github.com/yoshinorim/mha4mysql-manager/wiki)

[https://www.cnblogs.com/wingsless/p/4033093.html](https://www.cnblogs.com/wingsless/p/4033093.html)

[https://blog.csdn.net/qq_34605594/article/details/77387872](https://blog.csdn.net/qq_34605594/article/details/77387872)

## YUM安装

```
yum install perl-Config-Tiny perl-Log-Dispatch perl-Parallel-ForkManager perl-Time-HiRes

wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum install epel-release-latest-7.noarch.rpm

wget https://github.com/yoshinorim/mha4mysql-node/releases/download/v0.58/mha4mysql-node-0.58-0.el7.centos.noarch.rpm

wget https://github.com/yoshinorim/mha4mysql-manager/releases/download/v0.58/mha4mysql-manager-0.58-0.el7.centos.noarch.rpm

yum install mha4mysql-node-0.58-0.el7.centos.noarch.rpm mha4mysql-manager-0.58-0.el7.centos.noarch.rpm -y
```