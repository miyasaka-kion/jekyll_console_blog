---
title: Git cheat sheets
categories: git, dev
---

# Git Notes

## basic command

`git add file`

`git commit ^m 'message'`



## 查看本地与远端的差异

使用 Git 命令来查看本地和远程仓库之间的差异。以下是一些常用的 Git 命令来进行比较和查看差异：

1. **查看本地分支与远程分支的差异：**

   ```shell
   git fetch origin  # 获取远程分支的最新信息
   git diff master origin/master  # 比较本地分支和远程分支的差异
   ```

   这将比较本地的 `master` 分支和远程的 `origin/master` 分支之间的差异。

2. **查看当前分支与远程分支的差异：**

   ```shell
   git fetch origin  # 获取远程分支的最新信息
   git diff HEAD origin/master  # 比较当前分支与远程分支的差异
   ```

   这将比较当前分支和远程的 `origin/master` 分支之间的差异。

3. **查看特定文件的差异：**

   ```shell
   git diff <file>  # 查看工作目录中文件的本地更改
   git diff HEAD <file>  # 查看文件在当前分支和最新提交之间的差异
   git diff <commit-hash-1> <commit-hash-2> -- <file>  # 比较两个提交之间文件的差异
   ```

   这些命令用于比较特定文件的本地更改、当前分支与最新提交之间的差异，或两个提交之间文件的差异。

4. **查看提交之间的差异：**

   ```shell
   git log  # 查看提交历史
   git log <commit-hash-1>..<commit-hash-2>  # 查看两个提交之间的提交历史
   git diff <commit-hash-1> <commit-hash-2>  # 比较两个提交之间的差异
   ```

   这些命令用于查看提交历史和比较不同提交之间的差异。

5. **查看远程仓库的 URL：**

   ```shell
   git remote -v  # 查看远程仓库的 URL
   ```

   这将显示远程仓库的 URL，以确保你正在与正确的远程仓库进行比较。

请根据你的具体需求使用上述 Git 命令来查看本地和远程仓库之间的差异。不同的情况可能需要不同的比较方式。





## 子模块

### 添加子模块

```shell
git submodule add <URL_to_submodule_repository> <path_to_submodule_directory>
```

要注意`<path_to_submodule_directory>` 是相对路径；

### 注意子模块的更新不会自动同步到主模块

在 Git 中，需要注意子模块的更新不会自动反映到包含它的主项目中。比如，

当你在子模块中进行了更改并将这些更改推送到子模块的远程仓库时，主项目 A 不会自动检测并获取子模块的最新更改。

要在项目 A 中获取子模块的最新更改，你需要手动执行以下步骤：

1. **在项目 A 中拉取子模块的最新更改：**

   ```shell
   git submodule update --remote
   ```

   这个命令会将子模块更新到其最新的提交。

2. **提交项目 A 的更改：**

   ```shell
   git add .
   git commit -m "Update submodule to latest version"
   git push origin master  # 或者你的主分支名称
   ```

   这将提交项目 A 中子模块的最新更改。

需要注意的是，如果项目 A 的其他开发者也希望获取子模块的最新更改，他们需要执行相同的操作。子模块的状态（特定的提交哈希）是在项目 A 中维护的，而不是子模块存储库中的文件内容，因此需要手动更新子模块。

总结起来，子模块的更新不会自动在主项目中反映，需要手动执行一些命令来获取和提交子模块的更改。这可以确保主项目和子模块之间的依赖关系保持一致。
