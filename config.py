# 项目配置文件

# 基础配置


# 设置cookie加密混淆密钥
SECRET_KEY = '1234567890ABCDEFG'

# 配置数据库连接
HOSTNAME = 'localhost'
PORT = '3306'
USERNAME = 'root'
PASSWORD = '123456Zlx'
DATABASE = 'qasys'
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
SQLALCHEMY_DATABASE_URI = DB_URL

# 邮箱配置(去第三方设置开启邮箱服务)
# 授权码:ldzlxrkliejmebjc(2492471056@qq.com)
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2492471056@qq.com"
MAIL_PASSWORD = "ldzlxrkliejmebjc"
MAIL_DEFAULT_SENDER = "2492471056@qq.com"