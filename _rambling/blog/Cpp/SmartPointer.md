
```cpp
#include <iostream>
// #include <GLFW/glfw3.h>
#include <memory>

// #include "Logger.h"

class Log {
public:
    Log() {
        p_x = std::make_shared<int>(42);
    }

    std::shared_ptr<int> getValueByValue() {
        std::cout << "getValueByValue -> use_count() = " << p_x.use_count() << std::endl;
        return p_x;
    }

    std::shared_ptr<int>& getValueByReference() {
        std::cout << "getValueByReference -> use_count() = " << p_x.use_count() << std::endl;
        return p_x;
    }

    decltype(auto) getUseCount() {
        return p_x.use_count();
    }

private:
    std::shared_ptr<int> p_x;
};

template <typename T>
void print(T value) {
    std::cout << value << std::endl;
}

int main() {
    Log log{};
    std::cout << &(*log.getValueByReference()) << std::endl;
    std::cout << &(*log.getValueByReference()) << std::endl;
    std::cout << "log.getValueByValue().use_count(): " << log.getValueByReference().use_count() << std::endl;

    std::cout << "log.getUseCount():" << log.getUseCount() << std::endl;


    return 0;
}
```