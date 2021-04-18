DEBUG = True

#配置数据库
DB_USERNAME = 'root'
#密码按照mysql设置的密码填写
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
#数据库名按照命令行生成的数据库同名
DB_NAME = 'jjmanage'

#链接数据库
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI

TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

HR_USER_ID = 'USER_ID'
SECRET_KEY = 'abcdefghijklnmopqrstuvwx'
