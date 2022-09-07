
from flask import request
from flask_restx import Namespace, Resource

from do.testcase_do import TestcaseDo
from service.testcase_service import TestcaseService
from utils.log_util import logger

testcase_ns = Namespace("case", description="用例管理")
testcase_service = TestcaseService()

@testcase_ns.route("")
class TestcaseController(Resource):

    get_parser = testcase_ns.parser()
    get_parser.add_argument("id",type=int, location="args")
    @testcase_ns.expect(get_parser)
    def get(self):
        testcase_id = request.args.get("id")
        if testcase_id:
            data = [testcase_service.get(testcase_id).as_dict()]
        else:
            testcase_entity_list = testcase_service.get_all()
            logger.info(type(testcase_entity_list))
            data = [testcase.as_dict() for testcase in testcase_entity_list]
        return {"msg": data}

    post_paresr = testcase_ns.parser()
    post_paresr.add_argument("id", type=int, required=True, location="json")
    post_paresr.add_argument("case_title", type=str, required=True, location="json")
    post_paresr.add_argument("remark", type=str, location="json")

    @testcase_ns.expect(post_paresr)
    def post(self):
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        case_id = case_data.get("id")
        case_title = case_data.get("case_title")
        # 查询数据库，查看是否有记录
        exists = testcase_service.get(case_id)
        logger.info(f"查询表结果：{exists}")
        logger.info(f"转换结果：{case_data.keys()}")
        # 如果不存在，则添加这条记录到库中
        # 如果存在，不执行新增操作， 返回 40001错误码
        # if not exists:
        #     testcase = testcase_service.save(case_data)
        #     logger.info(f"将要存储的内容为<======{testcase}")
        #     return {"code": 0, "msg": f"case id {case_id} success add."}
        # else:
        #     return {"code": 40001, "msg": "case is exists"}
        # 1) 若case_id为空，返回"ID不能为空"
        if case_id == '':
            return "ID cannot be empty."
        else:
            # 查询数据库，查看是否有记录
            exists_id = testcase_service.get(case_id)
            exists_titles = testcase_service.get_all_rows(case_title)
            exists_id_latest = testcase_service.get_order_desc(TestcaseDo.id)
            logger.info(f"根据id查询表结果为：{exists_id}")
            logger.info(f"根据case_title查询表结果为：{exists_titles}")
            logger.info(f"查询表中最新一条数据的id为：{exists_id_latest.id}")
            # 2) 若根据id查询结果中case_title不为空，返回"case_title已存在"
            if exists_titles:
                return f"case_title {case_title} already exists in the table."
            # 2.1) 若根据id查询结果为空，则添加这条记录到库中
            # 2.2) 若id存在，不执行新增操作， 返回 40001错误码
            else:
                if not exists_id:
                    testcase = testcase_service.save(case_data)
                    logger.info(f"将要存储的内容为<======{testcase}")
                    # 2.1.1) 若case_id为0，落库时，系统根据当前表中最新一条数据的id值+1 作为当前新增数据的id
                    if not case_id:
                        case_id = exists_id_latest.id + 1
                        return {"code": 0, "msg": f"case id {case_id} success add."}
                    # 2.1.2) 若case_id不为空，直接落库
                    else:
                        return {"code": 0, "msg": f"case id {case_id} success add."}
                else:
                    return {"code": 40001, "msg": f"case id {case_id} already exists in the table."}

    put_paresr = testcase_ns.parser()
    put_paresr.add_argument("id", type=int, required=True, location="json")
    put_paresr.add_argument("case_title", type=str, required=True, location="json")
    put_paresr.add_argument("remark", type=str, location="json")

    @testcase_ns.expect(put_paresr)
    def put(self):
        case_data = request.json
        logger.info(f"接收到的参数<====== {case_data}")
        # dic = {}
        # dic[request.headers.get('Cookie').split('=')[0]] = request.headers.get('Cookie').split('=')[-1]
        # logger.info(f"接收到的cookie信息是<====== {dic}")
        case_id = case_data.get("id")
        # 查询数据库，查看是否有记录
        exists = testcase_service.get(case_id)
        logger.info(f"查询表结果：{exists}")
        # 如果不存在，则 不执行修改操作 并返回 40002
        # 如果存在，执行修改操作
        if exists:
            case_data1 = {}
            case_data1["case_title"] = case_data.get("case_title")
            case_data1["remark"] = case_data.get("remark")
            testcase_service.update(case_data1)
            return {"code": 0, "msg": f"case id {case_id} success change to {case_data1}"}
        else:
            return {"code": 40002, "msg": "case is not exists"}

    delete_parser = testcase_ns.parser()
    delete_parser.add_argument("id", type=int, location="json", required=True)

    @testcase_ns.expect(delete_parser)
    def delete(self):
        case_data = request.json
        case_id = case_data.get("id")
        logger.info(f"接收到的参数id <====={case_id}")
        exists = testcase_service.get(case_id)
        if exists:
            testcase_service.delete(case_id)

            return {"code": 0, "msg": f"case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"case is not exists"}