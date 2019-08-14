# -*- coding: utf-8 -*-
# @Time    : 2019/7/9/16:55
# @Author  : XY
# @File    : get_data.py


from common import project_path
from common import read_config
import re

config = read_config.ReadConfig(project_path.conf_path)


class GetData:
    '''可以用来动态的更改 删除 获取数据'''
    COOKIE = None
    token = None
    # LOAN_ID = None  # 新添加的标id初始值
    # normal_user = config.get_str('data', 'normal_user')
    # normal_pwd = config.get_str('data', 'normal_pwd')
    # normal_member_id = config.get_str('data', 'normal_member_id')


def replace(target):
    p2 = '#(.*?)#'
    while re.search(p2, target):  # 查找参数的字符就matach object , True
        m = re.search(p2, target)  # 在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
        key = m.group(1)  # 传参就是只返回匹配的字符串，也就是当前组的匹配字符
        print(key)
        value = getattr(GetData, key)  # 拿到我们需要去替换的值
        target = re.sub(p2, value, target, count=1)

    return target