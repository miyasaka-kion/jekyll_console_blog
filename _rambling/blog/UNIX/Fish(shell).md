# Fish 的特性

>   status: 正在更新

## Variables

`fish` has no delicated *VARIABLE=VALUE* syntax for setting variables. Instead it has an ordinary command: `set`, which takes a variable name, and then its value.

```shell
> set name 'miyasaka kion'
> echo $name
miyasaka kion
```

Also, variables are not further split after substitution:

```shell
> mkdir $name
> ls
miyasaka kion
```

In bash, this would have created two directories "miyasaka" and "kion".

In fish, it only create one.

To erase/delete a variable;

```shell
> set -e my_variable
> env | grep my_variable
(no output)
```



## Exports

To give a variable to an external command, it needs to be "exported".

`fish` does not have and export command. We use `set` followed by either `--export` or `-x`.

```shell
> set -x my_variable
> env | grep my_variable
my_variable=some_value
```



## 执行

在 Fish Shell 中，你可以使用 `;` 来执行多个命令，但默认情况下它们是按照阻塞式执行的方式执行的。也就是说，每个命令会在前一个命令执行完毕后才会执行。

非阻塞式执行可以通过使用 `&` 来实现，这将使命令在后台执行，不会等待前一个命令执行完毕：

1.  阻塞式执行：

    ```
    shellCopy code
    command1 ; command2 ; command3
    ```

    在上述示例中，`command2` 和 `command3` 都会在 `command1` 执行完毕后才会执行。

2.  非阻塞式执行：

    ```
    shellCopy code
    command1 & command2 & command3
    ```

    在上述示例中，`command2` 和 `command3` 会立即在后台执行，不会等待 `command1` 执行完毕。
