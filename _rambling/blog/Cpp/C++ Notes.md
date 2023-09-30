---
layout: page
title: C++ Notes
categories: cpp
---

>   status: 持续更新；
>
>   feature：足够长的会单独开一个专题

# Dynamic Memory

```c++
double* pvalue  = NULL; // Pointer initialized with null
pvalue  = new double;   // Request memory for the variable
```

> The **malloc()** function from C, still exists in C++, but it is recommended to avoid using malloc() function. The main advantage of new over malloc() is that new **doesn't just allocate memory, it constructs objects** which is prime purpose of C++.

# Namespace

Namespaces provide a method for preventing name conflicts in large projects.

e.g.

```c++
#include <iostream>
using namespace std;
namespace my_namespace
{
    void my_function()
    {
        //x...
        cout << "xxx" << endl;
    }
    void another_namespace()
    {
        //x..
        void my_function()
        {
            cout << "this is another namespace." << endl;
        }
    }
}

int main()
{
    my_namespace::my_function();
    my_namespace::another_namespace::my_function();
    return 0;
}
```



当`a`既出现在局部又出现在全局，`::a`所指的是全局变量而`a`是局部变量。

```c++
#include <iostream>
using namespace std;
namespace A
{
    int a = 100;
    namespace B            //嵌套一个命名空间B
    {
        int a =20;
    }
}

int a = 200;//定义一个全局变量


int main(int argc, char *argv[])
{
    cout <<"A::a ="<< A::a << endl;
    cout <<"A::B::a ="<<A::B::a << endl;
    cout <<"a ="<<a << endl;
    cout <<"::a ="<<::a << endl;

    int a = 30;
    cout <<"a ="<<a << endl;
    cout <<"::a ="<<::a << endl;
    return 0;
}
```

```
A::a =100  
A::B::a =20
a =200      //全局变量a
::a =200
a =30       //局部变量a
::a =200 
```

## 建议

-   Use variables in a named namespace instead of using external global variables.
-   Use variables in an unnamed namespace instead of using static global variables.

# File Management

### header file

函数仅声明, 不定义.

>   函数定义（function definition）和函数原型（function prototype）
>
>   1.  内容不同：函数定义包含了函数的具体实现，包括函数体和实际执行的代码；而函数原型只是函数的声明，只包含函数的基本信息。
>   2.  位置不同：函数定义通常放在源文件（如`.cpp`文件）中，提供函数的实际实现；函数原型通常放在头文件（如`.h`文件）中，提供函数的声明。
>   3.  使用方式不同：函数定义用于实际编写函数的逻辑和实现；函数原型用于告知编译器有关函数的存在和基本信息，以便在其他地方调用函数时进行类型检查。
>   4.  编译要求不同：函数定义必须在每个调用该函数的源文件中可见，编译器需要将函数的实现与调用处进行链接；函数原型只需要在调用处可见，编译器只需要知道函数的声明即可。

-   Function prototypes
-   Symbolic constants defined using #define or const
-   Structure declarations
-   Class declarations
-   Template declarations
-   Inline functions

#### 引用 header file

-   double quotation marks: 搜索工作路径和 standard location;
-   angle brackets: host system’s file system that holds the **standard header files**

### source code

定义, 具体实现.



# Linkage

>   https://stackoverflow.com/questions/1358400/what-is-external-linkage-and-internal-linkage

```cpp
// In namespace scope or global scope.
int i; // extern by default
const int ci; // static by default
extern const int eci; // explicitly extern
static int si; // explicitly static

// The same goes for functions (but there are no const functions).
int f(); // extern by default
static int sf(); // explicitly static 
```





# Optimizing Performance

注意数组的遍历顺序:

```cpp
constexpr maxn = 1 << 10;
for(int i = 1; i < maxn; i++) {
	for(int j = 1; j < maxn; j++) {
        // dealing something with a[i][j]... Such as
        a[i][j] += j;
    }
}

for(int i = 1; i < maxn; i++) {
	for(int j = 1; j < maxn; j++) {
        // dealing something with a[i][j]... Such as
        a[j][i] += j; // not a good practice
    }
}
```

第一种大部分时间在连续的内存上读写，会快很多.

```cpp
for(int i = 1; i < maxn; i++) {
	for(int j = 1; j < maxn; j++) {
        // dealing something with a[i][j]... Such as
 		a[j][i] = f(a[j][i]);
    }
}
```



假如说我们对这个二维数组进行一些函数的运用，如果函数的开销小于在列上跳动的开销，那么就算优化了这个函数，也不会优化整体的运行时间.

什么是更糟糕，是当我们需要乱序访问内存的时候，时间会变得更长——比如我们使用`std::list`, 然后频繁进行`insert` 操作，这样就会把数据在内存上搞得乱七八糟，效率会很低。

如果是固定步长的话，prefetch 会出手来优化性能。

