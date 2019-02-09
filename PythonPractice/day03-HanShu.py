# x=1
# def f1():
#     def f2():
#         print(x)
#     return f2
# x=100
# def f3(func):
#     x=2
#     func()
# x=10000
# f3(f1()) # 10000


# def counter():
#     n = 0
#
#     def incr():
#         nonlocal n
#         x = n
#         n += 1
#         return x
#
#     return incr
#
#
# c = counter() # <==> incr
# print(c()) # incr()
# print(c())
# print(c())
# print(c.__closure__[0].cell_contents)  # 查看闭包的元素

"""
# ##################### 装饰器 #####################

login_status = {'user_name':None,'status':False} # 这个要放在全局，不能放在wrapper中（放在wrapper中每次执行都为原始状态）
def auth(func):
    def wrapper(*args, **kwargs):
        if login_status['user_name'] and login_status['status']:
            res = func(*args, **kwargs) # index(*args, **kwargs)
            return res
        else:
            user_name = input("请输入用户名：")
            pwd = input("请输入密码：")
            if user_name == "amy" and pwd == "123":
                login_status['user_name'] = user_name
                login_status['status'] = True
                res = func(*args, **kwargs) # index(*args, **kwargs)
                return res
            else:
                print("用户名或密码错误，请重新登录！")
    return wrapper


@auth  # index = auth(index)
def index(name):
    print("from index, name=%s" %name)

@auth
def home(name):
    print("%s, welcome to homepage!" %name)

index("amy") # wrapper()

home("amy")
"""

# ##################### 有参装饰器 #####################
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print("执行时间为：%s" %(end_time-start_time))
        return func
    return wrapper

login_status = {'user_name':None,'status':False} # 这个要放在全局，不能放在wrapper中（放在wrapper中每次执行都为原始状态）
def auth(driver="file"):
    def auth2(func):
        def wrapper(*args, **kwargs):
            if driver == "file":
                if login_status['user_name'] and login_status['status']:
                    res = func(*args, **kwargs) # index(*args, **kwargs)
                    return res
                else:
                    user_name = input("请输入用户名：")
                    pwd = input("请输入密码：")
                    if user_name == "amy" and pwd == "123":
                        login_status['user_name'] = user_name
                        login_status['status'] = True
                        res = func(*args, **kwargs) # index(*args, **kwargs)
                        return res
                    else:
                        print("用户名或密码错误，请重新登录！")
            elif driver == "mysql":
                print("==============>mysql认证！")
                res = func(*args, **kwargs)  # index(*args, **kwargs)
                return res
            elif driver == "ldap":
                print("==============>ldap认证！")
            else:
                print("==============>未知认证来源！")
        return wrapper
    return auth2

# @auth(driver='file')  # auth2 ===> index = auth2(index) ===> wrapper()
# def index(name):
#     print("from index, name=%s" %name)

# index("amy")

@timer # index = timer(auth2_wrapper) ===> index = timer_wrapper，其中，func 就是 auth2_wrapper
@auth('file') # auther2 ===> index = auth2(index) ===> index = auth2_wrapper
def home(name):
    print("%s, welcome to homepage!" %name)

home("amy")



