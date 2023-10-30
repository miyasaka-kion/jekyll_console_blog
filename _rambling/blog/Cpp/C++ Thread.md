---
title: C++ thread
layout: page
categories: cpp
---





# C++ Thread



## Recover

命中率、缺失率、命中时间和缺失代价是与高速缓存（Cache）性能和效率相关的关键概念。这些术语用于描述缓存系统的性能特征和效果。让我逐一解释这些概念：

1. **命中率（Hit Rate）**：
   - 命中率是指在高速缓存中找到所需数据的概率，即在缓存中发生命中的频率。
   - 命中率计算公式：命中次数 / (命中次数 + 不命中次数)。
   - 高命中率表示大部分请求的数据都可以在缓存中找到，缓存系统的性能良好。

2. **缺失率（Miss Rate）**：
   - 缺失率是指在高速缓存中无法找到所需数据的概率，即在缓存未命中的频率。
   - 缺失率计算公式：不命中次数 / (命中次数 + 不命中次数)。
   - 低缺失率表示高速缓存很少需要从主内存中加载数据，这有助于提高性能。

3. **命中时间（Hit Time）**：
   - 命中时间是指从高速缓存中找到所需数据并返回给请求者所需的时间。它通常是非常短暂的，因为高速缓存设计用于提供快速的数据访问。
   - 较低的命中时间有助于减少访问缓存的延迟，提高整体性能。

4. **缺失代价（Miss Penalty）**：
   - 缺失代价是指当发生缓存未命中时，从主内存加载所需数据所需的时间和成本。
   - 缺失代价通常远高于命中时间，因为从主内存加载数据需要更多的时钟周期和更多的时间。
   - 高速缓存系统的性能和效率在很大程度上受到缺失代价的影响。较低的缺失代价意味着即使发生缓存未命中，也可以快速地恢复性能。



## 回到正题

一个简单的例子：

```cpp
#include <thread>
#include <iostream>

using std::cout;
using std::endl;


int main() {
    int cnt = 0;
    int maxn = 100000;
    std::thread worker1([&]() {
        for(int i = 0; i < maxn; i++) {
            cnt ++;
        }
    } );

    std::thread worker2([&]() {
        for(int i = 0; i < maxn; i++) {
            cnt++;
        }
    });
    worker1.join();
    worker2.join();
    cout << cnt << endl;
    return 0;
}
```





## 处理好核心之间竞争数据的问题

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

这种情况下使用越多的核心速度会越慢，因为多个核心竞争同一个数据；



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

尝试通过区分开不同的原子变量来避免核心之间竞争资源——但是这样并没有解决什么问题，和之前一样慢。







完整测试程序：

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

