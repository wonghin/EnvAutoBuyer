from others_code.login import Login


username = '******'  # 账号
password = '******.'  # 密码
# 初始化Login类
login = Login(username, password)
# 使用淘宝账号或手机号登录
login.original()
# 使用新浪微博账号登录
# login.sina()