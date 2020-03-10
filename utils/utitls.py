# 封装获取测试结果并返回断言结果的方法
import json


def assert_fa(repone, code, message):
    # 3.获取测试结果
    status_code = repone.status_code
    msg = repone.json().get("message")
    # 4.断言
    if status_code == code and msg == message:
        return True
    else:
        return False


"""读取数据的公用方法"""


def build_data(data_file):
    # 打开测试数据文件
    list_data = []
    with open(file=data_file, encoding="utf-8")as f:
        # 读取完整数据
        r_data = json.load(f)
        # 遍历所有键值
        for cose_data in r_data.values():
            # 在此遍历所有键值,字典对象的键值列表
            list_data.append(list(cose_data.values()))
            print(list_data)
        # 返回读取数据
    return list_data
