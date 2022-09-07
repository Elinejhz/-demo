
from sqlalchemy import *

from server import db


class TestcaseDo(db.Model):
    # 表名
    __tablename__ = "testcase"
    # 用例ID 用例的唯 一标识
    id = db.Column(Integer, primary_key=True)
    # 用例的标题 或者文件名,限定 255个字符 ，不为空，并且唯一
    case_title = db.Column(String(255), nullable=False, unique=True)
    # 备注
    remark = db.Column(String(255))
    # 备注2
    # remark2 =
    # 将对象转换为字典的方法
    def as_dict(self):
        return {"id": self.id, "case_title": self.case_title, "remark": self.remark}

#
# if __name__ == '__main__':
#     db.create_all()