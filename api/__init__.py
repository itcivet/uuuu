from api.article import WenArticle, MisArticle, AppArticle
from api.login import MpLogin, MisLogin, AppLoging
from app import bsic_logger_cofing

"""工厂"""
#调用日记配置的方法
bsic_logger_cofing()

class FActoryApi:
    # 自媒体登陆类的类属性
    mp_login = MpLogin()
    # 自媒体发布文章的类属性
    mp_article = WenArticle()
    # 后台管理系统登录的类属性
    mis_login = MisLogin()
    # 后台管理系统文章类属性
    mis_article = MisArticle()
    # app登陆类的类属性
    app_login = AppLoging()
    #app文章的类属性
    app_article = AppArticle()
