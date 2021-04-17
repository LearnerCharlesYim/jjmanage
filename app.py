from flask import Flask,render_template,request,session,g,redirect,url_for
import config
from exts import db
from forms import LoginForm,SettingsForm,AddEmployeeForm
from models import HrUser,Project,Employee
import restful
from functools import wraps


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.before_request
def before_request():
    if config.HR_USER_ID in session:
        user_id = session.get(config.HR_USER_ID)
        user = HrUser.query.get(user_id)
        if user:
            g.user = user


def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if config.HR_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return inner


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = HrUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.HR_USER_ID] = user.id
                if remember:
                    # 默认过期时间31天
                    session.permanent = True
                return restful.success()
            else:
                return restful.params_error(message='邮箱或密码错误')
        else:
            return restful.params_error(message=form.get_error())



@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/logout/')
@login_required
def logout():
    del session[config.HR_USER_ID]
    return redirect(url_for('login'))


@app.route('/profile/')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/settings/',methods=['GET','POST'])
@login_required
def settings():
    if request.method == 'GET':
        return render_template('settings.html')
    else:
        form = SettingsForm(request.form)
        if form.validate():
            username = form.username.data
            email = form.email.data
            user = HrUser.query.get(g.user.id)
            user.username = username
            user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=form.get_error())


@app.route('/manage/',methods=['GET','POST'])
@login_required
def manage():
    if request.method == 'GET':
        projects = Project.query.all()
        return render_template('project_manage.html',projects=projects)
    else:
        project_id = request.form.get('project')
        user_id = request.form.get('user_id')
        user = HrUser.query.get(int(user_id))
        if project_id:
            project = Project.query.get(int(project_id))
            project.hr_user = user
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message='请选择可选项目！')


@app.route('/employee/',methods=['GET','POST'])
@login_required
def employee():
    if request.method == 'GET':
        employees = Employee.query.all()
        return render_template('employee.html',employees=employees)
    else:
        pass

@app.route('/employee/add/',methods=['GET','POST'])
@login_required
def add_employee():
    projects = Project.query.all()
    if request.method == 'GET':
        return render_template('add_employee.html',projects=projects)
    else:
        form = AddEmployeeForm(request.form)
        if form.validate():
            name = form.name.data
            age = form.age.data
            sex = form.sex.data
            hometown = form.hometown.data
            working_age = form.working_age.data
            education = form.education.data
            certificate = form.certificate.data
            resume_score = form.resume_score.data
            interview_score = form.interview_score.data
            project_id = form.project.data
            hr_id = g.user.id
            employee = Employee(name=name,age=age,sex=sex,hometown=hometown,working_age=working_age,education=education,certificate=certificate,resume_score=resume_score,interview_score=interview_score,project_id=project_id,total_score=resume_score+interview_score,hr_id=hr_id)
            db.session.add(employee)
            db.session.commit()
            return restful.success()

        else:
            return restful.params_error(form.get_error())


if __name__ == '__main__':
    app.run()
