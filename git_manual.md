# Git 常用操作手册

## 一、基础概念

| 概念 | 说明 |
|------|------|
| 工作区 (Workspace) | 你电脑上能看到的项目目录 |
| 暂存区 (Stage/Index) | 临时存放修改的地方，`git add` 后进入 |
| 本地仓库 (Local Repo) | 保存提交历史的地方，`git commit` 后进入 |
| 远程仓库 (Remote) | 托管在网络上的仓库，如 GitHub、Gitee |

---

## 二、Git 配置

```bash
# 设置用户名和邮箱（必做）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"

# 查看所有配置
git config --list

# 设置默认分支名为 main
git config --global init.defaultBranch main
```

---

## 三、创建仓库

```bash
# 在当前目录初始化一个新仓库
git init

# 克隆远程仓库到本地
git clone <仓库地址>
git clone <仓库地址> <自定义文件夹名>
```

---

## 四、日常工作流

```bash
# 查看文件状态
git status

# 查看简洁状态
git status -s

# 将文件添加到暂存区
git add <文件名>           # 添加指定文件
git add .                  # 添加所有修改
git add *.py               # 添加所有 .py 文件

# 提交到本地仓库
git commit -m "提交说明"

# 查看提交历史
git log                    # 详细历史
git log --oneline          # 一行显示一条记录
git log --oneline --graph  # 图形化显示分支
git log -n 5               # 只看最近 5 条

# 查看某次提交的详情
git show <commit-id>
```

---

## 五、远程仓库操作

```bash
# 添加远程仓库
git remote add origin <仓库地址>

# 查看远程仓库
git remote -v

# 推送到远程仓库
git push origin main       # 推送到 main 分支
git push -u origin main    # 首次推送并建立跟踪关系

# 拉取远程更新
git pull origin main       # 拉取并合并
git fetch origin           # 只拉取不合并

# 删除远程分支
git push origin --delete <分支名>
```

---

## 六、分支操作

```bash
# 查看分支
git branch                 # 查看本地分支
git branch -a              # 查看所有分支（含远程）

# 创建分支
git branch <分支名>

# 切换分支
git checkout <分支名>
git switch <分支名>         # Git 2.23+ 推荐使用

# 创建并切换到新分支
git checkout -b <分支名>
git switch -c <分支名>      # Git 2.23+ 推荐使用

# 删除分支
git branch -d <分支名>      # 安全删除（已合并的分支）
git branch -D <分支名>      # 强制删除

# 重命名分支
git branch -m <旧名称> <新名称>
```

---

## 七、撤销与回退

```bash
# 撤销工作区的修改（还没 add）
git checkout -- <文件名>
git restore <文件名>        # Git 2.23+ 推荐使用

# 取消暂存（add 了但没 commit）
git reset HEAD <文件名>
git restore --staged <文件名>  # Git 2.23+ 推荐使用

# 撤销最近一次 commit（保留修改）
git reset --soft HEAD~1

# 撤销最近一次 commit（不保留修改）
git reset --hard HEAD~1

# 回退到指定版本
git reset --hard <commit-id>

# 安全地撤销某次提交（生成新的反向提交）
git revert <commit-id>
```

---

## 八、暂存修改 (Stash)

```bash
# 暂存当前修改
git stash

# 暂存时添加说明
git stash push -m "说明文字"

# 查看暂存列表
git stash list

# 恢复最近一次暂存
git stash pop               # 恢复并删除该 stash
git stash apply             # 恢复但不删除 stash

# 恢复指定暂存
git stash apply stash@{0}

# 删除某个暂存
git stash drop stash@{0}

# 清空所有暂存
git stash clear
```

---

## 九、标签 (Tag)

```bash
# 查看所有标签
git tag

# 创建轻量标签
git tag v1.0.0

# 创建附注标签
git tag -a v1.0.0 -m "版本 1.0.0 发布"

# 给之前的提交打标签
git tag v0.9.0 <commit-id>

# 推送标签到远程
git push origin v1.0.0           # 推送单个标签
git push origin --tags           # 推送所有标签

# 删除本地标签
git tag -d v1.0.0

# 删除远程标签
git push origin --delete v1.0.0
```

---

## 十、查看差异

```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最新 commit 的差异
git diff --staged
git diff --cached

# 查看两个分支的差异
git diff <分支1> <分支2>

# 查看某个文件的修改历史
git log -p <文件名>

# 查看每行代码是谁写的
git blame <文件名>
```

---

## 十一、合并与变基

```bash
# 将指定分支合并到当前分支
git merge <分支名>

# 变基（将当前分支的提交接到目标分支后面）
git rebase <目标分支>

# 中止合并
git merge --abort

# 中止变基
git rebase --abort

# 交互式 rebase（合并多个 commit 为一个）
git rebase -i HEAD~3
```

---

## 十二、常见场景速查

| 场景 | 命令 |
|------|------|
| 想丢弃本地所有修改 | `git restore .` |
| commit 信息写错了 | `git commit --amend -m "新信息"` |
| 漏了文件没 add 进上次 commit | `git add <文件>` → `git commit --amend --no-edit` |
| 想切分支但当前有未保存的修改 | `git stash` → 切分支 → 回来后 `git stash pop` |
| 想回到某个历史版本看看 | `git checkout <commit-id>` |
| 想看某个文件某一行是谁改的 | `git blame <文件>` |
| 查看某个 commit 改了哪些文件 | `git show --stat <commit-id>` |
| 查看某次提交的详细内容 | `git show <commit-id>` |
| 不想追踪某个文件了 | `git rm --cached <文件>` |

---

## 十三、.gitignore 文件

在项目根目录创建 `.gitignore` 文件，写入要忽略的文件模式：

```gitignore
# 忽略所有 .log 文件
*.log

# 忽略 node_modules 目录
node_modules/

# 忽略 .env 文件
.env

# 忽略 dist 目录
dist/

# 但保留特定文件（! 表示例外）
!important.log
```

---

## 十四、常用全局配置别名

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```

配置后可以用 `git st` 代替 `git status`、`git lg` 显示漂亮的提交历史。

---

## 十五、最佳实践建议

1. **频繁提交**：完成一个小功能就 commit，不要把大量修改堆在一次提交里
2. **清晰的 commit message**：用动词开头，简明扼要，如 "添加用户登录功能"
3. **分支开发**：不要在 main 分支直接开发，每个功能／修复使用独立分支
4. **提交前检查**：`git status` + `git diff` 确认改了什么再 commit
5. **pull 前先 commit**：拉远程代码前确保本地修改已提交或 stash
6. **不要 force push 到共享分支**：`--force` 会覆盖他人的提交，非常危险
