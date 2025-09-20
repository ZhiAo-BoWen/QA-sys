from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session
from flask_mail import Message
from exts import mail, db
import string
import random
from models import UserModel, EmailCaptchaModel
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

# 参数：名称，对象，路由头
bp = Blueprint("auth", __name__, url_prefix="/auth")

# 为蓝图对象添加路由
@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库在不存在！")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password,password):
                # cookie:不适合存储太多数据，只适合存储少量数据，一般用来记录用户授权
                # flask中的session，是加密存储在cookie中的
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误！")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.login"))


# GET:从服务器获得数据
# POST:将客户端数据提交给服务器
@bp.route("/register",methods=['GET','POST'])
def register():
    # 渲染模板时注意修改html静态文件加载,使用jinjia.url_for('static',filename=path)
    # 抽取基模板base.html，改造其他网页为jinjia格式
    # bootstrap:前端框架,用于前后端未分离
    if request.method == 'GET':
        return render_template("register.html")
    else:   
        # 验证邮箱和邮箱验证码是否匹配
        # 表单验证:flask-wtf:wtforms
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # url_for:视图函数转url
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

# 退出登录
@bp.route("\logout")
def logout():
    session.clear()
    return redirect("/")


# 没有指定请求方式，默认GET
@bp.route("/captcha/email",)
def get_email_captcha():
    # 使用字符串查询传参
    email = request.args.get("email")
    # 生成验证码
    source = string.digits*4   #"0123456789"*4
    captcha = random.sample(source,4)
    captcha = "".join(captcha)
    message = Message(subject="QA-sys验证码",recipients=[email],body=f"您的验证码为 {captcha} ：来自于QA-sys")
    mail.send(message)
    # 保存邮箱与验证码的匹配信息
    # 建议存入缓存（memcached）
    # 这里使用数据库存储
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API:统一返回格式(前后端数据接口格式)
    # {code:200/400/500,message:"",data:{}}
    return jsonify({"code":200,"message":"","data":None})

@bp.route("/mail/test")
def mail_test():
    # subject:邮件名
    # recipients:收件人(列表)
    # body:邮件内容
    recipients=["1913774864@qq.com"]
    message = Message(subject="邮箱测试",recipients=recipients,body="这是一条测试邮件：来自于QA-sys")
    mail.send(message)
    return f"邮件发送成功至{recipients}"