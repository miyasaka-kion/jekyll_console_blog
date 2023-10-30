---
title: C++ Templates
categories: cpp

---

# C++ Templates

There is no doubt that C++ templates are a crucial part of the language.

> [Useful Tool](https://cppinsights.io/)

## Template Functions

A typical C++ template function looks like this:

```cpp
template<typename T>
T max (T const& a, T const& b)
{
	return b < a ? a : b;
}
```

However, not every `T` is acceptable. For instance, if `T` doesn't define the `<` operator, it won't work. Let's clearly define all the requirements for `T`:

- `operator <` (returning bool)
- copy/move constructor

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

Restricting `T` is debug-friendly.

### Type Conversion

Under different circumstances, if the parameters are passed by reference:

- Any type conversion is prohibited.

But what if type conversion is allowed?

```cpp
template<typename T>
T max (T const& a, T const& b)
{
	return b < a ? a : b;
}

int main() {
    max(4.2, 4); // In this case, we are uncertain whether T should be int or double.
    return 0;
}
```

If the parameters are passed by value:

- Only simple decay conversions are allowed.

Consider this function:

```cpp
template<typename T>
T max (T a, T b)
{
	return b < a ? a : b;
}
```

When the arguments are passed by value to the template function, only a simple conversion, known as "decay," is allowed. Decay refers to certain special transformations of the parameter type, such as removing const qualifiers or converting array types to pointer types. Here are some examples:

1. **Removing const qualifiers**: If the passed parameters have const qualifiers, they are removed. For example:

    ```cpp
    const int x = 42;
    const int y = 10;
    int result = max(x, y); // Both x and y will decay to int type.
    ```

2. **References are converted to the referenced type**: If the passed parameters are references, they are converted to the referenced type. For example:

    ```cpp
    int a = 5;
    int &b = a;
    int result = max(a, b); // Both a and b will decay to int type.
    ```

3. **Original arrays are converted to pointers**: If the passed parameters are original arrays, they are converted to pointers to array elements. For example:

    ```cpp
    int arr1[5] = {1, 2, 3, 4, 5};
    int arr2[3] = {10, 20, 30};
    int *result1 = max(arr1, arr2); // Both arr1 and arr2 will decay to int* type.
    ```

### Multiple Template Parameters

```cpp
template<typename T1, typename T2>
T1 max (T1 a, T2 b)
{
	return b < a ? a : b;
}
```

How should the return value be handled? The return value will change according to the deduced result of `T1`, which is not ideal.

#### Using Return Type Deduction

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
  return static_cast<double>(b) < a ? static_cast<double>(b) : a;
}
#endif


int main()
{
  max(3.2000000000000002, 1);
  return 0;
}
```

Here, the compiler casts `int` to `double`. Consequently, the return value becomes `double`.

> #### Excerpted from Vandevoorde, D., Josuttis, N. M., & Gregor, D. (Year). C++ Templates: The Complete Guide
>
> Note that
>
> ```cpp
> template<typename T1, typename T2>
> auto max (T1 a, T2 b) -> decltype(b<a?a:b);
> ```
>
> is a declaration, and the compiler at compile-time decides the actual return type based on the result of the `?:` operator. However, the specific implementation may vary. In fact, using `true` as the condition for the `?:` operator is sufficient:
>
> ```cpp
> template<typename T1, typename T2>
> auto max (T1 a, T2 b) -> decltype(true?a:b);
> ```
>
> > [Stack Overflow: Link](https://stackoverflow.com/questions/58093341/why-do-these-two-code-snippets-have-the-same-effect)
>
> However, in some cases, there could be a severe issue: *since T might be a reference type*, the return type could also be inferred as a reference type. Therefore, you should return the decayed type of T, like this:
>
> ```cpp
> #include <type_traits>
> template<typename T1, typename T2>
> auto max (T1 a, T2 b) -> typename std::decay<decltype(true? a:b)>::type
> {
> 	return b < a ? a : b;
> }
> ```
>



Why does the function template return a reference type, when it should deduce a reference?

Here, the return type is determined by `decltype(true? a:b)`. `decltype` provides a specific type deduction that includes information such as references and `const`. For example, if I call it like this:

```cpp
int x = 42;
int& rx = x; 
max(rx, 5);
```

the return type will be inferred as `int&`. However, in reality, `a` and `b` in the function `max` are copies of the call parameters `rx` and `5`, respectively. In other words, even though it's a reference type in the return, it's a reference to a function local variable, and after the lifetime of the function `max` ends, `a` and `b` will be destroyed. Therefore, the returned reference will be a dangling reference, and any operation on this reference will result in undefined behavior.

For example:

```cpp
template<typename T>
void print(const T& t) {
    std::cout << "Value: "  << t << std::endl;
    std::cout << "Addr: " << &t << std::endl;
}


template<typename T1, typename T2>
auto max (const T1& a, const T2& b) -> decltype(true? a:b)
{
    return b < a ? a : b; // Warning: Reference to stack memory associated with parameter 'b' returnedclang(-Wreturn-stack-address)
}

int main()


{
    int x = 42;
    int& rx = x;
    print(x);
    print(rx);
    double y = 4.2;
    double& ry = y;
    std::cout << "Is max(rx, 5) a reference?: " << std::is_reference<decltype(max(rx, 5))>::value << std::endl;
    int& max_r = max(rx, 5);
    print(max_r);
    max_r = 100;
    print(x);
}
```

The output will be:

```cpp
Value: 42
Addr: 0x9890fffd1c
Value: 42
Addr: 0x9890fffd1c
Is max(rx, 5) a reference?: 1
Value: -1862271760
Addr: 0x9890fffcf0
Value: 42
Addr: 0x9890fffd1c
```

It can be observed that `max(rx, 5)` is indeed a reference, but its `value` is different from the one pointed to by the original `x`. Moreover, the `value` of `max(rx, 5)` is some arbitrary value, not the expected `42`.

### Simple Applications

Printing anything:

```cpp
template<typename T>
void print(T& someArg) {
    cout << someArg << endl;
}
```



Printing the type's name (although this might not provide a human-friendly form):

```cpp
template<typename T>
void printType(T value) {
    cout << "The type of " << value << " is " << typeid(value).name() << endl;
}
```

For instance, for the type:

```cpp
class MyType {
public:
    int x, y;    
};
```

an instance of it,

```cpp
MyType someInstance;
printType(someInstance);
```

will output:

```cpp
6MyType
```

Note that using `typeid(value).name()` might not always yield accurate results. To obtain precise type information, using Boost is the recommended approach:

> Boost is a third-party package. First, install Boost:
>
> ```bash
> brew install boost
> ```
>
> ```cmake
> cmake_minimum_required(VERSION 3.15)
> 
> set(CMAKE_CXX_STANDARD 20)
> set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
> set(CMAKE_CXX_COMPILER "<- YOUR COMPILER PATH ->")
> 
> aux_source_directory(. SRC_LIST)
> project(template_test)
> 
> find_package(Boost REQUIRED COMPONENTS type_erasure)
> if(NOT Boost_FOUND)
> message("Boost not found!")
> endif()
> 
> include_directories(${Boost_INCLUDE_DIRS})
> add_executable(${PROJECT_NAME} ${SRC_LIST})
> target_link_libraries(${PROJECT_NAME} Boost::type_erasure)
> ```
>

### Removing References

To review:

`std::is_reference<some_type>::value` can determine whether `some_type` is a reference type, including lvalue references, rvalue references, and references to pointers.

```cpp
std::remove_reference<int&&>::type some_x = 42;
std::cout << std::is_reference<decltype(ref_x)>::value << std::endl;
std::cout << std::is_reference<decltype(rref_x)>::value << std::endl;
std::cout << std::is_reference<decltype(some_x)>::value << std::endl;
```

This will output:

```cpp
1
1
0
```

The template functions exhibit referential properties, which is why you attempted to implement a function to remove all references, including lvalue references and rvalue references:

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

This will output:

```cpp
0
1 // <my_remove_reference<int&>::type is a reference!
1 // <my_remove_reference<int&>::type is a reference!
```

However, it seems to have failed. The crucial point to note is that removing references occurs when type deduction happens. In the template function `print_is_reference`, the type `T` is the result of type deduction, and thus it is devoid of any references. Thus, whether it's `int`, `int&`, or `int&&`, `T` will be deduced as `int`, without any references.

However, in the case of the template class `my_remove_reference`, you explicitly specify the type of `T` as `int&` or `int&&`. As a result, `T` retains the information about the reference. In this scenario, assigning the type `T` to the member `type` does not undergo type deduction, thus preserving the reference information. This is why your attempt with `my_remove_reference` did not remove references.

A more specific example is:

```cpp
#include <boost/type_index.hpp>
#include <iostream>
#include <type_traits>

template<typename T>
void f(const T& param)
{
    std::cout << " >>>>>>>>>>>>>>>>>> " << std::endl;
    using boost::typeindex::type_id_with_cvr;
    // Show T
    std::cout << "T =     " << type_id_with_cvr<T>().pretty_name() << '\n';
    
    // Show param type
    std::cout << "param = " << type_id_with_cvr<decltype(param)>().pretty_name() << '\n';
}

int main() {
    int x = 42;
    int& rx = x;
    const int& crx = rx;
    // Deduction will happen
    f(x);
    f(rx);
    f(crx);

    // Explicitly specify the paramType
    f<int>(x);
    f<int&>(x);
    f<int&&>(x);    
    return 0;
}
```

When you explicitly specify `T`, it will remain unchanged from what you put inside the `<>`.

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
param = int& // 'const' is removed, because it's overridden by the int& passed inside <>
 >>>>>>>>>>>>>>>>>> 
T =     int&&
param = int& // Same as above
```

Indeed, `f<int> (x)` explicitly states that `T` is `int`, resulting in `paramType` being `int const&`. `f<int&> (x)` attempts to enforce `T` as `int&`, but it doesn't fit within the template, hence the const is overridden by the `int&` passed inside the `<>`.

Returning to the topic of removing references, the correct approach is to perform partial specializations for lvalue references and rvalue references:

```cpp
template<typename T>
struct
