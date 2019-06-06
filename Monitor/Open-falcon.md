# Open-falcon

## 部署监控主机

## 准备环境

```
[root@local-153 open-falcon]# go version  
go version go1.11.5 linux/amd64

设置GOPATH

[root@local-153 open-falcon]# go env
GOARCH="amd64"
GOBIN=""
GOCACHE="/root/.cache/go-build"
GOEXE=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOOS="linux"
GOPATH="/data/backup/go_workspace"
GOPROXY=""
GORACE=""
GOROOT="/usr/lib/golang"
GOTMPDIR=""
GOTOOLDIR="/usr/lib/golang/pkg/tool/linux_amd64"
GCCGO="gccgo"
CC="gcc"
CXX="g++"
CGO_ENABLED="1"
GOMOD=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build256281559=/tmp/go-build -gno-record-gcc-switches"
[root@local-153 open-falcon]# mkdir -pv /data/backup/go_workspace/src

```

下载open-falcon

```
[root@local-153 go_workspace]# cd src/
[root@local-153 src]#  git clone https://github.com/open-falcon/falcon-plus.git
```

安装MySQL和Redis

```
nil
```

初始化数据库

```
cd falcon-plus/scripts/mysql/db_schema/
/usr/local/mysql3306/bin/mysql -h 192.168.64.160 -P 3308 -uroot -p123456 <1_uic-db-schema.sql 
/usr/local/mysql3306/bin/mysql -h 192.168.64.160 -P 3308 -uroot -p123456 
/usr/local/mysql3306/bin/mysql -h 192.168.64.160 -P 3308 -uroot -p123456 < 2_portal-db-schema.sql 
/usr/local/mysql3306/bin/mysql -h 192.168.64.160 -P 3308 -uroot -p123456 < 3_dashboard-db-schema.sql 
/usr/local/mysql3306/bin/mysql -h 192.168.64.160 -P 3308 -uroot -p123456 < 4_graph-db-schema.sql 
/usr/local/mysql3306/bin/mysql -h 192.168.64.160 -P 3308 -uroot -p123456 < 5_alarms-db-schema.sql 
```

编译open-falcon

```
make all
make agent
make pack
```



解压安装

```
mv open-falcon-v0.2.1.tar.gz /data/backup/
cd /data/backup/
mkdir -p /data/open-falcon
tar -zxf open-falcon-v0.2.1.tar.gz -C /data/open-falcon
```

修改配置文件

```
[root@local-153 src]# cd /data/open-falcon
[root@local-153 open-falcon]# ls
agent  aggregator  alarm  api  data  gateway  graph  hbs  judge  nodata  open-falcon  plugin  public  transfer
[root@local-153 open-falcon]# 
```

分别修改子目录下的config文件夹中的配置文件

**数据库连接方式**

agent

```
[root@local-153 open-falcon]# cat agent/config/cfg.json 
{
    "debug": false,
    "hostname": "",
    "ip": "",
    "plugin": {
        "enabled": false,
        "dir": "./plugin",
        "git": "https://github.com/open-falcon/plugin.git",
        "logs": "./logs"
    },
    "heartbeat": {
        "enabled": true,
        "addr": "192.168.64.153:6030",
        "interval": 60,
        "timeout": 1000
    },
    "transfer": {
        "enabled": true,
        "addrs": [
            "192.168.64.153:8433"
        ],
        "interval": 60,
        "timeout": 1000
    },
    "http": {
        "enabled": true,
        "listen": ":1988",
        "backdoor": false
    },
    "collector": {
        "ifacePrefix": ["eth", "em"],
        "mountPoint": []
    },
    "default_tags": {
    },
    "ignore": {
        "cpu.busy": true,
        "df.bytes.free": true,
        "df.bytes.total": true,
        "df.bytes.used": true,
        "df.bytes.used.percent": true,
        "df.inodes.total": true,
        "df.inodes.free": true,
        "df.inodes.used": true,
        "df.inodes.used.percent": true,
        "mem.memtotal": true,
        "mem.memused": true,
        "mem.memused.percent": true,
        "mem.memfree": true,
        "mem.swaptotal": true,
        "mem.swapused": true,
        "mem.swapfree": true
    }
}
```

aggregator

```
[root@local-153 open-falcon]# cat aggregator/config/cfg.json 
{
    "debug": true,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6055"
    },
    "database": {
        "addr": "root:123456@tcp(192.168.64.160:3308)/falcon_portal?loc=Local&parseTime=true",
        "idle": 10,
        "ids": [1, -1],
        "interval": 55
    },
    "api": {
        "connect_timeout": 500,
        "request_timeout": 2000,
        "plus_api": "http://127.0.0.1:8080",
        "plus_api_token": "default-token-used-in-server-side",
        "push_api": "http://127.0.0.1:1988/v1/push"
    }
}
```

alarm

```
[root@local-153 open-falcon]# cat alarm/config/cfg.json 
{
    "log_level": "debug",
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:9912"
    },
    "redis": {
        "addr": "192.168.64.101:63792",
        "maxIdle": 5,
        "highQueues": [
            "event:p0",
            "event:p1",
            "event:p2"
        ],
        "lowQueues": [
            "event:p3",
            "event:p4",
            "event:p5",
            "event:p6"
        ],
        "userIMQueue": "/queue/user/im",
        "userSmsQueue": "/queue/user/sms",
        "userMailQueue": "/queue/user/mail"
    },
    "api": {
        "im": "http://127.0.0.1:10086/wechat",
        "sms": "http://127.0.0.1:10086/sms",
        "mail": "http://127.0.0.1:10086/mail",
        "dashboard": "http://127.0.0.1:8081",
        "plus_api":"http://127.0.0.1:8080",
        "plus_api_token": "default-token-used-in-server-side"
    },
    "falcon_portal": {
        "addr": "root:123456@tcp(192.168.64.160:3308)/alarms?charset=utf8&loc=Asia%2FChongqing",
        "idle": 10,
        "max": 100
    },
    "worker": {
        "im": 10,
        "sms": 10,
        "mail": 50
    },
    "housekeeper": {
        "event_retention_days": 7,
        "event_delete_batch": 100
    }
}
```

api

```
[root@local-153 open-falcon]# cat api/config/cfg.json 
{
        "log_level": "debug",
        "db": {
                "falcon_portal": "root:123456@tcp(192.168.64.160:3308)/falcon_portal?charset=utf8&parseTime=True&loc=Local",
                "graph": "root:123456@tcp(192.168.64.160:3308)/graph?charset=utf8&parseTime=True&loc=Local",
                "uic": "root:123456@tcp(192.168.64.160:3308)/uic?charset=utf8&parseTime=True&loc=Local",
                "dashboard": "root:123456@tcp(192.168.64.160:3308)/dashboard?charset=utf8&parseTime=True&loc=Local",
                "alarms": "root:123456@tcp(192.168.64.160:3308)/alarms?charset=utf8&parseTime=True&loc=Local",
                "db_bug": true
        },
        "graphs": {
                "cluster": {
                        "graph-00": "127.0.0.1:6070"
                },
                "max_conns": 100,
                "max_idle": 100,
                "conn_timeout": 1000,
                "call_timeout": 5000,
                "numberOfReplicas": 500
        },
        "metric_list_file": "./api/data/metric",
        "web_port": "0.0.0.0:8080",
        "access_control": true,
        "signup_disable": true,
        "salt": "",
        "skip_auth": false,
        "default_token": "default-token-used-in-server-side",
        "gen_doc": false,
        "gen_doc_path": "doc/module.html"
}
```

gateway

```
[root@local-153 open-falcon]# cat gateway/config/cfg.json 
{
    "debug": true,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:16060"
    },
    "rpc": {
        "enabled": true,
        "listen": "0.0.0.0:18433"
    },
    "socket": {
        "enabled": true,
        "listen": "0.0.0.0:14444",
        "timeout": 3600
    },
    "transfer": {
        "enabled": true,
        "batch": 200,
        "retry": 1,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "cluster": {
            "t1":"0.0.0.0:8433"
        }
    }
}
```

graph

```
[root@local-153 open-falcon]# cat graph/config/cfg.json 
{
    "debug": true,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6071"
    },
    "rpc": {
        "enabled": true,
        "listen": "0.0.0.0:6070"
    },
    "rrd": {
        "storage": "./data/6070"
    },
    "db": {
        "dsn": "root:123456@tcp(192.168.64.160:3308)/graph?loc=Local&parseTime=true",
        "maxIdle": 4
    },
    "callTimeout": 5000,
    "ioWorkerNum": 64,
    "migrate": {
            "enabled": false,
            "concurrency": 2,
            "replicas": 500,
            "cluster": {
                    "graph-00" : "127.0.0.1:6070"
            }
    }
}
```

```
[root@local-153 open-falcon]# cat hbs/config/cfg.json 
{
    "debug": true,
    "database": "root:123456@tcp(192.168.64.160:3308)/falcon_portal?loc=Local&parseTime=true",
    "hosts": "",
    "maxConns": 20,
    "maxIdle": 15,
    "listen": ":6030",
    "trustable": [""],
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6031"
    }
}

```

judge

```
[root@local-153 open-falcon]# cat judge/config/cfg.json 
{
    "debug": true,
    "debugHost": "nil",
    "remain": 11,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6081"
    },
    "rpc": {
        "enabled": true,
        "listen": "0.0.0.0:6080"
    },
    "hbs": {
        "servers": ["0.0.0.0:6030"],
        "timeout": 300,
        "interval": 60
    },
    "alarm": {
        "enabled": true,
        "minInterval": 300,
        "queuePattern": "event:p%v",
        "redis": {
            "dsn": "127.0.0.1:6379",
            "maxIdle": 5,
            "connTimeout": 5000,
            "readTimeout": 5000,
            "writeTimeout": 5000
        }
    }
}
```

nodata

```
[root@local-153 open-falcon]# cat nodata/config/cfg.json 
{
    "debug": true,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6090"
    },
    "plus_api":{
        "connectTimeout": 500,
        "requestTimeout": 2000,
        "addr": "http://127.0.0.1:8080",
        "token": "default-token-used-in-server-side"
    },
    "config": {
        "enabled": true,
        "dsn": "root:123456@tcp(192.168.64.160:3308)/falcon_portal?loc=Local&parseTime=true&wait_timeout=604800",
        "maxIdle": 4
    },
    "collector":{
        "enabled": true,
        "batch": 200,
        "concurrent": 10
    },
    "sender":{
        "enabled": true,
        "connectTimeout": 500,
        "requestTimeout": 2000,
        "transferAddr": "0.0.0.0:6060",
        "batch": 500
    }
}
```

transfer

```
[root@local-153 open-falcon]# cat transfer/config/cfg.json 
{
    "debug": true,
    "minStep": 30,
    "http": {
        "enabled": true,
        "listen": "0.0.0.0:6060"
    },
    "rpc": {
        "enabled": true,
        "listen": "0.0.0.0:8433"
    },
    "socket": {
        "enabled": true,
        "listen": "0.0.0.0:4444",
        "timeout": 3600
    },
    "judge": {
        "enabled": true,
        "batch": 200,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "replicas": 500,
        "cluster": {
            "judge-00" : "0.0.0.0:6080"
        }
    },
    "graph": {
        "enabled": true,
        "batch": 200,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "replicas": 500,
        "cluster": {
            "graph-00" : "0.0.0.0:6070"
        }
    },
    "tsdb": {
        "enabled": false,
        "batch": 200,
        "connTimeout": 1000,
        "callTimeout": 5000,
        "maxConns": 32,
        "maxIdle": 32,
        "retry": 3,
        "address": "127.0.0.1:8088"
    }
}
```

## 启动关闭open-falcon

```
[root@local-153 open-falcon]# cd /data/open-falcon
[root@local-153 open-falcon]# ./open-falcon start
[root@local-153 open-falcon]# ./open-falcon check
        falcon-graph         UP           29682 
          falcon-hbs         UP           27851 
        falcon-judge         UP           27865 
     falcon-transfer         UP           27876 
       falcon-nodata         UP           27888 
   falcon-aggregator         UP           27900 
        falcon-agent         UP           27912 
      falcon-gateway         UP           27925 
          falcon-api         UP           28002 
        falcon-alarm         UP           27944 
[root@local-153 open-falcon]# ./open-falcon stop
```

## 部署前端

```
mkdkir -p /data/open-falcon_front
[root@local-153 data]# cd /data/open-falcon_front/
[root@local-153 open-falcon_front]# git clone https://github.com/open-falcon/dashboard.git

[root@local-153 open-falcon_front]# cd dashboard/
yum install -y python-virtualenv
yum install -y python-devel
yum install -y openldap-devel
yum install -y mysql-devel
yum groupinstall "Development tools" -y

virtualenv ./env
./env/bin/pip install -r pip_requirements.txt
```

修改rrd 配置文件

```
[root@local-153 dashboard]# cat rrd/config.py
#-*-coding:utf-8 -*-
# Copyright 2017 Xiaomi, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# app config
import os
LOG_LEVEL = os.environ.get("LOG_LEVEL",'DEBUG')
SECRET_KEY = os.environ.get("SECRET_KEY","secret-key")
PERMANENT_SESSION_LIFETIME = os.environ.get("PERMANENT_SESSION_LIFETIME",3600 * 24 * 30)
SITE_COOKIE = os.environ.get("SITE_COOKIE","open-falcon-ck")

# Falcon+ API
API_ADDR = os.environ.get("API_ADDR","http://127.0.0.1:8080/api/v1")
API_USER = os.environ.get("API_USER","admin")
API_PASS = os.environ.get("API_PASS","password")

# portal database
# TODO: read from api instead of db
PORTAL_DB_HOST = os.environ.get("PORTAL_DB_HOST","192.168.64.160")
PORTAL_DB_PORT = int(os.environ.get("PORTAL_DB_PORT",3308))
PORTAL_DB_USER = os.environ.get("PORTAL_DB_USER","root")
PORTAL_DB_PASS = os.environ.get("PORTAL_DB_PASS","123456")
PORTAL_DB_NAME = os.environ.get("PORTAL_DB_NAME","falcon_portal")

# alarm database
# TODO: read from api instead of db
ALARM_DB_HOST = os.environ.get("ALARM_DB_HOST","192.168.64.160")
ALARM_DB_PORT = int(os.environ.get("ALARM_DB_PORT",3308))
ALARM_DB_USER = os.environ.get("ALARM_DB_USER","root")
ALARM_DB_PASS = os.environ.get("ALARM_DB_PASS","123456")
ALARM_DB_NAME = os.environ.get("ALARM_DB_NAME","alarms")

# ldap config
LDAP_ENABLED = os.environ.get("LDAP_ENABLED",False)
LDAP_SERVER = os.environ.get("LDAP_SERVER","ldap.forumsys.com:389")
LDAP_BASE_DN = os.environ.get("LDAP_BASE_DN","dc=example,dc=com")
LDAP_BINDDN = os.environ.get("LDAP_BINDDN","cn=manager,dc=example,dc=org")
LDAP_BIND_PASS = os.environ.get("LDAP_BIND_PASS","password")
LDAP_SEARCH_FMT = os.environ.get("LDAP_SEARCH_FMT","uid=%s")
LDAP_ATTRS = ["cn","mail","telephoneNumber"]
LDAP_TLS_START_TLS = False
LDAP_TLS_CACERTDIR = ""
LDAP_TLS_CACERTFILE = "/etc/openldap/certs/ca.crt"
LDAP_TLS_CERTFILE = ""
LDAP_TLS_KEYFILE = ""
LDAP_TLS_REQUIRE_CERT = True
LDAP_TLS_CIPHER_SUITE = ""

# i18n
BABEL_DEFAULT_LOCALE   = 'zh_CN'
BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'
# available translations
LANGUAGES   = {
    'en':  'English',
    'zh_CN':  'Chinese-Simplified',
}

# portal site config
MAINTAINERS = ['root']
CONTACT = 'root@open-falcon.com'

DEBUG = True

try:
    from rrd.local_config import *
except:
    print "[warning] no local config file"
[root@local-153 dashboard]# 
```

开启防火墙8081端口

```
nil
```

启动关闭front

```
[root@local-153 dashboard]# bash control start
[root@local-153 dashboard]# bash control tail
[root@local-153 dashboard]# bash control stop
```

## 部署监控机器agent

## 部署myMon

## reference

[https://github.com/open-falcon]()

[https://blog.csdn.net/weixin_42509278/article/details/83061918]()

[http://book.open-falcon.org/zh_0_2/quick_install/backend.html](http://book.open-falcon.org/zh_0_2/quick_install/backend.html)

[https://github.com/open-falcon/book/blob/master/zh_0_2/SUMMARY.md]()

[https://blog.csdn.net/qq_27384769/article/details/79569776]()
