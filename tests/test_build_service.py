
from do.build_do import BuildDo
from service.build_service import BuildService


class TestBuildService:

    def setup_class(self):
        self.build = BuildService()

    def test_get_all(self):
        print(self.build.get_all())

    def test_save(self):
        build = BuildDo(testcase_info="testcase111", report="测试报告1")
        self.build.__save(build)

    def test_execute(self):
        self.build.execute(1)