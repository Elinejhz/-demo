
from do.testcase_do import TestcaseDo
from service.testcase_service import TestcaseService


class TestTestcaseService:
    def setup_class(self):
        self.testcase = TestcaseService()

    def test_save(self):
        testcase = TestcaseDo(id=2, case_title="test22.py", remark="test12222")
        res = self.testcase.save(testcase)
        assert res != None

    def test_delete(self):
        self.testcase.delete(2)
        res = self.testcase.get(2)
        assert res == None

    def test_get(self):
        res = self.testcase.get(2)
        print(res)

        # assert False

    def test_get_all(self):
        print(self.testcase.get_all())  # assert False

    def test_update(self):
        self.testcase.update({"id": 2, "remark": "更新操作"})
        res = self.testcase.get(2)
        assert res.remark == "更新操作"