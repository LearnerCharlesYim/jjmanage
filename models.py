from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
import enum

class GenderEnum(enum.Enum):
    """
    性别模型
    :GenderEnum.MALE.name = MALE
    :GenderEnum.MALE.value = 1
    """
    MALE = 1
    FEMAIL = 2
    UNKNOW = 3


class EducationEnum(enum.Enum):
    """
    学历模型
    """
    DOCTOR = 1           #博士学历
    MASTER = 2           #研究生学历
    BACHELOR = 3         #本科
    HIGHSCHOOL = 4       #高中学历
    MIDDLESCHOOL = 5     #初中学历
    UNKNOW = 6


#Hr模型
class HrUser(db.Model):
    __tabalename__ = 'hr_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    _password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now())

    project_id = db.Column(db.Integer,db.ForeignKey('project.id'),unique=True)
    # ORM层面外键映射
    project = db.relationship('Project', backref=db.backref('hr_user',uselist=False))

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw_password):
        """
         密码加密
        """
        self._password = generate_password_hash(raw_password)

    def check_password(self,raw_password):
        """
        检查密码是否正确函数
        :param raw_password:
        :return:
        """
        result = check_password_hash(self.password,raw_password)
        return result


#项目模型
class Project(db.Model):
    __tabalename__ = 'project'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(200),nullable=False)


#应聘人员模型
class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    sex = db.Column(db.Enum(GenderEnum),default=GenderEnum.UNKNOW)
    hometown = db.Column(db.String(100))
    working_age = db.Column(db.Integer)
    education = db.Column(db.Enum(EducationEnum),default=EducationEnum.UNKNOW)
    certificate = db.Column(db.String(1000))
    resume_score = db.Column(db.Integer)
    interview_score = db.Column(db.Integer)
    total_score = db.Column(db.Integer)
    join_time = db.Column(db.DateTime, default=datetime.now())
    #定义外键
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    hr_id = db.Column(db.Integer,db.ForeignKey('hr_user.id'))

    #ORM层面外键映射
    project = db.relationship('Project', backref=db.backref('emploees',cascade='all'))
    hr = db.relationship('HrUser', backref=db.backref('emploees',cascade='all'))