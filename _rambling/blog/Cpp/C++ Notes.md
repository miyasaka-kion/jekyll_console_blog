---
layout: page
title: C++ Notes
categories: cpp
---

> status: continuously updated;
>
> feature: topics long enough will be addressed in separate sections

# Dynamic Memory

```cpp
double* pvalue  = nullptr; // Pointer initialized with null
pvalue  = new double;   // Request memory for the variable
```

> The **malloc()** function from C still exists in C++, but it is recommended to avoid using it. The main advantage of `new` over `malloc()` is that `new` **doesn't just allocate memory, it constructs objects**, which is the primary purpose of C++.

# Namespace

Namespaces provide a method for preventing name conflicts in large projects.

e.g.

```cpp
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



When `a` appears in both local and global scopes, `::a` refers to the global variable while `a` refers to the local variable.

```cpp
#include <iostream>
using namespace std;
namespace A
{
    int a = 100;
    namespace B            
    {
        int a =20;
    }
}

int a = 200; // defining a global variable


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
a =200      // global variable a
::a =200
a =30       // local variable a
::a =200 
```

## Recommendations

- Use variables in a named namespace instead of using external global variables.
- Use variables in an unnamed namespace instead of using static global variables.

# File Management

### Header File

Functions are declared but not defined.

> Function definition and function prototype:
>
> 1. Different content: Function definition includes the specific implementation of the function, including the function body and actual executable code; whereas function prototypes are only declarations that contain basic information about the function.
> 2. Different locations: Function definitions are typically placed in source files (e.g., `.cpp` files) to provide the actual implementation of the function; function prototypes are usually placed in header files (e.g., `.h` files) to provide the declaration of the function.
> 3. Different usage: Function definitions are used for writing the logic and implementation of the function; function prototypes are used to inform the compiler about the existence and basic information of the function, enabling type checking when the function is called elsewhere.
> 4. Different compilation requirements: Function definitions must be visible in each source file that calls the function, and the compiler needs to link the implementation of the function with the call site; function prototypes only need to be visible at the call site, and the compiler only needs to know the function declaration.

- Function prototypes
- Symbolic constants defined using #define or const
- Structure declarations
- Class declarations
- Template declarations
- Inline functions

#### Including a Header File

- Double quotation marks: searches the working path and standard location;
- Angle brackets: searches the host system's file system that holds the **standard header files**

### Source Code

Definitions with specific implementations.

# Linkage

Refer to: [Stack Overflow Explanation](https://stackoverflow.com/questions/1358400/what-is-external-linkage-and-internal-linkage)

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

### Array Traversal Order

```cpp
constexpr int maxn = 1 << 10;
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

The first approach spends most of the time reading and writing on contiguous memory, which is much faster.

```cpp
for(int i = 1; i < maxn; i++) {
    for(int j = 1; j < maxn; j++) {
        // dealing something with a[i][j]... Such as
        a[j][i] = f(a[j][i]);
    }
}
```

If we apply a function to this two-dimensional array, and if the cost of the function is less than the cost of jumping in columns, even if we optimize this function, it won't optimize the overall running time.

What's worse is when we need to access memory randomly, the time will become even longer—for example, when we use `std::list` and frequently perform `insert` operations, it will mess up the data in memory, resulting in low efficiency. If there is a fixed step, prefetching will come in to optimize performance.

### Utilizing Branch Prediction

Avoid complex:

- Branches
- Virtual function calls

## Sharing Between Cores

```cpp
void test() {
    Timer            timer;
    std::atomic<int> a(-1);
    std::thread      t0([&]() { work(a); });
    std::thread      t1([&]() { work(a); });
    std::thread      t2([&]() { work(a); });
    std::thread      t3([&]() { work(a); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}
```

Using more cores in this situation will result in slower speeds because multiple cores are competing for the same data.

```cpp
void test_maybe_better() {
    Timer            timer;
    std::atomic<int> a(-1);
    std::atomic<int> b(-1);
    std::atomic<int> c(-1);
    std::atomic<int> d(-1);
    std::thread      t0([&]() { work(a); });
    std::thread      t1([&]() { work(b); });
    std::thread      t2([&]() { work(c); });
   

 std::thread      t3([&]() { work(d); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}
```

Attempting to avoid core competition among different atomic variables doesn't solve the problem, and it remains slow, similar to the previous case.

Complete test program:

```cpp
#include <atomic>
#include <chrono>
#include <iostream>
#include <memory>
#include <thread>


class Timer {
private:
    std::chrono::time_point<std::chrono::high_resolution_clock> start_time;

public:
    Timer() {
        start_time = std::chrono::high_resolution_clock::now();
    }
    ~Timer() {

        auto end_time = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
        std::cout << "elapse time " << duration.count() << " ms" << std::endl;
    }
};

void work(std::atomic<int>& a) {
    for(int i = 1; i < 10000; i++) {
        a++;
    }
}

void test_one_core() {
    Timer            timer;
    std::atomic<int> a(-1);
    work(a);
    work(a);
    work(a);
    work(a);
}

void test() {
    Timer            timer;
    std::atomic<int> a(-1);
    std::thread      t0([&]() { work(a); });
    std::thread      t1([&]() { work(a); });
    std::thread      t2([&]() { work(a); });
    std::thread      t3([&]() { work(a); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}

void test_maybe_better() {
    Timer            timer;
    std::atomic<int> a(-1);
    std::atomic<int> b(-1);
    std::atomic<int> c(-1);
    std::atomic<int> d(-1);
    std::thread      t0([&]() { work(a); });
    std::thread      t1([&]() { work(b); });
    std::thread      t2([&]() { work(c); });
    std::thread      t3([&]() { work(d); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}

int main() {
    test_one_core();
    test();
    test_maybe_better();
    return 0;
}
```
