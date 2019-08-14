# -*- coding: utf-8 -*-
# @Time    : 2019/7/9/16:45
# @Author  : XY
# @File    : do_mysql.py

from pymysql import connect
from common.read_config import ReadConfig
from common import project_path
class DoMysql:
    '''操作数据库的类，专门进行数据的读取'''

    def do_mysql(self,query,flag=1):
        '''
        :query sql查询语句
        :flag 标志 1 获取一条数据 2获取多条数据'''
        db_config=ReadConfig(project_path.conf_path).get_data('mall_mysql','db_config')

        cnn=connect(**db_config)#建立一个链接
        cursor=cnn.cursor()

        cursor.execute(query)

        if flag==1:
            res=cursor.fetchone()#返回的元组
        else:
            res=cursor.fetchall()#返回的是列表嵌套元组

        return res
if __name__ == '__main__':
    query='select * from pp_goods'
    query2='select count(*) from pp_goods'
    res=DoMysql().do_mysql(query,0)
    count=DoMysql().do_mysql(query2)
    print('查询到条数为：{},数据库的查询结果：{}'.format(count,res))