"""文章发布审核"""
# 定义测试类
import time
import logging
import pytest

from api import FActoryApi
from app import Mp_Handers, Mis_Handers, App_Handers
from utils.utitls import assert_fa, build_data


class TestWenLogin:
    # 自媒体的发布文章的id类属性
    article_id = None
    # 后台管理系统-文章标题的类属性
    article_title = None

    # 定义测试方法
    def test_login_mp(self):
        # 定义测试数据
        mobile = "13012345678"
        code = "246810"
        # 调用登陆方法
        mp_login_response = FActoryApi.mp_login.test_mp_url_login(mobile, code)
        print("自媒体登陆获取结果返回信息为:", mp_login_response.json())
        # 断言 mp_login_response.status_code 状态码是否相等
        # assert mp_login_response.status_code == 201
        # assert mp_login_response.json().get("message") == "OK"
        assert assert_fa(mp_login_response, 201, "OK")
        # 获取登陆后的token
        mp_token = mp_login_response.json().get("data").get("token")
        print("自媒体登陆后返回的token={}".format(mp_token))
        # 给mp自媒体请求头加入Authorization的登陆后的键值对
        Mp_Handers["Authorization"] = "Bearer " + mp_token
        print("登陆后的基础配置头部信息为=", Mp_Handers)

    """自媒体发布文章测试方法"""

    @pytest.mark.parametrize("ar_title,ar_content,ch_id,status_code,msg",
                             build_data("./data/fabu_wz_article.json"))
    def test_fb_article(self, ar_title, ar_content, ch_id, status_code, msg):
        """
        ar_title=文章标题
        ar_content=文章内容
        ch_id=频道id
        status_code=期望返回状态码
        msg=期望返回msg
        """
        # 1.定义测试数据-每一组代表一种测试情况
        TestWenLogin.article_title = ar_title.format(time.strftime("%Y%m%d%H%M%S"))
        article_content = ar_content.format(time.strftime("%Y%m%d%H%M%S"))
        channel_id = ch_id
        # 2.调用测试方法-执行对应业务请求接口方法
        fb_reponse = FActoryApi.mp_article.test_fb_ariticle(self.article_title,
                                                            article_content,
                                                            channel_id)
        logging.info("发布文章的结果信息为:{}".format(fb_reponse.json()))
        # 3.获取测试结果
        # status_code = fb_reponse.status_code
        # msg = fb_reponse.json().get("message")
        # # 4.断言.
        # assert status_code == 201
        # assert msg == "OK"
        assert assert_fa(fb_reponse, status_code, msg)
        # 5.获取关联数据(*)
        # 如后续的测试方法:对于本次测试执行结果对应的数据没有依赖,则不需要关联数据
        # 如后续测试方法:需要使用到本次测试方法所产生的数据,则需要对应的数据结果进行存储
        # 由于后续测试方法需要使用存储的数据,存储数据的变量需要定义为测试类属性或实例化属性,这样才能获取对应的数据
        # 实例方法中局部变量其他实例方法是不能直接进行访问的
        TestWenLogin.article_id = fb_reponse.json().get("data").get("id")
        logging.info("发布文章的id{}".format(TestWenLogin.article_id))

    """后台管理系统-登录"""

    def test_mis_login(self):
        # 1.定义测试数据
        username = "testid"
        password = "testpwd123"
        # 2.调用测试方法
        mis_respones = FActoryApi.mis_login.test_mis_login_url(username, password)
        print("后台管理系统登录结果:", mis_respones.json())
        # 3.获取测试结果
        # status_code = mis_respones.status_code
        # msg = mis_respones.json().get("message")
        # # 4.断言
        # assert status_code == 201
        # assert msg == "OK"
        assert assert_fa(mis_respones, 201, "OK")
        # 5.获取关联数据 token.  下一个文章需要token
        mis_token = mis_respones.json().get("data").get("token")
        # 重组请求头,在添加一个 Authorization 属性
        Mis_Handers["Authorization"] = "Bearer " + mis_token
        print("登陆后的基础配置头部信息为=", mis_token)

    """后台管理系统-文章查询"""

    def test_wz_article(self):
        # 1.定义测试数据
        article_title = self.article_title
        print("文章的标题:", article_title)
        channl = "html"
        # 2.调用测试方法
        wz_respone = FActoryApi.mis_article.test_wz_aritcle(article_title, channl)
        print("查询文章结果为:", wz_respone.json())
        # 3.获取测试结果
        # status_code = wz_respone.status_code
        # msg = wz_respone.json().get("message")
        # # 4.断言
        # assert status_code == 200
        # assert msg == "OK"
        assert assert_fa(wz_respone, 200, "OK")
        print("文章的id:", TestWenLogin.article_id)
        assert wz_respone.json().get("data").get("articles")[0].get("article_id") == TestWenLogin.article_id
        # 5.获取关联数据

    """后台管理系统-文章审核"""

    def test_sh_article(self):
        # 1.定义测试数据
        ar_id = TestWenLogin.article_id
        ar_status = 2
        # 2.调用测试方法
        sh_respone = FActoryApi.mis_article.test_sh_article(ar_id, ar_status)
        print("发布文章响应体:", sh_respone.json())
        # 3.获取测试结果
        # 4.断言
        # assert assert_fa(sh_respone, 201, "OK")  #where False = assert_fa(<Response [401]>, 201, 'OK')
        # 5.获取关联数据
        """app登陆"""

    def test_app_logints(self):
        # 1.定义测试数据
        mobile = "13012345678"
        code = "246810"
        # 2.调用测试方法
        app_respones = FActoryApi.app_login.test_app_url(mobile, code)
        # 3.获取测试结果
        # 4.断言
        assert assert_fa(app_respones, 201, "OK")
        # 5.获取关联数据
        app_token = app_respones.json().get("data").get("token")
        # 重组请求头,在添加一个 Authorization 属性
        App_Handers["Authorization"] = "Bearer " + app_token
        print("app带token的信息请求头:", App_Handers)

    """获取频道下的新闻"""

    def test_app_article(self):
        # 1.定义测试方法
        # 2.定义测试数据
        cl_id = 1
        time_stamp = int(time.time() * 1000)
        print("当前的时间戳", time_stamp)
        with_top = 1
        # 3.调用接口方法
        fb_response = FActoryApi.app_article.test_pd_aryicle(cl_id, time_stamp, with_top)
        print("根据频道查询文章的结果:", fb_response.json())
        # 4.获取测试结果
        # 5.断言
        assert assert_fa(fb_response, 200, "OK")
        # 6.获取关联数据
