
from do.testcase_do import TestcaseDo
from server import db_session


class TestcaseDao:
    def save(self, testcase_entity:TestcaseDo):
        db_session.add(testcase_entity)
        db_session.commit()

    def delete(self,testcase_id):
        db_session.query(TestcaseDo).filter_by(id=testcase_id).delete()
        db_session.commit()


    def get(self, testcase_id)->TestcaseDo:
        # db_session
        # TestcaseDao.query
        return db_session.query(TestcaseDo).filter_by(id=testcase_id).first()

    def get_all_rows(self, testcase_row)->TestcaseDo:
        return db_session.query(TestcaseDo).filter_by(case_title=testcase_row).all()

    def get_order_desc(self, testcase_column_title):
        return db_session.query(TestcaseDo).order_by(testcase_column_title.desc()).first()
        # return db_session.query(TestcaseDo).order_by(f'TestcaseDo.{testcase_column_title}'.desc()).first()

    def get_all(self):
        return db_session.query(TestcaseDo).all()

    def update(self, testcase_id, update_testcase_data):
        db_session.query(TestcaseDo).filter_by(id=testcase_id).update(update_testcase_data)
        db_session.commit()

if __name__ == '__main__':
    pass
    # get_desc = TestcaseDao().get_order_desc(testcase_column_title=TestcaseDo.id)
    # print(get_desc)