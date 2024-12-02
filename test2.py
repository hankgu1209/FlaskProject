from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
app.config['LANGUAGES'] = ['en', 'es', 'de']  # 你应用支持的语言列表

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(debug=True)
