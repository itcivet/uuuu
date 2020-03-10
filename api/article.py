"""文章api"""
import requests

from app import Mp_Base_url, Mp_Handers, Mis_Base_url, Mis_Handers, Sh_Mis_Base_url, Sh_Mis_Handers, App_Base_url, \
    App_Handers


# 自媒体
class WenArticle:
    def __init__(self):
        # 发布文章的请求地址
        self.fb_article_url = Mp_Base_url + "/mp/v1_0/articles"
        # 发布文章接口方

    def test_fb_ariticle(self, title, content, channel_id):
        # 定义测试数据
        data_pms = {"title": title, "content": content,
                    "channel_id": channel_id,
                    "cover": {"type": 0, "images": []}}
        # 调用post接口 后返回对应结果
        return requests.post(url=self.fb_article_url,
                             json=data_pms, headers=Mp_Handers)


# 后台管理系统
class MisArticle:
    # 定义接口路径
    def __init__(self):
        # 查询文章的请求url地址
        self.wz_article_url = Mis_Base_url + "/mis/v1_0/articles"

        # 审核文章的请求url地址
        self.sh_article_url = Sh_Mis_Base_url + "/mis/v1_0/articles"

    # 封装接口方法
    def test_wz_aritcle(self, title, channel):
        # 定义测试数据
        wz_string = {"title": title, "channel": channel}
        # 调用接口请求
        return requests.get(url=self.wz_article_url,
                            params=wz_string,
                            headers=Mis_Handers)
        # 封装后台文章审核

    # 封装接口方法
    def test_sh_article(self, ar_id, status):
        # 定义测试数据
        data_sh = {"article_ids": [ar_id], "status": status}
        # 调用接口请求
        return requests.put(url=self.sh_article_url,
                            json=data_sh,
                            headers=Sh_Mis_Handers)


# app 获取频道下的新闻
class AppArticle:
    # 定义接口路径url
    def __init__(self):
        self.app_pd_url = App_Base_url + "/app/v1_1/articles"

    # 定义测试方法
    def test_pd_aryicle(self, cl_id, timestamp, with_top):
        # 定义测试数据
        data_pd = {"channel_id": cl_id, "timestamp": timestamp, "with_top": with_top}
        # 执行接口请求
        return requests.get(url=self.app_pd_url, params=data_pd, headers=App_Handers)
