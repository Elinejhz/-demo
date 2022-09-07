
from do.build_do import BuildDo
from server import db_session


class BuildDao:
    def get_all(self):
        return db_session.query(BuildDo).all()

    def save(self, build_entity:BuildDo):
        db_session.add(build_entity)
        db_session.commit()

    # def excute(self):