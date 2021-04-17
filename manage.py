from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app
from exts import db
from models import HrUser,Project,Employee

manager = Manager(app)

Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-e','--email',dest='email')
def create_hr_user(username,password,email):
    user = HrUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print('Hr用户添加成功！')


if __name__ == '__main__':
    manager.run()
