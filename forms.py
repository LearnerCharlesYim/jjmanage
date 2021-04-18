from wtforms import Form
from wtforms import StringField,IntegerField
from wtforms.validators import Email,InputRequired,Length,EqualTo

class BaseForm(Form):
    """
    定义基表单返回验证错误信息
    """
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message


class LoginForm(BaseForm):
    """
    登录表单
    """
    email = StringField(validators=[Email(message='请输入正确邮箱格式'),InputRequired(message='请输入邮箱')])
    password = StringField(validators=[Length(6,20,message='请输入正确格式密码(6-20位字符)')])
    remember = IntegerField()


class SettingsForm(BaseForm):
    """
    设置个人信息表单
    """
    username = StringField(validators=[InputRequired(message='请输入用户名')])
    email = StringField(validators=[Email(message='请输入正确邮箱格式'),InputRequired(message='请输入邮箱')])


class AddEmployeeForm(BaseForm):
    """
    添加应聘表单
    """
    name = StringField(validators=[InputRequired(message='请输入姓名')])
    age = IntegerField(validators=[InputRequired(message='请输入年龄')])
    sex = StringField(validators=[InputRequired(message='请选择性别')])
    hometown = StringField(validators=[InputRequired(message='请输入籍贯')])
    working_age = StringField(validators=[InputRequired(message='请输入从业年龄')])
    education = StringField(validators=[InputRequired(message='请选择学历')])
    certificate = StringField()
    resume_score = IntegerField(validators=[InputRequired(message='请输入简历评分')])
    interview_score = IntegerField(validators=[InputRequired(message='请输入面试评分')])
    project = IntegerField(validators=[InputRequired(message='请选择应聘项目')])


class EditEmployeeForm(BaseForm):
    """
    修改应聘信息表单
    """
    employee_id = IntegerField(validators=[InputRequired(message='没有这个应聘者')])
    name = StringField(validators=[InputRequired(message='请输入姓名')])
    age = IntegerField(validators=[InputRequired(message='请输入年龄')])
    sex = StringField(validators=[InputRequired(message='请选择性别')])
    hometown = StringField(validators=[InputRequired(message='请输入籍贯')])
    working_age = StringField(validators=[InputRequired(message='请输入从业年龄')])
    education = StringField(validators=[InputRequired(message='请选择学历')])
    certificate = StringField()
    resume_score = IntegerField(validators=[InputRequired(message='请输入简历评分')])
    interview_score = IntegerField(validators=[InputRequired(message='请输入面试评分')])
    total_score = IntegerField(validators=[InputRequired(message='请输入总分')])