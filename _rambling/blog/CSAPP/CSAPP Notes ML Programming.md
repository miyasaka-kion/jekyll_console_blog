---
title: Machine level programming
layout: page
categories: csapp
---



# CSAPP Notes ML Programming

> - I have abbreviation: Computer System -  Notes: Machine Level Programming；
> - status: 正在更新;
> - other info:随手写的，不能保证准确性；
> - powered by: ChatGPT 辅助；

本课程主要使用 x86 指令；CISC（复杂指令集）；

ARM 属于 RISC （精简指令集）；

## `g++` 和 `gcc` 

`g++` 和 `gcc` 都是 GNU Compiler Collection（GNU 编译器集合）中的工具，用于编译源代码并生成可执行文件。然而，它们之间有一些区别：

1. **g++：**
   - `g++` 是 GNU 编译器集合中专门用于编译 C++ 源代码的工具。
   - 当你使用 `g++` 编译时，它会默认将源代码视为 C++ 代码，然后应用 C++ 相关的语法和标准库。
   - 如果你使用 `g++` 编译一个 C++ 源文件，它会自动链接 C++ 标准库。
   - 例如：`g++ main.cpp -o main`
2. **gcc：**
   - `gcc` 是 GNU 编译器集合中通用的编译器，可以用于编译多种编程语言，包括 C、C++、Objective-C 等。
   - 当你使用 `gcc` 编译时，它会根据文件的扩展名来确定是 C 还是 C++ 代码。`.c` 扩展名会被视为 C 代码，`.cpp` 扩展名会被视为 C++ 代码。
   - 对于 C++ 代码，`gcc` 会自动调用 `g++` 来处理。
   - 如果你使用 `gcc` 编译 C++ 源文件，同样会链接 C++ 标准库。
   - 例如：`gcc main.cpp -o main`

### 流程
 **预处理阶段（Preprocessing）：**
   - 输入：`.cpp`、`.h` 等源文件。
   - 输出：`.i` 文件。
   - 过程：在此阶段，预处理器执行宏展开、文件包含等操作，生成一个经过预处理的源代码文件。
2. **编译阶段（Compilation）：**
   - 输入：`.i` 文件。
   - 输出：`.s` 文件。
   - 过程：编译器将经过预处理的源代码翻译成汇编语言代码。
3. **汇编阶段（Assembly）：**
   - 输入：`.s` 文件。
   - 输出：`.o` 文件。
   - 过程：汇编器将汇编语言代码翻译成机器代码，并生成目标文件（`.o` 文件）。
4. **链接阶段（Linking）：**
   - 输入：`.o` 文件、库文件等。
   - 输出：可执行文件（通常无后缀名，或 `.exe`、`.out` 等，取决于操作系统）。
   - 过程：链接器将目标文件以及可能的库文件链接在一起，解决符号引用，生成最终的可执行文件。



###   常用参数

1. **编译参数：**

   - `g++ source.cpp`：编译 `source.cpp` 文件并生成默认输出文件 `a.out`。
   - `g++ source.cpp -o output`：编译 `source.cpp` 文件并将可执行文件命名为 `output`。

2. **指定编译阶段：**

   - `-c`：只进行编译，不进行链接，生成目标文件（`.o` 文件）。
     - 预处理->编译->汇编
   - `-S`：只进行预处理和编译，不进行汇编和链接，生成汇编代码文件（`.s` 文件）。
     - 预处理->编译
   - `-E`：只进行预处理，不进行编译等等，生成的仍然是`.cpp` 文件；

3. **预处理选项：**

   - `-E`：只进行预处理，将预处理结果输出到标准输出。

4. **优化选项：**

   - `-O0`、`-O1`、`-O2`、`-O3`：指定不同级别的优化。`-O0` 表示不进行优化，`-O3` 表示最高级别优化。

   - > https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
     >
     > 优化级别：
     >
     > 1. **-O0**: 这是最低级别的优化，代码将不会进行任何优化处理。这对于调试和分析非常有用，因为生成的代码将与源代码相匹配，但可能会导致较低的性能。
     > 2. **-O1**: 这个级别启用了一些基本的优化，如去除冗余的计算和一些常见的性能改进。代码的执行速度可能会稍有提升，但仍然保持着较好的调试友好性。
     > 3. **-O2**: 在这个级别，编译器会执行更多的优化，包括内联函数、循环展开等。这会带来显著的性能提升，但有些情况下可能会导致一些调试信息的丢失。
     > 4. **-O3**: 这是更高级别的优化，编译器会进行更多的变换，以提高代码的执行速度。然而，这可能会导致一些副作用，如增加代码大小和编译时间。
     > 5. **-Os**: 该选项会优化代码的大小，即尽量减小生成的可执行文件的大小，而不是追求最大的性能提升。
     > 6. **-Og**: 此选项用于 "优化用于调试"，会在保留调试信息的前提下，进行一些基本的优化，以平衡调试友好性和性能。
     > 7. **-Ofast**: 这是一个极高级别的优化选项，会启用所有的优化，并可能会违反一些标准的语义，以实现更高的性能。但这可能会导致一些不符合预期的行为。

5. **链接选项：**

   - `-l<library>`：链接指定的库。例如，`-lm` 链接数学库。
   - `-L<dir>`：指定搜索库文件的目录。

6. **头文件包含路径：**

   - `-I<dir>`：指定头文件的搜索路径。

7. **其他常用选项：**

   - `-std=<standard>`：指定使用的 C++ 标准，例如 `-std=c++11`。
   - `-Wall`：开启所有警告信息。
   - `-g`：生成调试信息，用于调试程序。
   - `-Werror`：将警告视为错误。
   - `-pedantic`：严格遵循标准规范，发出更多警告。

**例**

程序清单

```cpp
#include <iostream>

using namespace std;
int main() {
    cout << "Hello world!" << endl;
    int x = 1;
    int y = 2;
    int z = 3;

    return 0;
}

```



- `-c`：只进行编译，不进行链接，生成目标文件（`.o` 文件）。

  - 预处理->编译->汇编

  - `g++ test.cpp -Og -c`

  - 可以用 `objdump` 或者 `nm` 等工具查看目标文件

    - ```bash
      objdump -d test.o   # 查看目标文件的汇编代码
      nm test.o           # 列出目标文件中的符号表信息
      ```

      

- `-S`：只进行预处理和编译，不进行汇编和链接，生成汇编代码文件（`.s` 文件）。

  - 预处理->编译
  - `g++ test.cpp -Og -S` (生成一个 600 行左右的汇编代码)

  

- `-E`：只进行预处理，不进行编译等等，生成的仍然是`.cpp` 文件；

  - 预处理
  - `g++ test.cpp -Og -E -o test.pre` (会变成一个六万行左右的cpp代码)
  - 预处理会进行一些操作，比如：
    - 宏展开
    - 头文件包含
    - 条件编译
    - 删除注释
    - 生成行号信息
  - 大体上可以理解为 copy and paste

  

## Assembly

### Disassembling Object Code: Disassembler

`objdump -d ___ `

**例**

#### ARM

机器信息：

> \> g++ --version
>
> Apple clang version 14.0.3 (clang-1403.0.22.14.1)
>
> Target: arm64-apple-darwin22.6.0
>
> Thread model: posix
>
> InstalledDir: /Library/Developer/CommandLineTools/usr/bin

源程序：

```cpp
#include <iostream>

using namespace std;

int my_sum(int x, int y) {
    return x + y;
}

int main() {    
    my_sum(1, 2);   
    return 0;
}

```



到汇编就停下：

```sh
g++ test.cpp -Og -S
```



```
	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 13, 0	sdk_version 13, 3
	.globl	__Z6my_sumii                    ; -- Begin function _Z6my_sumii
	.p2align	2
__Z6my_sumii:                           ; @_Z6my_sumii
	.cfi_startproc
; %bb.0:
	add	w0, w1, w0
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	mov	w0, #0
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols

```



先生成可执行文件，再反汇编

```bash
g++ test.cpp -Og -o test.o
objdump -d test.o >> test.txt
```


```

test.o:	file format mach-o arm64

Disassembly of section __TEXT,__text:

0000000100003fa8 <__Z6my_sumii>:
100003fa8: 20 00 00 0b 	add	w0, w1, w0
100003fac: c0 03 5f d6 	ret

0000000100003fb0 <_main>:
100003fb0: 00 00 80 52 	mov	w0, #0
100003fb4: c0 03 5f d6 	ret

```

可以看到生成的汇编代码会短一点，因为丢失了一些信息；



等下，这个课程用的是 x86 的汇编（）

换个机器先——

#### X86

机器信息：

> \> g++ --version 
>
> g++ (GCC) 8.3.1 20190311 (Red Hat 8.3.1-3)
>
> Copyright (C) 2018 Free Software Foundation, Inc.
>
> This is free software; see the source for copying conditions. There is NO
>
> warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

源程序：

```cpp
#include <iostream>

using namespace std;

int my_sum(int x, int y) {
    return x + y;
}

int main() {    
    my_sum(1, 2);   
    return 0;
}


```




```bash
g++ test.cpp -Og -S
```


```
	.file	"test.cpp"
	.text
	.type	_Z41__static_initialization_and_destruction_0ii, @function
_Z41__static_initialization_and_destruction_0ii:
.LFB977:
	.cfi_startproc
	cmpl	$1, %edi
	jne	.L5
	cmpl	$65535, %esi
	jne	.L5
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$_ZStL8__ioinit, %edi
	call	_ZNSt8ios_base4InitC1Ev
	movl	$__dso_handle, %edx
	movl	$_ZStL8__ioinit, %esi
	movl	$_ZNSt8ios_base4InitD1Ev, %edi
	call	__cxa_atexit
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
.L5:
	ret
	.cfi_endproc
.LFE977:
	.size	_Z41__static_initialization_and_destruction_0ii, .-_Z41__static_initialization_and_destruction_0ii
	.globl	_Z6my_sumii
	.type	_Z6my_sumii, @function
_Z6my_sumii:
.LFB975:
	.cfi_startproc
	leal	(%rdi,%rsi), %eax
	ret
	.cfi_endproc
.LFE975:
	.size	_Z6my_sumii, .-_Z6my_sumii
	.globl	main
	.type	main, @function
main:
.LFB976:
	.cfi_startproc
	movl	$0, %eax
	ret
	.cfi_endproc
.LFE976:
	.size	main, .-main
	.type	_GLOBAL__sub_I__Z6my_sumii, @function
_GLOBAL__sub_I__Z6my_sumii:
.LFB978:
	.cfi_startproc
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$65535, %esi
	movl	$1, %edi
	call	_Z41__static_initialization_and_destruction_0ii
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE978:
	.size	_GLOBAL__sub_I__Z6my_sumii, .-_GLOBAL__sub_I__Z6my_sumii
	.section	.init_array,"aw"
	.align 8
	.quad	_GLOBAL__sub_I__Z6my_sumii
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.hidden	__dso_handle
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-44)"
	.section	.note.GNU-stack,"",@progbits

```




```bash
g++ test.cpp -Og -o test.o
objdump -d test.o >> test.txt
```


```

test.o:     file format elf64-x86-64


Disassembly of section .init:

00000000004004d8 <_init>:
  4004d8:	48 83 ec 08          	sub    $0x8,%rsp
  4004dc:	48 8b 05 15 0b 20 00 	mov    0x200b15(%rip),%rax        # 600ff8 <__gmon_start__>
  4004e3:	48 85 c0             	test   %rax,%rax
  4004e6:	74 05                	je     4004ed <_init+0x15>
  4004e8:	e8 23 00 00 00       	callq  400510 <__gmon_start__@plt>
  4004ed:	48 83 c4 08          	add    $0x8,%rsp
  4004f1:	c3                   	retq   

Disassembly of section .plt:

0000000000400500 <.plt>:
  400500:	ff 35 02 0b 20 00    	pushq  0x200b02(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400506:	ff 25 04 0b 20 00    	jmpq   *0x200b04(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40050c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400510 <__gmon_start__@plt>:
  400510:	ff 25 02 0b 20 00    	jmpq   *0x200b02(%rip)        # 601018 <__gmon_start__>
  400516:	68 00 00 00 00       	pushq  $0x0
  40051b:	e9 e0 ff ff ff       	jmpq   400500 <.plt>

0000000000400520 <_ZNSt8ios_base4InitC1Ev@plt>:
  400520:	ff 25 fa 0a 20 00    	jmpq   *0x200afa(%rip)        # 601020 <_ZNSt8ios_base4InitC1Ev@GLIBCXX_3.4>
  400526:	68 01 00 00 00       	pushq  $0x1
  40052b:	e9 d0 ff ff ff       	jmpq   400500 <.plt>

0000000000400530 <__libc_start_main@plt>:
  400530:	ff 25 f2 0a 20 00    	jmpq   *0x200af2(%rip)        # 601028 <__libc_start_main@GLIBC_2.2.5>
  400536:	68 02 00 00 00       	pushq  $0x2
  40053b:	e9 c0 ff ff ff       	jmpq   400500 <.plt>

0000000000400540 <__cxa_atexit@plt>:
  400540:	ff 25 ea 0a 20 00    	jmpq   *0x200aea(%rip)        # 601030 <__cxa_atexit@GLIBC_2.2.5>
  400546:	68 03 00 00 00       	pushq  $0x3
  40054b:	e9 b0 ff ff ff       	jmpq   400500 <.plt>

0000000000400550 <_ZNSt8ios_base4InitD1Ev@plt>:
  400550:	ff 25 e2 0a 20 00    	jmpq   *0x200ae2(%rip)        # 601038 <_ZNSt8ios_base4InitD1Ev@GLIBCXX_3.4>
  400556:	68 04 00 00 00       	pushq  $0x4
  40055b:	e9 a0 ff ff ff       	jmpq   400500 <.plt>

Disassembly of section .text:

0000000000400560 <_start>:
  400560:	31 ed                	xor    %ebp,%ebp
  400562:	49 89 d1             	mov    %rdx,%r9
  400565:	5e                   	pop    %rsi
  400566:	48 89 e2             	mov    %rsp,%rdx
  400569:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  40056d:	50                   	push   %rax
  40056e:	54                   	push   %rsp
  40056f:	49 c7 c0 20 07 40 00 	mov    $0x400720,%r8
  400576:	48 c7 c1 b0 06 40 00 	mov    $0x4006b0,%rcx
  40057d:	48 c7 c7 85 06 40 00 	mov    $0x400685,%rdi
  400584:	e8 a7 ff ff ff       	callq  400530 <__libc_start_main@plt>
  400589:	f4                   	hlt    
  40058a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400590 <deregister_tm_clones>:
  400590:	b8 4f 10 60 00       	mov    $0x60104f,%eax
  400595:	55                   	push   %rbp
  400596:	48 2d 48 10 60 00    	sub    $0x601048,%rax
  40059c:	48 83 f8 0e          	cmp    $0xe,%rax
  4005a0:	48 89 e5             	mov    %rsp,%rbp
  4005a3:	77 02                	ja     4005a7 <deregister_tm_clones+0x17>
  4005a5:	5d                   	pop    %rbp
  4005a6:	c3                   	retq   
  4005a7:	b8 00 00 00 00       	mov    $0x0,%eax
  4005ac:	48 85 c0             	test   %rax,%rax
  4005af:	74 f4                	je     4005a5 <deregister_tm_clones+0x15>
  4005b1:	5d                   	pop    %rbp
  4005b2:	bf 48 10 60 00       	mov    $0x601048,%edi
  4005b7:	ff e0                	jmpq   *%rax
  4005b9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000004005c0 <register_tm_clones>:
  4005c0:	b8 48 10 60 00       	mov    $0x601048,%eax
  4005c5:	55                   	push   %rbp
  4005c6:	48 2d 48 10 60 00    	sub    $0x601048,%rax
  4005cc:	48 c1 f8 03          	sar    $0x3,%rax
  4005d0:	48 89 e5             	mov    %rsp,%rbp
  4005d3:	48 89 c2             	mov    %rax,%rdx
  4005d6:	48 c1 ea 3f          	shr    $0x3f,%rdx
  4005da:	48 01 d0             	add    %rdx,%rax
  4005dd:	48 d1 f8             	sar    %rax
  4005e0:	75 02                	jne    4005e4 <register_tm_clones+0x24>
  4005e2:	5d                   	pop    %rbp
  4005e3:	c3                   	retq   
  4005e4:	ba 00 00 00 00       	mov    $0x0,%edx
  4005e9:	48 85 d2             	test   %rdx,%rdx
  4005ec:	74 f4                	je     4005e2 <register_tm_clones+0x22>
  4005ee:	5d                   	pop    %rbp
  4005ef:	48 89 c6             	mov    %rax,%rsi
  4005f2:	bf 48 10 60 00       	mov    $0x601048,%edi
  4005f7:	ff e2                	jmpq   *%rdx
  4005f9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000400600 <__do_global_dtors_aux>:
  400600:	80 3d 3d 0a 20 00 00 	cmpb   $0x0,0x200a3d(%rip)        # 601044 <_edata>
  400607:	75 11                	jne    40061a <__do_global_dtors_aux+0x1a>
  400609:	55                   	push   %rbp
  40060a:	48 89 e5             	mov    %rsp,%rbp
  40060d:	e8 7e ff ff ff       	callq  400590 <deregister_tm_clones>
  400612:	5d                   	pop    %rbp
  400613:	c6 05 2a 0a 20 00 01 	movb   $0x1,0x200a2a(%rip)        # 601044 <_edata>
  40061a:	f3 c3                	repz retq 
  40061c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400620 <frame_dummy>:
  400620:	48 83 3d c8 07 20 00 	cmpq   $0x0,0x2007c8(%rip)        # 600df0 <__JCR_END__>
  400627:	00 
  400628:	74 1e                	je     400648 <frame_dummy+0x28>
  40062a:	b8 00 00 00 00       	mov    $0x0,%eax
  40062f:	48 85 c0             	test   %rax,%rax
  400632:	74 14                	je     400648 <frame_dummy+0x28>
  400634:	55                   	push   %rbp
  400635:	bf f0 0d 60 00       	mov    $0x600df0,%edi
  40063a:	48 89 e5             	mov    %rsp,%rbp
  40063d:	ff d0                	callq  *%rax
  40063f:	5d                   	pop    %rbp
  400640:	e9 7b ff ff ff       	jmpq   4005c0 <register_tm_clones>
  400645:	0f 1f 00             	nopl   (%rax)
  400648:	e9 73 ff ff ff       	jmpq   4005c0 <register_tm_clones>

000000000040064d <_Z41__static_initialization_and_destruction_0ii>:
  40064d:	83 ff 01             	cmp    $0x1,%edi
  400650:	75 2e                	jne    400680 <_Z41__static_initialization_and_destruction_0ii+0x33>
  400652:	81 fe ff ff 00 00    	cmp    $0xffff,%esi
  400658:	75 26                	jne    400680 <_Z41__static_initialization_and_destruction_0ii+0x33>
  40065a:	48 83 ec 08          	sub    $0x8,%rsp
  40065e:	bf 45 10 60 00       	mov    $0x601045,%edi
  400663:	e8 b8 fe ff ff       	callq  400520 <_ZNSt8ios_base4InitC1Ev@plt>
  400668:	ba 38 07 40 00       	mov    $0x400738,%edx
  40066d:	be 45 10 60 00       	mov    $0x601045,%esi
  400672:	bf 50 05 40 00       	mov    $0x400550,%edi
  400677:	e8 c4 fe ff ff       	callq  400540 <__cxa_atexit@plt>
  40067c:	48 83 c4 08          	add    $0x8,%rsp
  400680:	c3                   	retq   

0000000000400681 <_Z6my_sumii>:
  400681:	8d 04 37             	lea    (%rdi,%rsi,1),%eax
  400684:	c3                   	retq   

0000000000400685 <main>:
  400685:	b8 00 00 00 00       	mov    $0x0,%eax
  40068a:	c3                   	retq   

000000000040068b <_GLOBAL__sub_I__Z6my_sumii>:
  40068b:	48 83 ec 08          	sub    $0x8,%rsp
  40068f:	be ff ff 00 00       	mov    $0xffff,%esi
  400694:	bf 01 00 00 00       	mov    $0x1,%edi
  400699:	e8 af ff ff ff       	callq  40064d <_Z41__static_initialization_and_destruction_0ii>
  40069e:	48 83 c4 08          	add    $0x8,%rsp
  4006a2:	c3                   	retq   
  4006a3:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  4006aa:	00 00 00 
  4006ad:	0f 1f 00             	nopl   (%rax)

00000000004006b0 <__libc_csu_init>:
  4006b0:	41 57                	push   %r15
  4006b2:	41 89 ff             	mov    %edi,%r15d
  4006b5:	41 56                	push   %r14
  4006b7:	49 89 f6             	mov    %rsi,%r14
  4006ba:	41 55                	push   %r13
  4006bc:	49 89 d5             	mov    %rdx,%r13
  4006bf:	41 54                	push   %r12
  4006c1:	4c 8d 25 10 07 20 00 	lea    0x200710(%rip),%r12        # 600dd8 <__frame_dummy_init_array_entry>
  4006c8:	55                   	push   %rbp
  4006c9:	48 8d 2d 18 07 20 00 	lea    0x200718(%rip),%rbp        # 600de8 <__init_array_end>
  4006d0:	53                   	push   %rbx
  4006d1:	4c 29 e5             	sub    %r12,%rbp
  4006d4:	31 db                	xor    %ebx,%ebx
  4006d6:	48 c1 fd 03          	sar    $0x3,%rbp
  4006da:	48 83 ec 08          	sub    $0x8,%rsp
  4006de:	e8 f5 fd ff ff       	callq  4004d8 <_init>
  4006e3:	48 85 ed             	test   %rbp,%rbp
  4006e6:	74 1e                	je     400706 <__libc_csu_init+0x56>
  4006e8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  4006ef:	00 
  4006f0:	4c 89 ea             	mov    %r13,%rdx
  4006f3:	4c 89 f6             	mov    %r14,%rsi
  4006f6:	44 89 ff             	mov    %r15d,%edi
  4006f9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  4006fd:	48 83 c3 01          	add    $0x1,%rbx
  400701:	48 39 eb             	cmp    %rbp,%rbx
  400704:	75 ea                	jne    4006f0 <__libc_csu_init+0x40>
  400706:	48 83 c4 08          	add    $0x8,%rsp
  40070a:	5b                   	pop    %rbx
  40070b:	5d                   	pop    %rbp
  40070c:	41 5c                	pop    %r12
  40070e:	41 5d                	pop    %r13
  400710:	41 5e                	pop    %r14
  400712:	41 5f                	pop    %r15
  400714:	c3                   	retq   
  400715:	90                   	nop
  400716:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40071d:	00 00 00 

0000000000400720 <__libc_csu_fini>:
  400720:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000400724 <_fini>:
  400724:	48 83 ec 08          	sub    $0x8,%rsp
  400728:	48 83 c4 08          	add    $0x8,%rsp
  40072c:	c3                   	retq   

```



#### 书上的例子

·



#### 使用`gdb` 调试

```cpp
(gdb) disassemble my_sum
Dump of assembler code for function _Z6my_sumii:
   0x0000000000400681 <+0>:	lea    (%rdi,%rsi,1),%eax
   0x0000000000400684 <+3>:	retq   
End of assembler dump.
```

  

#### x86-64 寄存器

**通用目的寄存器（General-Purpose Registers）：**

1. `rax`：累加器寄存器，用于存放函数返回值。
2. `rbx`：基址寄存器，一般作为数据指针使用。
3. `rcx`：计数寄存器，常用于循环计数和函数参数传递。
4. `rdx`：数据寄存器，用于存放函数返回值。
5. `rsi`：源索引寄存器，通常用于数据传输操作。
6. `rdi`：目的索引寄存器，通常用于数据传输操作。
7. `rsp`：栈指针寄存器，指向当前栈顶。
8. `rbp`：基址指针寄存器，用于指向当前栈帧的基址。
9. `r8` 到 `r15`：通用寄存器，用于一般用途。

**段寄存器（Segment Registers）：**

1. `cs`：代码段寄存器，存储当前代码段的选择子。
2. `ds`、`es`、`fs`、`gs`：数据段寄存器，用于存储数据段的选择子。
3. `ss`：堆栈段寄存器，存储堆栈段的选择子。

**指令指针寄存器（Instruction Pointer Register）：**

- `rip`：指令指针寄存器，存储下一条要执行的指令的地址。

**标志寄存器（Flags Register）：**

- `rflags`：标志寄存器，包含各种处理器状态标志，如条件码、进位标志等。

> 32 位寄存器：
>
> - `rax` -> `eax`
> - `rbx` -> `ebx`
> - ...
>
> - `r8` -> `r8d`
> - ...
>
> 也有 16 位的，也有 8 位的；

这些位置可以存值，也可以去除；

