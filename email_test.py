# 测试通过gmail 向对方发送邮件

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮件服务
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False  # 确保未启用 SSL，因为我们使用的是 TLS
app.config['MAIL_USERNAME'] = 'xxx@gmail.com'  # 替换为你的 Gmail 地址
app.config['MAIL_PASSWORD'] = 'xxxxx'  # 替换为你的 Gmail 应用专用密码
app.config['MAIL_DEFAULT_SENDER'] = 'xxx@gmail.com'  # 替换为默认发送者地址

mail = Mail(app)

@app.route('/send_email')
def send_email():
    try:
        msg = Message("Hello from Flask", recipients=['xxx@hotmail.com'])  # 替换为接收者地址
        msg.body = f"Hello this is a test email sent from {app.config['MAIL_USERNAME']}"
        mail.send(msg)
        return "Email sent successfully!"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)


