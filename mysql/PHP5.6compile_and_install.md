# PHP5.6编译安装
---
## 环境配置

```
yum -y install gcc gcc-c++ openssl openssl-devel curl curl-devel libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel pcre pcre-devel libxslt libxslt-devel bzip2 bzip2-devel libmcrypt libxml2-devel openssl-devel libcurl-devel libjpeg-devel libpng-devel libicu-devel openldap-devel
```

## 下载

```
下载php 5.6.30 并验证md5sum
http://php.net/get/php-5.6.30.tar.gz/from/a/mirror

```
## 解压
```
tar xf php-5.6.30.tar.gz

mkdir -p /usr/local/php
```

## 编译安装
```
./configure --prefix=/usr/local/php \
 --with-libdir=lib64 \
 --enable-fpm \
 --with-fpm-user=php-fpm \
 --with-fpm-group=www \
 --enable-mysqlnd \
 --with-mysql=mysqlnd \
 --with-mysqli=mysqlnd \
 --with-pdo-mysql=mysqlnd \
 --enable-opcache \
 --enable-pcntl \
 --enable-mbstring \
 --enable-soap \
 --enable-zip \
 --enable-calendar \
 --enable-bcmath \
 --enable-exif \
 --enable-ftp \
 --enable-intl \
 --with-openssl \
 --with-zlib \
 --with-curl \
 --with-gd \
 --with-zlib-dir=/usr/lib \
 --with-png-dir=/usr/lib \
 --with-jpeg-dir=/usr/lib \
 --with-gettext \
 --with-mhash \
 --with-ldap


make -j 20
make install

```

