---
title: C++ template
categories: cpp
---

# C++ Template

毫无疑问 C++ template 是非常重要的一个部分.

>   [好用的工具](https://cppinsights.io/)

## 模板函数

一个普通的 C++ 模板函数是这样的

```cpp
template<typename T>
T max (T const& a, T const& b)
{
	return b < a ? a : b;
}
```

但是不是所有的 T 都行，比如 T 没定义 < 运算就肯定是不行的——让我们理清楚对 T 的所有要求：

-   operator < (returning bool)
-   copy/move constructor

## Concept

```cpp
template<typename T>
concept SupportsLessThan = requires (T x) {x < x;};

template<typename T>
requires std::copyable<T> && SupportsLessThan<T>
T max (T const& a, T const& b)
{
	return b < a ? a : b;
}
```

对 T 做出限制——调试友好；

### 类型转换

分情况，如果调用的参数是按引用传递：

-   禁止任何类型转换

如果允许类型转换呢？

```cpp
template<typename T>
T max (T const& a, T const& b)
{
	return b < a ? a : b;
}

int main() {
    max(4.2, 4); // 这样就不知道 T 应该是 int 好还是 double 好了——
    return 0;
}

```



如果调用参数是按值传递的：

-   只允许退化（decay）这一简单转换；

考虑这个函数：

```cpp
template<typename T>
T max (T a, T b)
{
	return b < a ? a : b;
}
```

当参数按值传递给模板函数时，只允许进行"退化"（decay）这一简单转换。退化指的是参数类型的一些特殊变换，例如去除const限定符、将数组类型转换为指针类型等。以下是一些例子：

1. **去除const限定符**：如果传递的参数具有const限定符，它们会被去除。例如：

   ```cpp
   const int x = 42;
   const int y = 10;
   int result = max(x, y); // x和y都会退化为int类型
   ```

2. **引用被转换为被引用的类型**：如果传递的参数是引用，它们会被转换为被引用的类型。例如：

   ```cpp
   int a = 5;
   int &b = a;
   int result = max(a, b); // a和b都会退化为int类型
   ```

3. **原始数组转换为指针**：如果传递的参数是原始数组，它们会被转换为指向数组元素的指针。例如：

   ```cpp
   int arr1[5] = {1, 2, 3, 4, 5};
   int arr2[3] = {10, 20, 30};
   int *result1 = max(arr1, arr2); // arr1和arr2都会退化为int*类型
   ```



### 多个模板参数

```cpp
template<typename T1, typename T2>
T1 max (T1 a, T2 b)
{
	return b < a ? a : b;
}
```

返回值如何处理？这个返回值会随着 `T1` 的推导结果改变而改变——这不是一个好事情；

#### 使用返回值推导

``` cpp
template<typename T1, typename T2>
decltype(b < a ? a : b) max(T1 a, T2 b)
{
  return b < a ? a : b;
}


/* First instantiated from: insights.cpp:8 */
#ifdef INSIGHTS_USE_TEMPLATE
template<>
double max<double, int>(double a, int b)
{
  return static_cast<double>(b) < a ? a : static_cast<double>(b);
}
#endif


int main()
{
  max(3.2000000000000002, 1);
  return 0;
}

```

这里编译器把 int cast 成了 double. 那么整个东西的返回值就是 double 了.



>   #### 摘选自 Vandevoorde, D., Josuttis, N. M., & Gregor, D. (Year). C++ Templates: The Complete Guide
>
>   需要注意的是
>
>   ```cpp
>   template<typename T1, typename T2>
>   auto max (T1 a, T2 b) -> decltype(b<a?a:b);
>   ```
>
>   是一个声明，编译器在编译阶段会根据运算符?:的返回结果来决定实际的返回类型。不过具
>   体的实现可以有所不同，事实上用 true 作为运算符?:的条件就足够了：
>
>   ```cpp
>   template<typename T1, typename T2>
>   auto max (T1 a, T2 b) -> decltype(true?a:b);
>   ```
>
>   >   https://stackoverflow.com/questions/58093341/why-do-these-two-code-snippets-have-the-same-effect
>
>   但是在某些情况下会有一个严重的问题：*由于 T 可能是引用类型*，返回类型就也可能被推断
>   为引用类型。因此你应该返回的是 decay 后的 T，像下面这样：
>
>   ```cpp
>   #include <type_traits>
>   template<typename T1, typename T2>
>   auto max (T1 a, T2 b) -> typename std::decay<decltype(true? a:b)>::type
>   {
>   	return b < a ? a : b;
>   }
>   ```
>
>   

why？函数模板不是会去引用吗？为什么会返回引用类型？

在这里返回值是由于`decltype(true? a:b)` 决定的，decltype 会给出一个具体的类型推导，这个推导会包括引用和`const`等信息。比如我这样子调用

```cpp
int x = 42;
int& rx = x; 
max(rx, 5);
```

那么返回值类型就推导为 `int&`, 但是实际上在函数 max 中的 `a` 和 `b` 是对调用时的` rx` 和 `5` 的拷贝——也就是说我们在返回的时候尽管是个 reference type，但是是对函数局部变量的 reference，在函数`max` 生命周期结束之后 `a` 和 ` b` 被销毁——那返回的引用将会是一个悬空引用，对这个引用的操作将会是未定义行为。

比如：

```cpp
template<typename T>
void print(const T& t) {
    std::cout << "Value: "  << t << std::endl;
    std::cout << "Addr: " << &t << std::endl;
}


template<typename T1, typename T2>
// auto max (T1 a, T2 b) -> typename std::decay<decltype(true? a:b)>::type
auto max (const T1& a, const T2& b) -> decltype(true? a:b)
// auto max(T1 a, T2 b)
{
    return b < a ? a : b; // 警告信息： Reference to stack memory associated with parameter 'b' returnedclang(-Wreturn-stack-address)
}
```

然后

```cpp  int x = 42;
    int x = 42;
    int& rx = x;
    print(x);
    print(rx);
    double y = 4.2;
    double& ry = y;
    std::cout << "is max(rx, 5) a reference?: " << std::is_reference<decltype(max(rx, 5))>::value << std::endl;
    int& max_r = max(rx, 5);
    print(max_r);
    max_r = 100;
    print(x);
```

输出：

```cpp
Value: 42
Addr: 0x9890fffd1c
Value: 42
Addr: 0x9890fffd1c
is max(rx, 5) a reference?: 1
Value: -1862271760
Addr: 0x9890fffcf0
Value: 42
Addr: 0x9890fffd1c
```



可以看到`max(rx, 5)` 确实是个引用，但是与原来的`x`指向的地址已经不一样了——而且`max(rx, 5)`的`value `还是一些奇怪的东西。



### 简单的应用

输出任意类型的东西：

```cpp
template<typename T>
void print(T& someArg) {
    cout << someArg << endl;
}
```



输出类型的名字（虽然这里不能给出人类友好的形式）：

```cpp
template<typename T>
void printType(T value) {
    cout << "The type of " << value << " is " << typeid(value).name() << endl;
}
```

比如对于类型

```cpp
class MyType {
public:
    int x, y;    
};
```

的一个实例，

```cpp
MyType someInstance;
printType(someInstance);
```

输出为：

```cpp
6MyType
```

要注意使用 typeid(value).name() 的做法得到的不一定是准确的结果——要想知道准确的类型，正确的做法是使用 boost：

>   boost 是第三方包，首先安装boost:
>
>   ```bash
>   brew install boost
>   ```
>
>   ```cmake
>   cmake_minimum_required(VERSION 3.15)
>   
>   set(CMAKE_CXX_STANDARD 20)
>   set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
>   set(CMAKE_CXX_COMPILER "<- YOUR COMPILER PATH ->")
>   
>   aux_source_directory(. SRC_LIST)
>   project(template_test)
>   
>   find_package(Boost REQUIRED COMPONENTS type_erasure)
>   if(NOT Boost_FOUND)
>       message("Boost not found!")
>   endif()
>   
>   include_directories(${Boost_INCLUDE_DIRS})
>   add_executable(${PROJECT_NAME} ${SRC_LIST})
>   target_link_libraries(${PROJECT_NAME} Boost::type_erasure)
>   ```
>
>   



### 去引用

>   复习：
>
>   `std::is_reference< some_type >::value ` 可以判断 `some_type` 是否是个 reference type, 包括左值引用和右值引用，也包括对指针的左值引用和右值引用。
>
>   https://en.cppreference.com/w/cpp/types/is_reference
>
>   ```cpp
>       std::remove_reference<int&&>::type some_x = 42;
>       std::cout << std::is_reference<decltype(ref_x)>::value << std::endl;
>       std::cout << std::is_reference<decltype(rref_x)>::value << std::endl;
>       std::cout << std::is_reference<decltype(some_x)>::value << std::endl;
>   ```
>
>   输出：
>
>   ```
>   1
>   1
>   0
>   ```
>
>   

模板函数具有去引用性，所以顺理成章想到一个应用：实现一个函数来去掉所有的引用，包括左值引用和右值引用

```cpp
template<typename T>
void print_is_reference(T value) {
    using type = T;
    std::cout << std::is_reference<T>::value << std::endl;
}
```

```cpp
int x = 10;
int& ref_x = x;
int&& rref_x = 42;    

print_is_reference(x); // x is neither a lvalue nor an rvalue reference
print_is_reference(ref_x); // x is a lvalue reference
print_is_reference(rref_x); // x is an rvalue reference 
```

输出：

```cpp
0
0
0
```



作为一个模板的新手，我已经迫不及待想尝试一下新的东西了——按照函数模板的思想，类似地试试看模板类

```cpp
template<typename T>
struct my_remove_reference {
    using type = T;
};

```

```cpp
    std::cout << std::is_reference<my_remove_reference<int>::type>::value << std::endl;
    std::cout << std::is_reference<my_remove_reference<int&>::type>::value << std::endl;
    std::cout << std::is_reference<my_remove_reference<int&&>::type>::value << std::endl;
```

输出：

```cpp
0
1 // <my_remove_reference<int&>::type 是一个引用！
1 // <my_remove_reference<int&>::type 是一个引用！
```

emmm? 怎么失败了？

要注意去引用这件事情发生的核心在于是否发生类型推导——

在模板函数 `print_is_reference` 中，我们传入了一个参数 `value` 的类型 `T` 会经过**类型推导**，而类型推导会去除参数的引用性，所以 `T` 最终是不带引用的类型。因此，无论传入的是 `int`、`int&` 还是 `int&&`，`T` 都会被推导为 `int`，不带引用。

然而，在模板类 `my_remove_reference` 中，我们显式地指定了 `T` 的类型——`int&` 或者是 `int &&`, 这样 T 就会保留 reference 这一信息。在这里，将传入的类型 `T` 分配给了 `type` 成员，没有经过类型推导的过程，因此 `type` 会保留传入类型 `T` 的引用性。这就是为什么在你这个尝试中 `my_remove_reference` 不会去除引用的原因。

更具体的例子是：

```cpp
#include <boost/type_index.hpp>
#include <iostream>
#include <type_traits>

template<typename T>
void f(const T& param)
{
	std::cout << " >>>>>>>>>>>>>>>>>> " << std::endl;
    using boost::typeindex::type_id_with_cvr;
    //显示T
    std::cout << "T =     "
         << type_id_with_cvr<T>().pretty_name()
         << '\n';
    
    //显示param类型
    std::cout << "param = "
         << type_id_with_cvr<decltype(param)>().pretty_name()
         << '\n';
}

int main() {
 	int x = 42;
	int& rx = x;
	const int& crx = rx;
    // 会进行推导
	f(x);
	f(rx);
	f(crx);

    // 显式指定 paramType
	f<int> (x);	
	f<int&> (x);
	f<int&&> (x);	
    
	return 0;
}

```

在显式指定 T 的时候，T 将 <> 里传入的参数原封不动保留；

```cpp
 >>>>>>>>>>>>>>>>>> 
T =     int
param = int const&
 >>>>>>>>>>>>>>>>>> 
T =     int
param = int const&
 >>>>>>>>>>>>>>>>>> 
T =     int
param = int const&
 >>>>>>>>>>>>>>>>>> 
T =     int
param = int const&
 >>>>>>>>>>>>>>>>>> 
T =     int&
param = int& // const 被去掉，因为参数被<>里传入的 int& 覆盖？(why?)
 >>>>>>>>>>>>>>>>>> 
T =     int&&
param = int& // 和上面一样

```

直觉上来说，`	f<int> (x)	` 强制了 `T` 的类型是 `int`，所以 `paramType` 是 `int const&`;

`f<int&> (x)` 试图强制 `T` 的类型是 `int&`，但是塞不到模板里面去，？





回到去引用的话题上来——正确的方法，是对左值引用和右值引用进行部分特化：

```cpp
template<typename T>
struct my_remove_reference {
    using type = T;
};

template<typename T>
struct my_remove_reference<T&> {
    using type = T;
};

template<typename T>
struct my_remove_reference<T&&> {
    using type = T;
};

```

```cpp
    std::cout << std::is_reference<my_remove_reference<int>::type>::value << std::endl;
    std::cout << std::is_reference<my_remove_reference<int&>::type>::value << std::endl;
    std::cout << std::is_reference<my_remove_reference<int&&>::type>::value << std::endl;
```

输出:

```cpp
0
0
0
```

>    STL ：  
>
>   ```cpp
>   _EXPORT_STD template <class _Ty>
>   struct remove_reference {
>       using type                 = _Ty;
>       using _Const_thru_ref_type = const _Ty;
>   };
>   
>   template <class _Ty>
>   struct remove_reference<_Ty&> {
>       using type                 = _Ty;
>       using _Const_thru_ref_type = const _Ty&;
>   };
>   
>   template <class _Ty>
>   struct remove_reference<_Ty&&> {
>       using type                 = _Ty;
>       using _Const_thru_ref_type = const _Ty&&;
>   };
>   ```
>
>   
>





### 是否保留 `const` ?

EFC++ 里面，从严谨度出发进行了分类讨论——所以我就不多重复那里的内容了。

我将会从直觉上，或者说从逻辑上可以解释，回答「为什么要这样」的问题。

```cpp
template<typename T>
void f(T& param);  
```

首先对于这里的推导：

```cpp
int x=27;                       //x是int
f(x);                           //T是int，param的类型是int&
```

函数 `f` 在定义之初就没有 `const`, 说明函数本意就是说 `param` 是一个会在函数的定义中可能会被改变的值，所以 `ParamType` 被推导为 `int&`.



```cpp
const int cx=x;                 //cx是const int
f(cx);                          //T是const int，param的类型是const int&
```

`x` 在定义之初就说明了常量性，`f` 的参数里说了 `param` 是一个引用，结果自然是` const`  和引用的叠加形式，所以 `ParamType` 被推导为 `const int&`.



```cpp
const int& rx=x;                //rx是指向作为const int的x的引用
f(rx);                          //T是const int，param的类型是const int&
```

这个更不用说了，其实`rx` 在声明的时候就已经规定了所有的事情了——这是一个对`x` 的引用， 不要尝试改变这个引用的值；函数 `f` 的规定是`rx`声明的一个放松，所以 `ParamType` 被推导为 `const int&`.
