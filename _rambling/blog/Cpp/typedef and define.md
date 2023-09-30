---
title: "typedef v.s. #define"
Layout: page
categories: cpp
---

# `typedef` vs. `#define`

-   `#define` is a preprocessor token: the compiler itself will never see it.
-   `typedef` is a compiler token: the preprocessor does not care about it.

-   `#define` 由预处理器负责；
    -   本质上是 copy and paste;
    -   从声明开始，下面的代码都可见；
-   `typedef` 由编译器负责；
    -   就像是变量一样，具有作用域；
    -   可以做到一些`#define` 做不到的事情；

https://stackoverflow.com/questions/1666353/are-typedef-and-define-the-same-in-c

`typedef` obeys scoping rules just like variables, whereas `define` stays valid until the end of the compilation unit (or until a matching `undef`).
Also, some things can be done with `typedef` that cannot be done with `define`.
For example:

```cpp
typedef int* int_p1;
int_p1 a, b, c;  // a, b, c are all int pointers

#define int_p2 int*
int_p2 a, b, c;  // only the first is a pointer, because int_p2
                // is replaced with int*, producing: int* a, b, c
                // which should be read as: int *a, b, c
typedef int a10[10];
a10 a, b, c;  // create three 10-int arrays
typedef int (*func_p) (int);
func_p fp;  // func_p is a pointer to a function that
           // takes an int and returns an int
```





总之为了避免发生奇怪的事情，最好避免这样的声明方式：

```cpp
int* a, b;
```

而是更显示地写成这样：

```cpp
int* a; // a 是指针变量，可以存储整数变量的地址
int b;  // b 是整数变量
```

为了防止`int* a, b;` 这样的东西出现，就像上文展示的那样，最好不要用`#define` 来给`int*` 创建 alias，而是应该使用`typedef`.



When things get "hairy", using the proper tool makes it right

```cpp
#define FX_TYPE void (*)(int)
typedef void (*stdfx)(int);

void fx_typ(stdfx fx); /* ok */
void fx_def(FX_TYPE fx); /* error */
```

