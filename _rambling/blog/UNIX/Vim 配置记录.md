---
title: Vim configuration 
categories: vim 
---



# Vim 配置记录



懒人包：https://gitee.com/HGtz2222/VimForCpp/



Step 1: Compile vim with python3 and install;

```bash
$ git clone https://github.com/vim/vim.git
$ cd vim/src
$ ./configure --with-features=huge --enable-python3interp
$ make -j
$ sudo make install
```



Step 2: Install Vundle;

follow instructions on the [Vundle site](https://github.com/VundleVim/Vundle.vim):

```
https://github.com/VundleVim/Vundle.vim
```

注意全程的 `python3` 环境需要一致，不然直接重新开始（）；

有可能导致python3 环境不一样的因素：在 `/tmp	` 文件夹进行安装；


