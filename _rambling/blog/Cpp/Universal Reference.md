---
title: Universal reference
layout: page
categories: cpp
---



# Universal Reference

通用引用是个比较恼人的事情，因为他长得跟一般的右值引用很像；

通用引用可以接受左值和右值，比如：

```cpp
#include <iostream>

template <typename T>
void foo(T&& t) {
    std::cout << "Inside foo: " << t << std::endl;
}

int main() {
    int x = 42;
    const int y = 20;

    // 通用引用 T&& 绑定到左值
    foo(x);  // x 是左值
    foo(y);  // y 是左值

    // 通用引用 T&& 绑定到右值
    foo(10);  // 10 是右值
    foo(std::move(x));  // std::move(x) 是右值

    return 0;
}

```



>    如果一个函数模板形参的类型为`T&&`，并且`T`需要被推导得知，或者如果一个对象被声明为`auto&&`，这个形参或者对象就是一个通用引用。



>    如果类型声明的形式不是标准的`type&&`，或者如果类型推导没有发生，那么`type&&`代表一个右值引用。





>   通用引用，如果它被右值初始化，就会对应地成为右值引用；如果它被左值初始化，就会成为左值引用。

```cpp
#include <iostream>

// 通用引用函数模板
template <typename T>
void process(T&& val) {
    // 使用std::is_lvalue_reference来判断是否为左值引用
    if (std::is_lvalue_reference<T>::value) {
        std::cout << "Left value reference" << std::endl;
    } else {
        std::cout << "Right value reference" << std::endl;
    }
}

int main() {
    int x = 42; // x 是左值
    const int y = 55; // y 也是左值——不允许修改的左值
    int&& z = 100; // z 是右值引用

    process(x); // 传递左值
    process(y); // 传递左值
    process(std::move(z)); // 传递右值

    return 0;
}

```

输出：

```
Left value reference
Left value reference
Right value reference
```

