## ngnix 安装配置
### 解决依赖关系
```
yum -y install gcc gcc-c++ autoconf automake zlib zlib-devel openssl openssl-devel pcre-devel
```
### 创建用户

```
useradd -M -s /sbin/nologin  nginx  
useradd -s /sbin/nologin -g nginx -r nginx
```

### 编译参数1

```
./configure \
--prefix=/usr \
--sbin-path=/usr/sbin/nginx \
--conf-path=/etc/nginx/nginx.conf \
--error-log-path=/var/log/nginx/error.log \
--pid-path=/var/run/nginx/nginx.pid \
--user=nginx \
--group=nginx \
--with-http_ssl_module \
--with-http_flv_module \
--with-http_gzip_static_module \
--http-log-path=/var/log/nginx/access.log \
--http-client-body-temp-path=/var/tmp/nginx/client \
--http-proxy-temp-path=/var/tmp/nginx/proxy \
--http-fastcgi-temp-path=/var/tmp/nginx/fcgi \
--with-http_stub_status_module
```

###编译参数2

```
./configure \
--prefix=/usr/local/nginx \
--conf-path=/usr/local/nginx/conf/nginx.conf \
--error-log-path=/data/log/nginx/error.log \
--pid-path=/usr/local/nginx/tmp/nginx.pid \
--user=nginx \
--group=nginx \
--with-http_ssl_module \
--with-http_flv_module \
--with-http_gzip_static_module \
--http-log-path=/data/log/nginx/access.log \
--http-client-body-temp-path=/usr/loca/nginx/tmp/client \
--http-proxy-temp-path=/usr/local/nginx/tmp/proxy \
--http-fastcgi-temp-path=/usr/local/nginx/tmp/fcgi \
--with-http_stub_status_module
```
### 编译参数3 

```
./configure \
--prefix=/usr/local/nginx \
--user=nginx \
--group=nginx \
--with-http_ssl_module \
--with-http_flv_module \
--with-http_gzip_static_module \
--with-http_stub_status_module

```
### 安装
```
make && make install
```
