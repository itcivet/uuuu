"""自媒体url"""
import logging.handlers
import time

Mp_Base_url = "http://ttapi.research.itcast.cn"
"""自媒体请求头"""
Mp_Handers = {"Content-Type": "application/json"}
"""后台管理系统url"""
Mis_Base_url = "http://ttapi.research.itcast.cn"
"""后台管理系统请求头"""
Mis_Handers = {"Content-Type": "application/json"}
"""审核文章的url"""
Sh_Mis_Base_url = "http://ttapi.research.itcast.cn"
"""审核文章请求头"""
Sh_Mis_Handers = {"Content-Type": "application/json"}
"""app登陆url"""
App_Base_url = "http://ttapi.research.itcast.cn"
"""app请求头"""
App_Handers = {"Content-Type": "application/json"}

"""日记配置"""


def bsic_logger_cofing():
    # 1.创建日记器
    logerr = logging.getLogger()
    # 2.设置日记级别
    logerr.setLevel(level=logging.INFO)
    # 3.创建处理器
    cl = logging.StreamHandler()
    log_file = "./log/apiAtu_log_{}".format(time.strftime("%Y%m%d%H%M%S"))
    lh = logging.handlers.TimedRotatingFileHandler(filename=log_file, when='midnight', interval=1, backupCount=2)
    # 4.创建格式化器
    famatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 5.给处理器添加格式化器
    cl.setFormatter(famatter)
    lh.setFormatter(famatter)
    # 6.给日记器添加处理器
    logerr.addHandler(cl)
    logerr.addHandler(lh)
