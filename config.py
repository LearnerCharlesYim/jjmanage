DEBUG = True

#配置数据库
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'jjmanage'
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

HR_USER_ID = 'USER_ID'
SECRET_KEY = 'abcdefghijklnmopqrstuvwx'
# flask-paginate的相关配置
PER_PAGE = 10