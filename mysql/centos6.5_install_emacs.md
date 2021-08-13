# centos6.5 下 emacs 安装

## 配置依赖环境

```
yum -y groupinstall "Development Tools"
yum -y  install gtk+-devel gtk2-devel libXpm-devel libpng-devel giflib-devel libtiff-devel libjpeg-devel ncurses-devel gpm-devel dbus-devel dbus-glib-devel dbus-python  GConf2-devel pkgconfig libXft-devel
```

## 安装emacs

```
yum -y install emacs.x86_64
```

## 验证安装

```
emacs --version
GNU Emacs 23.1.1
Copyright (C) 2009 Free Software Foundation, Inc.
GNU Emacs comes with ABSOLUTELY NO WARRANTY.
You may redistribute copies of Emacs
under the terms of the GNU General Public License.
For more information about these matters, see the file named COPYING.
```