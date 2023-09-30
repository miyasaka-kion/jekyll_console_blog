---
title: C++ thread
layout: page
categories: cpp
---





# C++ Thread

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



