c = get_config()

# 基础配置
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.hub_port = 8081
c.JupyterHub.hub_ip = '127.0.0.1'

# cookie 配置
c.JupyterHub.cookie_secret_file = '/home/ecs-user/jupyterhub/jupyterhub_cookie_secret'
c.ConfigurableHTTPProxy.auth_token = '/home/ecs-user/jupyterhub/proxy_auth_token'

# 认证配置
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'
c.DummyAuthenticator.password = "jupyterhub123"

# Spawner 配置
c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'
c.Spawner.notebook_dir = '/home/ecs-user/jupyterhub'  # 先设置一个基础目录
c.Spawner.default_url = '/lab'

# 用户配置
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allowed_users = {
    'admin', 
    'teacher1', 'teacher2', 'teacher3',
    'student001'
}

# 角色配置
c.JupyterHub.load_roles = [
    {
        'name': 'teacher',
        'scopes': [
            'access:servers',
            'access:services',
            'servers',
            'users',
            'read:users:activity',
            'read:users:name',
            'read:users:groups',
            'list:users',
            'admin:groups',
        ],
        'users': ['teacher1', 'teacher2', 'teacher3']
    },
    {
        'name': 'student',
        'scopes': [
            'access:servers',
            'access:services',
            'self',
        ],
        'users': ['student001']
    }
]

# 调试设置
c.JupyterHub.debug_db = True
c.JupyterHub.log_level = 'DEBUG'
c.Spawner.debug = True

# 环境变量
c.Spawner.env = {
    'PATH': '/home/ecs-user/jupyterhub/venv/bin:/usr/local/bin:/usr/bin:/bin',
    'JUPYTER_PATH': '/home/ecs-user/jupyterhub/venv/share/jupyter',
    'JUPYTER_RUNTIME_DIR': '/tmp/jupyter-runtime'
} 