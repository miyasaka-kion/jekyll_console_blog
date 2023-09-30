---
title: SDL configuration
categories: dev
---


# SDL 项目配置记录



```bash
brew install sdl2
brew install sdl2_image
brew install spdlog 

```

```bash
brew --prefix sdl2
...
```

文件结构:

- 这里好像是吧 spdlog 编译安装了

```bash
kionmiyasaka@macmini ~/D/p/spdtest> tree -L 2

.
├── CMakeLists.txt
├── build
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   ├── Makefile
│   ├── cmake_install.cmake
│   └── spdtest
├── main.cpp
└── spdlog
    ├── CMakeLists.txt
    ├── INSTALL
    ├── LICENSE
    ├── README.md
    ├── appveyor.yml
    ├── bench
    ├── build
    ├── cmake
    ├── example
    ├── include
    ├── logos
    ├── scripts
    ├── src
    └── tests
```



```cmake
cmake_minimum_required(VERSION 3.11)

project(spdtest)

if(NOT TARGET spdlog)
    # Stand-alone build
    find_package(spdlog REQUIRED)
	message(STATUS "Package spdlog found status: ${spdlog_FOUND}")
	message(STATUS "spdlog_DIR = ${spdlog_DIR}")
	message(STATUS "spdlog_INCLUDE_DIRS = ${spdlog_INCLUDE_DIRS}")
	message(STATUS "spdlog_LIBS = ${spdlog_LIBS}")
	
endif()


find_package(SDL2 REQUIRED)
message(STATUS "Package SDL2 found status: ${SDL2_FOUND}")
message("SDL2_DIR = ${SDL2_DIR}")
message("SDL2_INCLUDE_DIR = ${SDL2_INCLUDE_DIR}")
add_executable(spdtest main.cpp)
target_link_libraries(spdtest PRIVATE SDL2::SDL2)
target_link_libraries(spdtest PRIVATE spdlog::spdlog_header_only)


```

`find_package` 会自己找到 brew 安装的包；





例程：

```cpp
#include <iostream>
#include <spdlog/spdlog.h>

using std::cout;
using std::endl;

int main() {
	spdlog::info("test");
	return 0;
}

```







