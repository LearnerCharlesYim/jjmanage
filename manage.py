from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from models import HrUser,Project,Employee
import pymysql

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_hr_user(username,password,email):
    """
    命令行生成hr用户 python manage.py create_hr_user -u 用户名 -p 密码 -e 邮箱
    :param username:
    :param password:
    :param email:
    :return:
    """
    user = HrUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print('Hr用户添加成功！')


@manager.command
def create_database():
    # '''创建数据库'''
    # 打开数据库连接，不需要指定数据库，因为需要创建数据库
    conn = pymysql.connect(host="127.0.0.1", user="root", password="root")
    # 获取游标
    cursor = conn.cursor()
    # 创建数据库jjmanage
    cursor.execute('CREATE DATABASE IF NOT EXISTS jjmanage DEFAULT CHARSET utf8 COLLATE utf8_general_ci;')
    cursor.close()  # 先关闭游标
    conn.close()  # 再关闭数据库连接
    print('创建数据库成功！')


if __name__ == '__main__':
    manager.run()
