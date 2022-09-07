
from typing import List

from dao.testcase_dao import TestcaseDao
from do.testcase_do import TestcaseDo

testcase_dao = TestcaseDao()

class TestcaseService:
    """
    测试用例的服务层
    """
    # 问题： 目前的参数和实体类的每个字段都是强关联的，如果实体类熙增，或者删除字段，那么
    # 参数也要跟着改变
    def save(self, testcase_entity:TestcaseDo):
        """
        1. 查询用例，是否存在，如果存在，则不新增
        2. 反之就做新增操作
        :return:
        """
        # testcase_id = 1
        # 查询用例是否存在，如果存在，则不需要新增，返回错误
        # 判断传入的参数是否为对象，若是字典，则将字典转换成对象
        if isinstance(testcase_entity, dict):
            testcase_entity = TestcaseDo(**testcase_entity)
        if self.get(testcase_entity.id):
            return False
        else:
            # 如果不存在就做新增操作
            testcase_dao.save(testcase_entity)
            return True

    def delete(self, testcase_id):
        if self.get(testcase_id):
            testcase_dao.delete(testcase_id)
        else:
            return False

    def get(self, testcase_id)->TestcaseDo:
        return testcase_dao.get(testcase_id)

    def get_all_rows(self, testcase_row)->TestcaseDo:
        return testcase_dao.get_all_rows(testcase_row)

    def get_order_desc(self, testcase_column_title):
        return testcase_dao.get_order_desc(testcase_column_title)

    def get_all(self)->List[TestcaseDo]:
        return testcase_dao.get_all()

    def update(self, update_testcase:dict):
        testcase_id = update_testcase.get("id")
        if self.get(testcase_id):
            testcase_dao.update(testcase_id, update_testcase)
        else:
            return False


