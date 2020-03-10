import requests
from app import Mp_Base_url, Mp_Handers, Mis_Base_url, Mis_Handers, App_Base_url, App_Handers

"""自媒体"""


class MpLogin:
    def __init__(self):
        # 自媒体登陆请求url
        self.mp_login_url = Mp_Base_url + "/mp/v1_0/authorizations"
        # 登陆测试方法

    def test_mp_url_login(self, mobile, code):
        # 定义数据
        data_pm = {"mobile": mobile, "code": code}
        # 执行请求
        return requests.post(url=self.mp_login_url,
                             json=data_pm,
                             headers=Mp_Handers)


"""后台管理系统"""


class MisLogin:
    # 1.定义接口路劲
    def __init__(self):
        # 后台管理系统的请求url地址
        self.mis_login_url = Mis_Base_url + "/mis/v1_0/authorizations"

        # 2.定义测试方法

    def test_mis_login_url(self, username, password):
        # 3.定义接口数据
        data_mis = {"account": username, "password": password}
        # 4.执行接口请求
        return requests.post(url=self.mis_login_url, json=data_mis, headers=Mis_Handers)


# app
# 1.定义接口测试类
class AppLoging:
    # 2.定义接口路径
    def __init__(self):
        self.applogin_url = App_Base_url + "/app/v1_0/authorizations"
        # 3.定义测试方法

    def test_app_url(self, mobile, code):
        # 4.定义测试数据
        data_app = {"mobile": mobile, "code": code}
        # 5.执行接口请求
        return requests.post(url=self.applogin_url, json=data_app, headers=App_Handers)
