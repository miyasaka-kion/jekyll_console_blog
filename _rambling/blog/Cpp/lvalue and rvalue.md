---
title: lvalue and rvalue, std::move()
categories: cpp
---



# lvalue and rvalue



>   [好用的工具](https://godbolt.org/)

## 写在前面

如何记住 [排 列 组 合](https://stackoverflow.com/questions/1143262/what-is-the-difference-between-const-int-const-int-const-and-int-const) ？

那如何区分这些东西呢？

-   `const int&`
-   `int& const`
-   `int const & const`
-   ……

## What is a lvalue and what is an rvalue?

>   [Awsome video from Cherno](https://www.youtube.com/watch?v=fbYknr-HPYE)
>
>   [Back to Basics: Understanding Value Categories - Ben Saks - CppCon 2019](https://www.youtube.com/watch?v=XS2JddPq7GQ&t=568s)

`=` 左边的是 lvalue，`=`右边的是 rvalue；

```cpp
int m, n;
m = 10;
n = 20;
foo(m + n);
```

-   lvalue: `m, n`
-   rvalue: `m + n`

我们不能像是对待 lvalue 那样对 rvalue 取地址，`m + n` 存在一个由编译器生成的 temporary object 里;

```cpp
#include <iostream>

// This is okay!
void getValue(const std::string& name) {
	std::cout << name << std::endl;
}

// error!!
void getValue(std::string& name) {
	std::cout << name << std::endl;
}

int main() {
	std::string name1 = "StringFirst ";
	std::string name2 = "stringSecond";
	getValue(name1 + name2);
	return 0;
}

```

`name1 + name2` is an rvalue so cannot be referenced by `std::string&` , which is an rvalue reference;

-   lvalue: We care about where it lives;
-   rvalue We care about where it holds;

-   概念上，rvalue 没有自己的地址，但是在实际情况中是可能会有的；
-   概念上，lvalue 举有自己的地址，但是在实际情况中也可能没有；
    -   比如被编译器优化掉；

>   坏的例子：我不想函数的 return value 被 copy，于是灵机一动使用 `std::move()` 来偷函数里面的 local variable:
>
>   ```cpp
>   std::vector<int> make_vec(const int n) {
>       std::vector<int> v;
>      	// ...
>       return std::move(v);
>   }
>   ```
>
>   实际上这样写的话：
>
>   ```cpp
>   std::vector<int> make_vec(const int n) {
>       std::vector<int> v;
>      	// ...
>       return v;
>   }
>   ```
>
>   既不会有 copy 也不会有 move，编译器会帮你优化好； 

How to specify which kind of value (lvalue or rvalue) should we use as the argument of a function?

```cpp
// This function can accept both lvalue and rvalue
void getValue(const std::string& name) {
	std::cout << name << std::endl;
}

// This function can only accept lvalue, since only lvalue have an address and thus can be referenced
void getValue(std::string& name) {
	std::cout << name << std::endl;
}

// This function can only accept rvalue,
// But! In the definition of the function, name is treated as an rvalue,
// In fact every argument inside function definition is an rvalue.
void getValue(std::string&& name) {
    std::cout << name << std::endl;
}
int main() {
	std::string name1 = "StringFirst ";
	std::string name2 = "stringSecond";
	getValue(name1 + name2);
	return 0;
}

```



## Unary *

unary * 产生 lvalue；

```cpp
int a[N];
int* p = a;
*p = 3 // OK, *p is an lvalue 
```



```cpp
char *s = nullptr;
*s = '\0' // undefined behavior
```

`*s` 是 lvalue，尽管他是个 `nullptr`，lvalue 可以赋值，但是不保证在语义上没问题；



## Rvalues of Class Type

概念上，rvalue of class type 不占用存储；

但是实际上会占用存储：

```cpp
int x = foo().x;
```

## Reference Types

Reference 可以被写成是一个常量指针（不是指向常量的指针），

>   常量指针：
>
>   -   引用不能为null，必须在声明时初始化，并且一旦初始化，它不能引用其他变量。

更具体来说就是：

```cpp
// refernce notation
// must be initialize as soon as it has been declared
int& ri = i; 
int* const cpi = &i;

```

就像是 [排 列 组 合](https://stackoverflow.com/questions/1143262/what-is-the-difference-between-const-int-const-int-const-and-int-const) 所说，区分 `int* const` 和 	`const int*`　的方法就是倒着念：

-  `int* const` -> const pointer to int;
- `const int*` -> pointer to const int;

为什么要引入 reference？

- 为了让自己实现的类型表现得就像 built-in 的类型一样;
- 没有 reference 我们很难写 overloaded operators;



-   A "pointer to T" can point only to an lvalue of type T.
-   Similarly,  a "reference to T" binds only to an lavlue of type T.

