# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 20:03
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : __init__.py.py

# 1：完成注册手机号码的初始化操作：修改Excel
# 第一种操作：利用Excel设置初始化手机号码，每次进行+1操作，以及变量替换。记得做数据演示。
# 第二种操作：每次从数据库里面查询最大的手机号码，在这个基础上加1（后期自己操作）
# 第三种操作：每次清除完这个手机号码相关的数据，进行垃圾数据重置操作。---数据库
# 当前时间戳生成手机号码 参数替换完成 ${变量名}


#所有用过的手机号码 都放到Excel里面  138、135、134+8位随机生成
#利用一个函数 随机生成一个手机号码  去检测是否在excel中出现过
#如果出现过就不用  没有出现过 就用
#你要从excel中读取所有的数据  然后再去进行分析  可能会有点麻烦

#正则去进行匹配：设定一个初始值

#13800000000
#13900000000
#18800000000
#千万次