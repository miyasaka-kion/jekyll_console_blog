---
layout: page
title: Visual Studio - Workspace file management
categories: cpp, dev
published: false
---



# Visual Studio - Workspace file management

我的文件树样例：

```powershell
 CalculationPractice  tree
Folder PATH listing for volume 0x01
Volume serial number is 9C27-0C00
S:.
├─bin
│  ├─intermediates
│  │  └─x64
│  │      └─Debug
│  │          └─Calculat.6dd2621e.tlog
│  └─x64
│      └─Debug
└─CalculationPractice
    └─src
```



## 库管理

直接使用 Visual Studio 进行设置

### 静态库

https://learn.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-170&source=recommendations

-    **Add Reference** 
-    **Configuration** drop-down to **All Configurations**. Set the **Platform** drop-down to **All Platforms**
     -   **Configuration Properties** > **C/C++** > **General**
     -   **Additional Include Directories** property, specify the path of the directory, or browse for it.

### 动态库

-   略

![image-20230720183723381](https://s2.loli.net/2023/07/20/QDpAmWYI3CG7twe.png)







## 使用`premake` 生成项目文件