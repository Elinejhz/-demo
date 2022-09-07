
from sqlalchemy import *

from server import db


class BuildDo(db.Model):
    # 表名
    __tablename__ = "build"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 255个字符 ，不为空，并且唯一
    testcase_info = db.Column(String(255), nullable=False, unique=True)
    # 备注
    report = db.Column(String(255))

# if __name__ == '__main__':
#     db.create_all()