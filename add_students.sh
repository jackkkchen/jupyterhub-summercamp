#!/bin/bash

# 读取学生列表文件
while IFS= read -r username
do
    # 创建系统用户
    sudo useradd -m "$username"
    # 设置初始密码（建议后续要求学生修改）
    echo "${username}:initial_password" | sudo chpasswd
    
    # 创建JupyterHub工作目录
    sudo mkdir -p "/home/ecs-user/jupyterhub/users/$username"
    sudo chown "$username:$username" "/home/ecs-user/jupyterhub/users/$username"
    sudo chmod 755 "/home/ecs-user/jupyterhub/users/$username"
done < student_list.txt 




# 重启服务
# sudo systemctl daemon-reload
# sudo systemctl restart jupyterhub

# 检查服务状态
# sudo systemctl status jupyterhub