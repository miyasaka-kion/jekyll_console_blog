---
title: C++ Template
categories: cpp

---

# C++ Template

Undoubtedly, C++ template is a crucial part of the language.

> [Useful Tool](https://cppinsights.io/)

## Template Functions

A typical C++ template function looks like this:

```cpp
template<typename T>
T max(T const& a, T const& b) {
	return b < a ? a : b;
}
```

However, not every type `T` is suitable. For instance, if `T` does not define the `<` operator, it is not valid. Let's clarify all the requirements for `T`:

- `operator <` (returning bool)
- Copy/move constructor

## Concept

```cpp
template<typename T>
concept SupportsLessThan = requires(T x) {x < x;};

template<typename T>
requires std::copyable<T> && SupportsLessThan<T>
T max(T const& a, T const& b) {
	return b < a ? a : b;
}
```

Constraints on `T` are debug-friendly.

### Type Conversion

In certain cases, if the function is called with parameters passed by reference:

- Prohibit any type conversions

What if type conversions are allowed?

```cpp
template<typename T>
T max(T const& a, T const& b) {
	return b < a ? a : b;
}

int main() {
    max(4.2, 4); // It's ambiguous whether T should be int or double.
    return 0;
}
```

If the parameters are passed by value:

- Only allow decay conversions

Consider this function:

```cpp
template<typename T>
T max(T a, T b) {
	return b < a ? a : b;
}
```

When the parameters are passed by value to the template function, only a simple conversion called "decay" is allowed. Decay refers to some special transformations of the parameter type, such as removing const qualifiers or converting array types to pointer types. Here are some examples:

1. **Removing const qualifiers**: If the passed parameters have const qualifiers, they are removed. For example:

   ```cpp
   const int x = 42;
   const int y = 10;
   int result = max(x, y); // Both x and y will decay to the int type.
   ```

2. **Reference is converted to the referenced type**: If the passed parameters are references, they are converted to the referenced type. For example:

   ```cpp
   int a = 5;
   int &b = a;
   int result = max(a, b); // Both a and b will decay to the int type.
   ```

3. **Raw arrays are converted to pointers**: If the passed parameters are raw arrays, they are converted to pointers to the array elements. For example:

   ```cpp
   int arr1[5] = {1, 2, 3, 4, 5};
   int arr2[3] = {10, 20, 30};
   int *result1 = max(arr1, arr2); // Both arr1 and arr2 will decay to the int* type.
   ```

### Multiple Template Parameters

```cpp
template<typename T1, typename T2>
T1 max(T1 a, T2 b) {
	return b < a ? a : b;
}
```

How is the return value handled? The return value will change based on the deduction result of `T1`, which is not desirable.

#### Using Return Type Deduction

```cpp
template<typename T1, typename T2>
decltype(b < a ? a : b) max(T1 a, T2 b) {
  return b < a ? a : b;
}

/* First instantiated from: insights.cpp:8 */
#ifdef INSIGHTS_USE_TEMPLATE
template<>
double max<double, int>(double a, int b) {
  return static_cast<double>(b) < a ? static_cast<double>(b) : a;
}
#endif

int main() {
  max(3.2000000000000002, 1);
  return 0;
}
```

Here, the compiler casts int to double. Consequently, the return value of the entire expression becomes double.

> #### Excerpt from "C++ Templates: The Complete Guide" by Vandevoorde, D., Josuttis, N. M., & Gregor, D.
>
> Note that
>
> ```cpp
> template<typename T1, typename T2>
> auto max(T1 a, T2 b) -> decltype(true ? a : b);
> ```
>
> is a declaration. The compiler during the compilation phase decides the actual return type based on the result of the `?:` operator. In fact, using `true` as the condition for the `?:` operator is enough:
>
> ```cpp
> template<typename T1, typename T2>
> auto max(T1 a, T2 b) -> decltype(true ? a : b);
> ```
>
> [Stack Overflow - Code Snippet Effect](https://stackoverflow.com/questions/58093341/why-do-these-two-code-snippets-have-the-same-effect)
>
> However, in some cases, there might be a severe issue: *Since T might be a reference type*, the return type might also be inferred as a reference type. Therefore, you should return the decayed type of T, like this:
>
> ```cpp
> #include <type_traits>
> template<typename T1, typename T2>
> auto max(T1 a, T2 b) -> typename std::decay<decltype(true ? a : b)>::type {
> 	return b < a ? a : b;
> }
> ```

But why would the function template return a reference type, given that the function should go by reference? The return value is determined by `decltype(true ? a : b)`, and decltype provides a specific type deduction that includes references and const information. For example, when calling:

```cpp
int x = 42;
int& rx = x;
max(rx, 5);
```

the return type is deduced as `int&`, but in reality, `a` and `b` in the function `max` are copies of `rx` and `5`. This means that even though it's a reference type returned, it's a reference to a local variable within the function `max`, and after the lifetime of the function, `a` and `b` will be destroyed. Consequently, the returned reference will be a dangling reference, and any operations on this reference will lead to undefined behavior.

For example:

```cpp
template<typename T>
void print(const T& t) {
    std::cout << "Value: "  << t << std::endl;
    std::cout << "Addr: " << &t << std::endl;
}

template<typename T1, typename T2>
auto max(const T1& a, const T2& b) -> decltype(true ? a : b) {
    return b < a ? a : b; // Warning: Reference to stack memory associated with parameter 'b' returned (clang -Wreturn-stack-address)
}

int x = 42;
int& rx = x;
print(x);
print(rx);
double y = 4.2;
double& ry = y;
std::cout << "Is max(rx,

 5) a reference?: " << std::is_reference<decltype(max(rx, 5))>::value << std::endl;
int& max_r = max(rx, 5);
print(max_r);
max_r = 100;
print(x);
```

Output:

```
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

You can observe that `max(rx, 5)` is indeed a reference, but its `value` points to an address different from the original `x` — and the `value` of `max_r` is some strange data.

### Simple Applications

Output anything of any type:

```cpp
template<typename T>
void print(T& someArg) {
    cout << someArg << endl;
}
```

Output the name of the type (although it may not give a human-readable form):

```cpp
template<typename T>
void printType(T value) {
    cout << "The type of " << value << " is " << typeid(value).name() << endl;
}
```

For example, for the type:

```cpp
class MyType {
public:
    int x, y;    
};
```

an instance:

```cpp
MyType someInstance;
printType(someInstance);
```

prints:

```cpp
6MyType
```

Note that using `typeid(value).name()` may not always provide accurate results. To get the exact type, using boost is a better approach:

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

### Removing References

To review:
`std::is_reference<some_type>::value` can determine whether `some_type` is a reference type, including lvalue references, rvalue references, and references to pointers.

```cpp
std::remove_reference<int&&>::type some_x = 42;
std::cout << std::is_reference<decltype(ref_x)>::value << std::endl;
std::cout << std::is_reference<decltype(rref_x)>::value << std::endl;
std::cout << std::is_reference<decltype(some_x)>::value << std::endl;
```

Output:

```
1
1
0
```

Template functions have the property of removing references, so it's only natural to try a similar approach with template classes:

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

Output:

```
0
0
0
```

STL:

```cpp
_EXPORT_STD template <class _Ty>
struct remove_reference {
   using type                 = _Ty;
   using _Const_thru_ref_type = const _Ty;
};

template <class _Ty>
struct remove_reference<_Ty&> {
   using type                 = _Ty;
   using _Const_thru_ref_type = const _Ty&;
};

template <class _Ty>
struct remove_reference<_Ty&&> {
   using type                 = _Ty;
   using _Const_thru_ref_type = const _Ty&&;
};
```

### Preserving `const`?

In EFC++, a categorization discussion is made from a strictness perspective, so I won't repeat the content here.

I will answer the question "why" from an intuitive or logical perspective.

```cpp
template<typename T>
void f(T& param);
```

Firstly, for this deduction:

```cpp
int x=27;                       
f(x);                           
```

The function `f` has no `const` from its inception, indicating that the function's intent is to modify the value of `param`. Therefore, `ParamType` is deduced as `int&`.

```cpp
const int cx=x;                 
f(cx);                          
```

`x` is initially defined as constant, and the parameter `param` in function `f` is a reference. Therefore, `ParamType` is deduced as `const int&`.

```cpp
const int& rx=x;                
f(rx);                          
```

Here, `rx` is already defined as a reference to `x` as a constant int. The function `f` is a relaxation of `rx`'s declaration, so `ParamType` is deduced as `const int&`.
