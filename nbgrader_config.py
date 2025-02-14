c = get_config()

# 课程ID
c.CourseDirectory.course_id = "python101"

# 课程根目录
c.CourseDirectory.root = '/home/ecs-user/jupyterhub/courses/python101'

# 配置提交目录
c.Exchange.root = '/home/ecs-user/jupyterhub/courses/python101'
c.Exchange.submit_directory = '/home/ecs-user/jupyterhub/courses/python101/submitted'

# 配置用户权限
c.CourseDirectory.student_id_exclude = ['admin', 'teacher1']

# 启用必要的扩展
c.NbGrader.logfile = '/home/ecs-user/jupyterhub/nbgrader.log'

# 设置允许访问nbgrader的用户
c.Authenticator.admin_users = {'admin'}
c.Authenticator.allowed_users = {'teacher1', 'student1', 'student2'}

# 配置教师用户
c.FormgradeApp.authenticator_class = "nbgrader.auth.SimpleAuth"
c.FormgradeApp.authorized_users = {'teacher1'} 