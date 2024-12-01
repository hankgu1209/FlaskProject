import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://root:GUcx0106@localhost/microblog_user'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 10
    # email_pwd = os.getenv('email_pwd')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PWD')
    # Email settings
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'

    # 端口配置
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))  # 默认使用 587 端口 (TLS)

    # 使用 TLS 或 SSL
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False') == 'True'

    # 对于 Gmail，TLS 和端口 587 是推荐的配置
    # 确保 MAIL_USE_TLS 为 True，MAIL_USE_SSL 为 False
    if MAIL_USE_TLS and MAIL_USE_SSL:
        raise ValueError("Cannot use both TLS and SSL at the same time.")
