#!/bin/bash

# 激活虚拟环境
c

# 确保环境变量正确
export PATH="$HOME/jupyterhub/venv/bin:$PATH"

# 启动服务
jupyterhub -f ~/jupyterhub/jupyterhub_config.py 