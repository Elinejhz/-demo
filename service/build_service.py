
from dao.build_dao import BuildDao
from do.build_do import BuildDo
from service.testcase_service import TestcaseService
from utils.log_util import logger

build_dao = BuildDao()
testcase_service = TestcaseService()

class BuildService:

    def get_all(self):
        return build_dao.get_all()

    # save 方法不会对controller暴漏。
    def __save(self, build_entity:BuildDo):
        build_dao.save(build_entity)

    def execute(self, testcase_id):
        """
        执行测试用例，产生构建记录
        """
        # 1. 传入测试用例的id
        # 2. 获取对应的用例信息
        testcase_entity = testcase_service.get(testcase_id)
        testcase_info = testcase_entity.case_title
        # 3. 执行用例：先使用log代替，下节课优化为真实过程
        logger.info(f"执行的测试用例为{testcase_info}")
        # 4. 获取报告：先使用log代替，下节课优化为真实过程
        report = testcase_entity.remark
        logger.info(f"测试报告为{report}")
        # 5. 保存测试记录
        build_entity = BuildDo(testcase_info=testcase_info, report=report)
        self.__save(build_entity)