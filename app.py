# 项目主程序
from flask import Flask, session, g, Response
import config
from exts import db, mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)

# 1.绑定配置文件
app.config.from_object(config)

# 2.db,mail绑定app
db.init_app(app)
mail.init_app(app)

# 3.模型迁移(+三部曲)
migrate= Migrate(app,db)

# 4.注册蓝图（blueprint:使路由模块化）
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

# 安装脚本路由
@app.route('/install.sh')
def install_sh():
    # 返回 install.sh 内容，设置正确的 Content-Type
    return Response(
        "
        echo 'hello!'
        ",
        mimetype='text/x-shellscript',
        headers={
            'Content-Disposition': 'inline; filename=install.sh'
        }
    )

# 钩子函数(hook)：插到视图函数之前，检查有没有登陆过，登陆过就直接跳转
# hook1
@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

# hook2
@app.context_processor
def my_context_processor():
    return {"user": g.user}

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
