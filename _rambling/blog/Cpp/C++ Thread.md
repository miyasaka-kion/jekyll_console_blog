---
title: C++ Thread
layout: page
categories: cpp
---

# C++ Thread

## Recovery

Hit rate, miss rate, hit time, and miss penalty are key concepts related to the performance and efficiency of caches. These terms are used to describe the performance characteristics and effects of cache systems. Let me explain these concepts one by one:

1. **Hit Rate**:
    - Hit rate refers to the probability of finding the required data in the cache, i.e., the frequency of hits in the cache.
    - Hit rate calculation formula: number of hits / (number of hits + number of misses).
    - A high hit rate indicates that most requested data can be found in the cache, indicating good cache system performance.

2. **Miss Rate**:
    - Miss rate refers to the probability of not finding the required data in the cache, i.e., the frequency of cache misses.
    - Miss rate calculation formula: number of misses / (number of hits + number of misses).
    - A low miss rate indicates that the cache rarely needs to load data from the main memory, which helps improve performance.

3. **Hit Time**:
    - Hit time refers to the time taken to find the required data in the cache and return it to the requester. It is usually very short as caches are designed to provide fast data access.
    - Lower hit time helps reduce access latency to the cache and improve overall performance.

4. **Miss Penalty**:
    - Miss penalty refers to the time and cost required to load the required data from the main memory when a cache miss occurs.
    - Miss penalty is usually much higher than hit time because loading data from the main memory takes more clock cycles and time.
    - The performance and efficiency of a cache system are greatly influenced by the miss penalty. A lower miss penalty means that even if a cache miss occurs, performance can be quickly recovered.

## Back to the Point

A simple example:

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

## Managing Data Competition Between Cores

```cpp
void test() {
    Timer timer;
    std::atomic<int> a(-1);
    std::thread t0([&]() { work(a); });
    std::thread t1([&]() { work(a); });
    std::thread t2([&]() { work(a); });
    std::thread t3([&]() { work(a); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}
```

Using more cores in this situation will result in slower speeds because multiple cores are competing for the same data.

```cpp
void test_maybe_better() {
    Timer timer;
    std::atomic<int> a(-1);
    std::atomic<int> b(-1);
    std::atomic<int> c(-1);
    std::atomic<int> d(-1);
    std::thread t0([&]() { work(a); });
    std::thread t1([&]() { work(b); });
    std::thread t2([&]() { work(c); });
    std::thread t3([&]() { work(d); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}
```

Trying to avoid core competition among different atomic variables doesn't solve any problems, and it remains slow, similar to the previous case.

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
    Timer timer;
    std::atomic<int> a(-1);
    work(a);
    work(a);
    work(a);
    work(a);
}

void test() {
    Timer timer;
    std::atomic<int> a(-1);
    std::thread t0([&]() { work(a); });
    std::thread t1([&]() { work(a); });
    std::thread t2([&]() { work(a); });
    std::thread t3([&]() { work(a); });
    t0.join();
    t1.join();
    t2.join();
    t3.join();
}

void test_maybe_better() {
    Timer timer;
    std::atomic<int> a(-1);
    std::atomic<int> b(-1);
    std::atomic<int> c(-1);
    std::atomic<int> d(-1);
    std::thread t0([&]() { work(a); });
    std::thread t1([&]() { work(b); });
    std::thread t2([&]() { work(c); });
    std::thread t3([&]() { work(d); });
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