from flask import Flask, request#从flask包中导入Flask类
from config import Config
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
import pymysql
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from logging.handlers import RotatingFileHandler
import logging
import os
from flask_babel import Babel
pymysql.install_as_MySQLdb()



app = Flask(__name__)#将Flask类的实例 赋值给名为 app 的变量。这个实例成为app包的成员。
app.config.from_object(Config)
login = LoginManager(app)
login.login_view='login'
# print('等会谁（哪个包或模块）在使用我：',__name__)
mail = Mail(app)
# bootstrap 初始化
bootstrp = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)

db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象


@babel.localeselector
def get_locale():
    # 自动根据客户端请求选择合适的语言
    return request.accept_languages.best_match(app.config['LANGUAGES'])

#从app包中导入模块routes
from app import routes,models,errors
#注：上面两个app是完全不同的东西。两者都是纯粹约定俗成的命名，可重命名其他内容。


if not app.debug:
    # ...

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')



