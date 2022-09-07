
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session


app = Flask(__name__)
api = Api(app)

username = "root"
password = "root123"
server = "127.0.0.1"
database = "flask_test0823"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{server}/{database}?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# SQLAlchemy 绑定 app
db = SQLAlchemy(app)
db_session: Session = db.session

def add_router():
    from controller.testcase_controller import testcase_ns
    api.add_namespace(testcase_ns, "/testcase")

if __name__ == '__main__':
    add_router()
    app.run(debug=True)

