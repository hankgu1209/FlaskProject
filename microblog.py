from app import app
from app.forms import LoginForm
from app.models import  User, Post, db

@app.shell_context_processor
def make_shell_context():
    return {'db':db,'User':User,'Post':Post}

if __name__ == '__main__':
    app.run(debug=True)