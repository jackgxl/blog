# gitlab upgrade


## verson10

```
[root@NodeC backup]# gitlab-ctl stop unicorn ; gitlab-ctl stop sidekiq ; gitlab-ctl stop nginx    
ok: down: unicorn: 19s, normally up
ok: down: sidekiq: 0s, normally up
ok: down: nginx: 1s, normally up
[root@NodeC backup]# gitlab-ctl status
run: gitaly: (pid 1074) 69s; run: log: (pid 830) 48487600s
run: gitlab-monitor: (pid 1089) 69s; run: log: (pid 829) 48487600s
run: gitlab-workhorse: (pid 1092) 68s; run: log: (pid 832) 48487600s
run: logrotate: (pid 1105) 68s; run: log: (pid 831) 48487600s
down: nginx: 9s, normally up; run: log: (pid 828) 48487600s
run: node-exporter: (pid 1145) 67s; run: log: (pid 835) 48487600s
run: postgres-exporter: (pid 1153) 66s; run: log: (pid 825) 48487601s
run: postgresql: (pid 1159) 66s; run: log: (pid 817) 48487601s
run: prometheus: (pid 1161) 66s; run: log: (pid 846) 48487600s
run: redis: (pid 1172) 65s; run: log: (pid 820) 48487601s
run: redis-exporter: (pid 1190) 65s; run: log: (pid 836) 48487600s
down: sidekiq: 10s, normally up; run: log: (pid 822) 48487601s
down: unicorn: 34s, normally up; run: log: (pid 860) 48487600s
```

```
rpm -Uvh gitlab-ce-10.8.7-ce.0.el7.x86_64.rpm
```

```
vim /etc/gitlab/gitlab.rb

```

## verson11

```
gitlab-ctl stop unicorn;gitlab-ctl stop sidekiq ;gitlab-ctl stop nginx
```
```
[root@NodeC backup]# gitlab-ctl status        
run: alertmanager: (pid 12037) 327s; run: log: (pid 2968) 3099s
run: gitaly: (pid 12057) 326s; run: log: (pid 830) 48491028s
run: gitlab-monitor: (pid 12074) 326s; run: log: (pid 829) 48491028s
run: gitlab-workhorse: (pid 12078) 325s; run: log: (pid 832) 48491028s
run: logrotate: (pid 12093) 325s; run: log: (pid 831) 48491028s
down: nginx: 167s, normally up; run: log: (pid 828) 48491028s
run: node-exporter: (pid 12142) 324s; run: log: (pid 835) 48491028s
run: postgres-exporter: (pid 12148) 324s; run: log: (pid 825) 48491029s
run: postgresql: (pid 12158) 323s; run: log: (pid 817) 48491029s
run: prometheus: (pid 12161) 322s; run: log: (pid 846) 48491028s
run: redis: (pid 12191) 322s; run: log: (pid 820) 48491029s
run: redis-exporter: (pid 12343) 322s; run: log: (pid 836) 48491028s
down: sidekiq: 15s, normally up; run: log: (pid 822) 48491029s
down: unicorn: 170s, normally up; run: log: (pid 860) 48491028s
```

```
rpm -Uvh gitlab-ce-11.0.0-ce.0.el7.x86_64.rpm
```

```
gitlab-ctl restart

gitlab-ctl reconfigure
```



## 安装

### 安装依赖

```shell
yum install wget curl openssh-server openssh-clients postfix cronie policycoreutils-python patch –y

rpm -i gitlab-ce-10.0.2-ce.0.el7.x86_64.rpm

vim /etc/gitlab/gitlab.rb
gitlab-ctl reconfigure
gitlab-ctl restart
```



新版本下载（清华源更好用）

repo模式

```shell

vim /etc/yum.repo.d/gitlab-ce.repo

[gitlab-ce]
name=gitlab-ce
baseurl=http://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7
repo_gpgcheck=0
gpgcheck=0
enabled=1
gpgkey=https://packages.gitlab.com/gpg.key

yum install gitlab-ce -y

gitlab-ctl reconfigure
gitlab-ctl status
gitlab-ctl start
```

rpm模式

```shell
wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-13.9.1-ce.0.el7.x86_64.rpm
```



查看当前gitlab-ce版本号

```
yum list | grep gitlab-ce

cat /opt/gitlab/embedded/service/gitlab-rails/VERSION
```

查看gitlab状态

```
gitlab-ctl status
```

备份恢复相关

备份
```
gitlab-rake gitlab:backup:create
```
恢复

#先停止

```
gitlab-ctl stop unicorn
gitlab-ctl stop sidekiq
```

#开始恢复

```
gitlab-rake gitlab:backup:restore BACKUP=/data/gitlab/backups/1557136073_2019_05_06_11.10.4
```

恢复后检查

```
gitlab-rake gitlab:check SANITIZE=true
```

### 升级相关

关闭GitLab核心服务

10

```
gitlab-ctl stop unicorn;gitlab-ctl stop sidekicks;gitlab-ctl stop nginx
```

11

```
gitlab-ctl stop unicorn;gitlab-ctl stop sidekiq ;gitlab-ctl stop nginx
```

下载最新包

```
wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-12.9.5-ce.0.el7.x86_64.rpm

wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-10.5.0-ce.0.el7.x86_64.rpm

wget https://gitlab.com/xhang/gitlab/-/archive/10-5-stable/gitlab-10-5-stable.zip

wget https://gitlab.com/xhang/gitlab/-/archive/10-5-stable-zh/gitlab-10-5-stable-zh.zip

wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-12.0.0-ce.0.el7.x86_64.rpm

wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-11.9.9-ce.0.el7.x86_64.rpm

wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-11.0.0-ce.0.el7.x86_64.rpm


wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-10.8.7-ce.0.el7.x86_64.rpm

wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el7/gitlab-ce-12.3.9-ce.0.el7.x86_64.rpm

wget https://gitlab.com/xhang/gitlab/-/archive/12-3-stable/gitlab-12-3-stable.zip
wget https://gitlab.com/xhang/gitlab/-/archive/12-3-stable-zh/gitlab-12-3-stable-zh.zip

wget https://gitlab.com/xhang/gitlab/-/archive/10-5-stable-zh/gitlab-10-5-stable-zh.zip
```

升级

```
rpm -Uvh gitlab-ce-10.8.7-ce.0.el7.x86_64.rpm
```

重新配置

```
gitlab-ctl reconfigure
gitlab-ctl restart

```

### 汉化相关

生成汉化补丁

```shell
git clone https://gitlab.com/xhang/gitlab.git
git branch -a

git diff ${version} ${version}-zh >123.diff

gitlab-ctl stop
patch -d /opt/gitlab/embedded/service/gitlab-rails -p1 <123.diff 
gitlab-ctl start
```





停止服务

```
gitlab-ctl stop
```

汉化必须包

```
yum install git patch unzip tmux -y

//翻墙警告

git clone https://gitlab.com/xhang/gitlab.git

//gitee

https://gitee.com/panda26/gitlab?_from=gitee_search

git diff v9.0.0 v9.0.0-zh > ../9.0.0-zh.diff
```

#### 安装汉化补丁

```
sudo patch -d /opt/gitlab/embedded/service/gitlab-rails -p1 < 9.0.0-zh.diff
```

官方下载地址：

```
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/gitlab-ce-10.0.5-ce.0.el7.x86_64.rpm/download.rpm
```

#### 10最高版本

```
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/gitlab-ce-10.8.7-ce.0.el7.x86_64.rpm/download.rpm
```

#### 11最高版本

```
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/gitlab-ce-11.0.0-ce.0.el7.x86_64.rpm/download.rpm
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/el/7/gitlab-ce-11.9.9-ce.0.el7.x86_64.rpm/download.rpm
```

#### 12

```
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/ol/7/gitlab-ce-12.0.0-ce.0.el7.x86_64.rpm/download.rpm
wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/ol/7/gitlab-ce-12.5.5-ce.0.el7.x86_64.rpm/download.rpm
```



密码修改

```
gitlab-rails console -e production //进入gitlab 终端
user = User.where(id: 1).first  // 选择用户
user.password = 'secret_pass'  //修改密码
user.password_confirmation = 'secret_pass' //确认密码
user.save!	//保存密码
exit  //退出
```



#### reference

[https://www.bbsmax.com/A/Gkz1mQ1gzR/](https://www.bbsmax.com/A/Gkz1mQ1gzR/)

https://www.cnblogs.com/yanjieli/p/10605381.html

https://gitlab.com/larryli/gitlab/-/wikis/home

https://gitlab.com/xhang/gitlab/-/tree/12-3-stable-zh

https://www.cnblogs.com/nethrd/p/9408290.html

https://blog.51cto.com/12390045/2117819

https://www.bbsmax.com/A/xl567gQYdr/

[https://www.jianshu.com/p/977bc03daffb](https://www.jianshu.com/p/977bc03daffb)

[https://blog.csdn.net/A___LEi/article/details/110476531](https://blog.csdn.net/A___LEi/article/details/110476531)