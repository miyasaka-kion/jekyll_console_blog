---
categories: cpp
title: typedef struct and struct
---



# `typedef struct` and `struct`

>   status: 更新中
>
>   warning: 初学者写的内容，可能有内容上的错误

>   https://stackoverflow.com/questions/252780/why-should-we-typedef-a-struct-so-often-in-c

## `typedef`

`typedef` 仅仅是给已有的类型取一个别名；

```c
typedef int my_int
```

>   `typedef` vs. `#define`
>
>   
>
>   >   详细：https://www.cnblogs.com/kion/p/17659279.html
>
>   -   `#define` is a preprocessor token: the compiler itself will never see it.
>   -   `typedef` is a compier token: the preprocessor does not care about it.
>

## `C` vs. `C++`

### C

在 C（注意不是 C++ ）中，像这样声明一个结构体：

```c
struct myStruct{
    int cat;
    int dog;
};
```

那么声明一个实例的时候就必须要带上 `struct` 关键字：

```c
struct myStruct myVariable;
```

所以为了偷懒有些人就会写成如下格式：

```c
typedef struct myStruct{
    int cat;
    int dog;
} myStruct;
```

就会让编译器把 `myStruct` 替换成 `struct myStruct`；



但是这样不一定是好的，也有说法是要尽量避免这种写法：

>   https://www.kernel.org/doc/html/latest/process/coding-style.html#typedefs

-    The `typedef` saves a little typing, but it hides the fact that it's a structure type. ：会隐藏这个对象是一个结构体类型的事实；
-   除非你确定这是需要隐藏的；

### C++

在 C++ 中，可以像这样声明一个结构体：

```c
struct myStruct{
    int cat;
    int dog;
};
```

而 `struct` 关键字是可选的：

```c
myStruct myVariable; // OK
struct myStruct myVariable; // also OK!
```

>   在 C 和 C++ 中其实 `struct` 和 `class` 的区别是：
>
>   -    `struct` 默认所有成员都是 public 的；
>   -    `class` 默认所有成员都是 private 的；