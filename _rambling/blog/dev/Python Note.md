---
categories: other
title: Python note
---



# Python Note

##### 判断类型

`type()`不会认为子类是一种父类类型；

`isinstance()`会认为子类是一种父类类型；

## Python 标准类型

-   Number
-   String 
-   List 
-   Tuple
-   Set
-   Dictionary

不可变数据：Number, String, Tuple

可变数据：List, Set, Dictionary

### Number

**int, float, bool, complex**

>   python2 has no `bool`class.
>
>   python3 has deifined `True` and `false` as Keyword.
>
>   example:
>
>   ```python
>   >>> True + 1
>   2
>   ```



### Clear Var

```python 
del var
```



### 数值运算

```python 
>>> 2/4		#	the result is a float
0.5
>>> 2//4	#	the result is a integer
0				
>>> 2 ** 5 # power
32
```

>   -   Python can assign values to multiple variables at the same time.
>
>   ```python
>   a,b = 1,2
>   ```
>
>   -   A var can point to different types of objects by assignments
>
>   ```python 
>   >>> a = 1
>   >>> type (a)
>   <class 'int'>
>   >>> a = 0.0
>   >>> type (a)
>   <class 'float'>
>   ```
>
>   -   In hybrid computings, Python will convert `int` to `float`
>   -   Python also supports complex number. For instance, `1+3j` or `complex(1,3)`

### String

For instance:

```python 
>>> str = 'miyasaka';
>>> print(str)
miyasaka
>>> print(str[0:-1])
miyasak
>>> print(str[0])
m
>>> print(str[2:5])
yas
>>> print(str[2:])
yasaka
>>> print(str * 2)
miyasakamiyasaka
>>> print(str + '-' + 'Shiori')
miyasaka-Shiori
```

>   Python没有单独的字符类型，一个字符就是长度为`1`的字符串；

#### 反斜杠(\\)

-   表示转义字符
-   续行符

>   重申：Python的字符串是常量，`word[0]='m'`是非法操作；

-   使用`r`来避免转义：

```python 
>>> print("misaka-shiori\n")
misaka-shiori

>>> print(r"misaka-shiori\n")
misaka-shiori\n
```



### List

和`String`一样：

-   `+`是列表连接

-   `*`是列表重复

    ```python
    >>> L = ['asd',1573,'kion',78.9]
    >>> l = ['*&^%$']
    >>> print(L)
    ['asd', 1573, 'kion', 78.9]
    >>> print(L[0])
    asd
    >>> print(L[1:3])
    [1573, 'kion']
    >>> print(L[2:])
    ['kion', 78.9]
    >>> print(L*2)
    ['asd', 1573, 'kion', 78.9, 'asd', 1573, 'kion', 78.9]
    >>> print(L+l)
    ['asd', 1573, 'kion', 78.9, '*&^%$']
    ```

列表中的元素可以改变：

```python 
>>> L = ['asd',1573,'kion',78.9]
>>> L[0]='wawa'
>>> L
['wawa', 1573, 'kion', 78.9]
```

List 可以接受三元参数：

```python 
# Usage: list[begin,end,step]
>>> L = [1,2,3,4,5]
>>> L[1:3:2]
[2]
```

#### List Comprehension

``` python 
>>> squares = list(map(lambda x: x**2, range(10)))
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Or 

```python 
>>> squares = [x**2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

A **list comprehension** consists of brackets containing an expression folloewed by a `for` clause, then zero or more `for` or `if` clases.

```python 
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> [(x, y) for x in range(10) for y in range(10)]
[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]
```



#### List iterator

```python
L = [x for x in range(10)]

it = iter(L)
print(next(it))
print(next(it))
for x in it:
    print(x, end = ' ')
```

output:

```
0
1
2 3 4 5 6 7 8 9 
```



##### StopIteration

```python 
import sys
L = [x for x in range(10)]

it = iter(L)

while 1:
    try:
        print(next(it),end = ' ')
    except StopIteration:
        sys.exit()
```

output:

```
0 1 2 3 4 5 6 7 8 9 
```





### Tuple

Syntactically, similar to `list`

#### Specital Things 

```python 
>>> T = () # <- empty tuple 
>>> T0 = (0,) # <- a tuple with only one element 
```



-   Elements in a tuple are **immutable** 
-   元组可以索引、切片
-   使用`+`进行拼接

### Set

```python 
>>> S = {'chicken','bull','duck','goose','monkey','monkey'}
>>> S
{'monkey', 'chicken', 'duck', 'goose', 'bull'}
```

Notice that Python automatically deleted duplicated elements

>   To create a empty `set`, we must use `set()` rather than `{}`. The latter one is used to create an empty `dictionary`.

```python
>>> a = set('isudghfiausdghf')
>>> b = set('weiuhsdkjnfcishjafd')
>>> a # print elements in a
{'f', 'a', 'u', 'i', 'g', 'd', 's', 'h'}
>>> a - b # letters in a but not in b
{'g'}
>>> a | b # letters in a or b or both 
{'f', 'a', 'c', 'i', 'd', 'k', 'j', 'e', 'h', 'u', 'n', 'g', 'w', 's'}
>>> a & b # letters in a and b
{'f', 'a', 'u', 'i', 'd', 's', 'h'}
>>> a ^ b # letters in a or b but not in both 
{'c', 'j', 'n', 'g', 'w', 'k', 'e'}
```

#### Set Comprehension

```python 
>>> a = {x for x in 'asdasd' if x not in 'as'}
>>> a
{'d'}
```



### Dictionaries

```python
>>> D = {}
>>> D['asd'] = 'misaka'
>>> D[2] = 1
>>> D
{'asd': 'misaka', 2: 1}
>>> d = {'first name':'Shiori','last name':'miyasaka','code':114514}
>>> d
{'first name': 'Shiori', 'last name': 'miyasaka', 'code': 114514}
>>> d.keys()
dict_keys(['first name', 'last name', 'code'])
>>> d.values()
dict_values(['Shiori', 'miyasaka', 114514])

>>> list(d)
['first name', 'last name', 'code']

>>> del d['code']
>>> d
{'first name': 'Shiori', 'last name': 'miyasaka'}
>>> d['number'] = 9090
>>> d
{'first name': 'Shiori', 'last name': 'miyasaka', 'number': 9090}
>>> 'first name' in d
True
>>> 'middle name'in d 
False
```

关于顺序问题：

```python
import collections
import random
import string
from collections import OrderedDict

def generate_one_random_string(word_length: int):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=word_length))
    return random_string

dic = dict()
odd = OrderedDict()
str_length = 6
for i in range(10):
    rand_str = generate_one_random_string(str_length)
    rand_num = random.randrange(0, 1000)
    print(rand_str + ' ' + str(rand_num))
    dic[rand_str] = rand_num
    odd[rand_str] = rand_num

print()

for key, val in dic.items():
    print(key + ' ' + str(val))

print("odd: ")
for key, val in odd.items():
    print(key + ' ' + str(val))

```

```python
S:\anaconda\envs\develop\python.exe S:/projects/test_programme/word_count/main.py
wT9f6P 545
Xp9jEC 257
0VxRXe 484
TcfbAg 644
8sFiWQ 180
aQcnjz 84
4qeDvV 288
4WZWyq 201
pIR0sy 825
v5wBhc 330

wT9f6P 545
Xp9jEC 257
0VxRXe 484
TcfbAg 644
8sFiWQ 180
aQcnjz 84
4qeDvV 288
4WZWyq 201
pIR0sy 825
v5wBhc 330
odd: 
wT9f6P 545
Xp9jEC 257
0VxRXe 484
TcfbAg 644
8sFiWQ 180
aQcnjz 84
4qeDvV 288
4WZWyq 201
pIR0sy 825
v5wBhc 330

Process finished with exit code 0
```

`dict`和`OrderedDict`是Python中两种不同的字典类型，它们在某些方面有所不同。

1. 插入顺序保持（Insertion Order Preservation）：
   - `dict`：在Python 3.7之前，`dict`对象的元素插入顺序是不确定的。从Python 3.7开始，字典保持了元素插入的顺序。但是，官方仍建议不要依赖于此，因为实际实现可能会有变化。
   - `OrderedDict`：`OrderedDict`对象会记住元素插入的顺序，并按照插入顺序进行迭代。

2. 迭代顺序（Iteration Order）：
   - `dict`：在Python 3.7及更高版本中，`dict`对象的迭代顺序与插入顺序相同。但是在旧版本的Python中，迭代顺序是不确定的。
   - `OrderedDict`：`OrderedDict`对象的迭代顺序总是与元素插入顺序相同。

3. 效率（Efficiency）：
   - `dict`：由于不需要维护插入顺序的开销，`dict`在内存使用和操作效率方面通常优于`OrderedDict`。
   - `OrderedDict`：由于需要维护插入顺序，`OrderedDict`可能比`dict`在内存使用和操作效率方面稍慢。

根据您的需求，您可以选择使用`dict`或`OrderedDict`。如果您需要保持元素的插入顺序，并且希望以插入顺序进行迭代，那么使用`OrderedDict`是一个好选择。如果顺序并不重要，您可以使用普通的`dict`来获得更好的性能。

#### `dict()` constructor:

```python 
>>> dict([('a',1),('b',2)])
{'a': 1, 'b': 2}
```

When the keys are simple strings and values are simple ints:

```python 
>>> dict(name = 170170, code = 2333)
{'name': 170170, 'code': 2333}
```



#### Dictionary Comprehension:

```python 
>>> {x:x**2 for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## Styling 

Class names should be written in *CamelCaps*. To do this, capitalize the first letter of each word in the name, and don’t use underscores. Instance and module names should be written in lowercase with underscores between words.

Class 要有 docstring. 和函数类似.

import 的先后顺序：先包含「标准库」

Python的标准库（Standard Library）是一组在Python安装时自带的模块和包，它们提供了丰富的功能和工具，涵盖了各种不同的领域。下面是一些常见的标准库模块的示例：

1. `os`：提供与操作系统交互的功能，例如文件和目录操作。
2. `sys`：提供与Python解释器和系统交互的功能，例如命令行参数和标准输入/输出。
3. `math`：提供数学运算和函数，例如三角函数、对数函数等。
4. `datetime`：提供日期和时间处理的功能，例如日期计算、格式化等。
5. `random`：提供生成随机数和随机选择的功能。
6. `json`：提供JSON（JavaScript Object Notation）的编码和解码功能。
7. `urllib`：提供与URL操作和网络通信的功能。
8. `re`：提供正则表达式的功能，用于模式匹配和文本处理。
9. `csv`：提供读写CSV（Comma-Separated Values）文件的功能。
10. `sqlite3`：提供与SQLite数据库的交互功能。

除了上述示例外，标准库还包含许多其他模块，涵盖了文件处理、网络编程、图形界面、多线程、数据处理、密码学等多个领域。您可以通过查看Python的官方文档以及标准库的文档，了解更多标准库模块的详细信息和用法。

需要注意的是，标准库模块在Python安装时已经包含在内，无需额外安装。您可以在Python代码中使用它们，无需任何额外的导入或安装步骤。


## `open()`

> but if a bug in your program
prevents the close() statement from being executed, the file may never
close. This may seem trivial, but improperly closed files can cause data
to be lost or corrupted. 


当文件没有正确关闭时，可能会导致数据丢失或损坏的原因有几个：

1. 数据缓冲区刷新（Buffer Flushing）：在文件关闭时，文件缓冲区中的数据通常会被刷新（写入磁盘）。如果文件没有正确关闭，数据可能仍然在缓冲区中，而没有被写入磁盘。这意味着在程序异常退出或崩溃的情况下，这些数据可能永远丢失。

2. 数据一致性（Data Consistency）：在文件关闭时，文件系统通常会执行一些操作以确保文件的一致性。这可能包括更新文件的元数据（如大小、时间戳等）。如果文件没有正确关闭，这些操作可能无法执行，导致文件的元数据不正确。这可能会导致其他程序或系统对文件的操作出现问题，甚至导致文件损坏。

3. 文件锁定（File Locking）：在某些情况下，多个进程或线程可能同时访问同一个文件。当文件被一个进程或线程打开并锁定时，其他进程或线程可能无法访问或修改文件。如果文件没有正确关闭，文件锁可能无法释放，导致其他进程或线程无法访问文件，进而导致数据丢失或损坏。

总之，关闭文件是一种良好的编程实践，可以确保文件的数据完整性和一致性。如果文件没有正确关闭，可能会导致数据在缓冲区中丢失、文件元数据不一致，以及其他进程或线程无法访问文件。这些问题可能会导致数据丢失或损坏，影响程序的正确性和可靠性。因此，在处理文件时，应该始终确保适时地关闭文件。

## NumPy

all elements in NumPy array should be homogeneous

### construction

- zeros 
- ones
- empty 
- arange
- linspace

(similar to MATLAB)

### manipulation

- sort 
  - argsort
  - ...
- concatenate

### shape and size

`narray.ndim` will tell you the number of axes, or dimensions, of the array 

`ndarray.size`

`ndarray.shape`   

### reshape

### Indexing and slicing

## Python vs C++

### 局部变量

Python和C++在局部变量的处理上存在一些差异，下面是一些常见的区别：

1. 声明和初始化：在C++中，局部变量必须显式声明和初始化，例如`int x = 5;`。而在Python中，变量在首次赋值时会被隐式声明和初始化，例如`x = 5`。

2. 静态类型和动态类型：C++是一种静态类型语言，变量在声明时需要指定其类型，并且类型在编译时检查。而Python是一种动态类型语言，变量的类型是在运行时确定的，并且可以随时更改。

3. 作用域：C++中的局部变量具有块级作用域，它们只在声明它们的块中可见。Python中的局部变量也具有块级作用域，但它们可以在块内的任何位置进行访问，包括在声明之前。

4. 生命周期：在C++中，局部变量的生命周期从其声明点开始，直到其所在的块结束。而在Python中，局部变量的生命周期是在其不再被引用之后，由垃圾回收器决定。

5. 默认值：在C++中，局部变量如果未初始化，则其值是未定义的，取决于变量的存储位置。在Python中，局部变量在首次赋值之前是不存在的，访问未初始化的局部变量会引发`NameError`异常。

这些是Python和C++之间局部变量处理的一些常见差异。需要根据具体的编程语言和上下文来理解和应用这些差异。

### `\0`

在Python中，字符串是以Unicode字符序列的形式表示的，而不是以null-terminated字符数组的形式表示。因此，在Python中并没有类似于C/C++中的`\0`表示字符串的结束符。

在C/C++中，由于使用null-terminated字符数组表示字符串，需要使用`\0`（空字符）来标识字符串的结束。这是因为在C/C++中，字符串是按照字符数组的形式存储的，以null字符作为结束符以便确定字符串的长度。

而在Python中，字符串是以Unicode字符序列的形式表示的，每个字符都有自己的编码，而不需要使用特殊字符来标识字符串的结束。在Python中，字符串的长度可以直接通过`len()`函数获取，不需要关注字符串的结束符。

因此，可以说Python中没有类似于C/C++中的`\0`结束符的概念。在Python中，字符串的长度表示的是字符的数量，而不需要特殊字符来标识字符串的结束。
