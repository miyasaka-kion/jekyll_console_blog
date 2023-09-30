---
title: A simple list impl
categories: cpp
---



复习：

-   指针
    -   动态内存
-   类
    -   构造函数
    -   成员函数



### 动态内存

c 和 c++ 不同风格区分：

c++: 

-   `new`
-   `delete`

c:

-   `malloc()`
-   `free()`

**Remark**. 函数在 C 语言中就出现了，在 C++ 中仍然存在，但建议尽量不要使用 malloc() 函数。new 与 malloc() 函数相比，其主要的优点是，new 不只是分配了内存，它还创建了对象。

 **Remark**.  在面向对象编程时尽量不要使用 c 风格的动态内存编程方法. 有可能导致代码错误而不报错.

例：

```cpp
#include <iostream>

using std::cout;
using std::endl;

// insert overloaded new() function here

class Point {
public:
    int x, y;
    Point(int x, int y) : x(x), y(y) {
		cout << "Initialized!" << endl;
	}
};

int main() {
// #define CSTYLE
#ifdef CSTYLE
    int* p = ( int* )malloc(sizeof(Point));
	free(p);
#else
	Point* p = new Point(0, 1);
	delete p;
#endif
    return 0;
}

```

没有输出；需要注意 `malloc` 分配内存不会执行构造函数，`new` 会；

在调试的时候，为了让堆上的分配可视化，可以重载 `new`：

```cpp
void* operator new(size_t size) {
	cout << size << " of byte allocated!" << endl;
	return malloc(size);
}
```

这样就方便了调试：（输出：）

```cpp
8 of byte allocated!
Initialized!
```

回归正题：

### Class: Node

```cpp
class Node
{
public:
    int data;
    Node* next;
    Node()
    {
        this->data = 0;
        this->next = NULL;
    }
    Node(int _,Node *p = NULL)
    {
        this->data = _;
        this->next = p;
    }
    void info()
    {
        cout << "*****info*****" << endl;
        cout << "address:  " << this << endl;
        cout << "data:     " << this->data << endl;
    }
};
```

定义一个节点类`Node`:

-   `data`是节点保存的值；

-   `next` 是下一节点的地址；



### Class List

```cpp
class List
{
public:
    Node* HEAD;
    Node* TAIL;
    List()
    {
        HEAD = NULL;
        TAIL = NULL;
    }
    bool empty();
    void push_back(int x);
    void push_front(int x);
    void clear();
    void erase(Node* p);
    void insert(Node* p,int x);
    void print();
    Node* find_LtoR(int x);
    Node* find_LtoR_old(int x);
};
```

定义一个链表类`List`:

-   包含头部指针`HEAD`和尾部指针`TAIL`;
-   `bool empty();` 判断链表是否空；



### Functions 

```cpp
bool List::empty()
{
    if (this->HEAD == NULL)return true;
    return false;
}
```

-   `void push_back(int x);`

在链表尾部添加一个元素.

```cpp
void List::push_back(int x)
{
    Node* node = new Node();
    node->data = x;
    if (this->empty())
    {
        HEAD = node;
        TAIL = node;
        return;
    }
    this->TAIL->next = node;
    this->TAIL = node;
}
```



-   `void push_front(int x);`

在链表最前面添加一个元素.

```cpp
void List::push_front(int x)
{
    Node* node = new Node();
    node->data = x;
    if (this->empty())
    {
        HEAD = node;
        TAIL = node;
        return;
    }
    node->next = this->HEAD;
    this->HEAD = node;
}
```



-   ` void clear();`

将链表整个删除.

```cpp
void List::clear()
{
    for (Node* p = this->HEAD; p != NULL; p = p->next)
    {
        // free (p);
        delete p;
    }
    HEAD = NULL;
    TAIL = NULL;
}
```



-   `void erase(Node* p);`

从链表中删除一个元素`p`.

-   …

```cpp
void List::erase(Node* p)
{
    if (p == TAIL)
    {
        cout << "Nonething behind TAIL!" << endl;
    }
    if (p->next == TAIL)TAIL = p;

    cout << "debug" << endl;
    cout << p << ' ' << p->data<<endl;
    //...
    

    Node* cur;
    cur = (p->next);
    p->next = p->next->next;
    ////??
    delete(cur);
    //
    cout << "erase_ok" << endl;
}
```



-   `void insert(Node* p,int x);`

插入一个元素.

-   如果链表是空的：
    -   头和尾节点都指向插入的节点即可；
-   如果链表非空：
    -   …

```cpp
void List::insert(Node* p,int x)
{
    Node* node = new Node();
    node->data = x;

    if (this->empty())
    {
        HEAD = node;
        TAIL = node;
        return;
    }
    
    node->next = p->next;
    p->next = node;
}
```



-   `void print();`

    打印整个链表.

    ```cpp
    void List::print()
    {
        for (Node* p = this->HEAD; p != NULL; p = p->next)
        {
            cout << p->data << ' ';
        }
        cout << endl;
    }
    ```

    

-   `Node* find_LtoR(int x);`  

查找链表是否存在元素`x`，从左到右. 

-   如果找到就返回该元素对应的指针；
-   如果没有找到就返回空指针（未验证）；

```cpp
Node* List::find_LtoR(int x)
{ 
    Node* cur;
    cur = this->HEAD;
    for (; cur != NULL; cur = cur->next)
    {
        if (cur->data == x) break;
      //  cur->info();
    }
   // cout << endl;
    return cur;
}


```









### Appendix：All code.

```c++
// List_Template.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
using namespace std;
class Node
{
public:
    int data;
    Node* next;
    Node()
    {
        this->data = 0;
        this->next = NULL;
    }
    Node(int _,Node *p = NULL)
    {
        this->data = _;
        this->next = p;
    }
    void info()
    {
        cout << "*****info*****" << endl;
        cout << "address:  " << this << endl;
        cout << "data:     " << this->data << endl;
    }
};

class List
{
public:
    Node* HEAD;
    Node* TAIL;
    List()
    {
        HEAD = NULL;
        TAIL = NULL;
    }
    bool empty();
    void push_back(int x);
    void push_front(int x);
    void clear();
    void erase(Node* p);
    void insert(Node* p,int x);
    void print();
    Node* find_LtoR(int x);
    Node* find_LtoR_old(int x);
};

void List::print()
{
    for (Node* p = this->HEAD; p != NULL; p = p->next)
    {
        cout << p->data << ' ';
    }
    cout << endl;
}

bool List::empty()
{
    if (this->HEAD == NULL)return true;
    return false;
}

void List::push_front(int x)
{
    Node* node = new Node();
    node->data = x;
    if (this->empty())
    {
        HEAD = node;
        TAIL = node;
        return;
    }
    node->next = this->HEAD;
    this->HEAD = node;
}

void List::push_back(int x)
{
    Node* node = new Node();
    node->data = x;
    if (this->empty())
    {
        HEAD = node;
        TAIL = node;
        return;
    }
    this->TAIL->next = node;
    this->TAIL = node;
}

void List::insert(Node* p,int x)
{
    Node* node = new Node();
    node->data = x;

    if (this->empty())
    {
        HEAD = node;
        TAIL = node;
        return;
    }
    
    node->next = p->next;
    p->next = node;
}

void List::clear()
{
    for (Node* p = this->HEAD; p != NULL; p = p->next)
    {
        free (p);
    }
    HEAD = NULL;
    TAIL = NULL;
}

void List::erase(Node* p)
{
    if (p == TAIL)
    {
        cout << "Noting behind TAIL!" << endl;
    }
    if (p->next == TAIL)TAIL = p;

    cout << "debug" << endl;
    cout << p << ' ' << p->data<<endl;
    //...
    

    Node* cur;
    cur = (p->next);
    p->next = p->next->next;
    ////??
    delete(cur);
    //
    cout << "erase_ok" << endl;
}

Node* List::find_LtoR(int x)
{ 
    Node* cur;
    cur = this->HEAD;
    for (; cur != NULL; cur = cur->next)
    {
        if (cur->data == x) break;
      //  cur->info();
    }
   // cout << endl;
    return cur;
}

int main()
{
    List L;
    std::cout << L.HEAD << ' ' << L.TAIL << std::endl;
    for (int i = 1; i <= 10; i++)
    {
        L.push_back(i);
    }
    L.print();
    for (int i = 1; i <= 10; i++)
    {
        L.push_front(i);
    }
    L.print();

    Node* nn = L.find_LtoR(7);
    nn->info();

    L.erase(nn);
    L.print();
    cout << "Hello World!\n";
    return 0;
}

```
