# JupyterHub 教学平台部署指南

## 1. 平台简介
这是一个基于 JupyterHub 的在线 Python 教学平台，支持多用户同时在线学习和练习 Python 编程。平台实现了教师和学生的角色分离，支持课程内容管理、作业发布和提交等功能。

## 2. 用户角色和权限

### 2.1 管理员 (admin)
- 完整的系统管理权限
- 可以添加/删除用户
- 可以查看所有用户的活动
- 可以访问和修改所有课程内容
- 默认账号: admin，密码: jupyterhub123

### 2.2 教师用户 (teacher1, teacher2, teacher3)
- 可以访问所有课程内容
- 可以在 source 目录编写和修改教材
- 可以查看学生活动和提交的作业
- 可以管理学生组
- 无法添加新用户（需要管理员权限）
- 默认密码: jupyterhub123

### 2.3 学生用户 (student001 等)
- 只能访问 release 目录下的教程和练习
- 可以在个人工作空间完成作业
- 可以提交作业到 submitted 目录
- 无法访问其他学生的工作空间
- 默认密码: jupyterhub123

## 3. 目录结构
```
/home/ecs-user/jupyterhub/courses/
├── python101/
│   ├── source/                 # 教师可见（含答案）
│   │   ├── tutorial/
│   │   └── exercises/
│   ├── release/               # 学生可见（无答案）
│   │   ├── tutorial/
│   │   └── exercises/
│   ├── submitted/            # 学生作业提交目录
│   └── feedback/             # 教师反馈目录
└── python102/
    └── ...
```

## 4. 作业流程

### 4.1 教师端
1. 在 source 目录编写教材和练习（包含答案）
2. 将无答案版本复制到 release 目录
3. 在 feedback 目录提供作业反馈

### 4.2 学生端
1. 访问 release 目录查看教程和练习
2. 在个人工作空间完成练习
3. 将完成的作业提交到 submitted 目录

## 5. 自动化功能
- 自动用户角色分配
- 自动目录权限管理
- 作业自动归档
- 支持 Jupyter Notebook 自动评分（待实现）

## 6. 安装和配置

### 6.1 安装必要的依赖
```bash
sudo apt update
sudo apt install python3 python3-pip nodejs npm
```

### 6.2 安装 JupyterHub 和 Jupyter Lab
```bash
sudo python3 -m pip install jupyterhub jupyterlab
sudo npm install -g configurable-http-proxy
```

### 6.3 创建配置文件
```bash
mkdir -p /home/ecs-user/jupyterhub
cd /home/ecs-user/jupyterhub
sudo jupyterhub --generate-config
```

## 7. 使用指南

### 7.1 教师使用指南
1. 使用教师账号登录系统
2. 在 source 目录开发课程内容
3. 使用提供的工具将内容发布到 release
4. 在 submitted 目录查看和评阅学生作业

### 7.2 学生使用指南
1. 使用学生账号登录系统
2. 在 release 目录学习课程内容
3. 在个人工作空间完成练习
4. 将作业提交到 submitted 目录

## 8. 注意事项
- 定期备份 source 目录的内容
- 保持 release 目录内容的更新
- 定期清理 submitted 目录
- 确保 cookie_secret 文件权限正确

## 9. 未来计划
- 添加自动作业评分功能
- 实现课程进度追踪
- 添加学生成绩管理
- 支持在线考试功能

## 10. 常见问题

### 10.1 网页无法访问（cookie secret 文件丢失）
1. 停止服务
```bash
sudo systemctl stop jupyterhub
```

2. 删除现有的 cookie secret 文件
```bash
sudo rm -f /home/ecs-user/jupyterhub/jupyterhub_cookie_secret
sudo rm -f /home/ecs-user/jupyterhub/proxy_auth_token
```

3. 重新创建文件并设置严格的权限
```bash
sudo touch /home/ecs-user/jupyterhub/jupyterhub_cookie_secret
sudo touch /home/ecs-user/jupyterhub/proxy_auth_token
```

4. 生成新的 secret
```bash
sudo openssl rand -hex 32 | sudo tee /home/ecs-user/jupyterhub/jupyterhub_cookie_secret > /dev/null
sudo openssl rand -hex 32 | sudo tee /home/ecs-user/jupyterhub/proxy_auth_token > /dev/null
```

5. 设置正确的所有权和权限
```bash
sudo chown root:root /home/ecs-user/jupyterhub/jupyterhub_cookie_secret
sudo chown root:root /home/ecs-user/jupyterhub/proxy_auth_token
sudo chmod 400 /home/ecs-user/jupyterhub/jupyterhub_cookie_secret
sudo chmod 400 /home/ecs-user/jupyterhub/proxy_auth_token
```

6. 重启服务
```bash
sudo systemctl daemon-reload
sudo systemctl restart jupyterhub
```

7. 检查服务状态
```bash
sudo systemctl status jupyterhub
```

### 10.2 配置 HTTPS（推荐）
为了提高安全性，建议配置 HTTPS：
1. 获取 SSL 证书
2. 在配置文件中添加证书路径
3. 设置强制 HTTPS
