# 自定义中间件
import re

from django.shortcuts import redirect
from django.urls import reverse


class ShopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        print('url:', path)

        # 判断管理台是否登录
        # 定义后台不登录也可以直接访问的url列表
        urllist = ['/myadmin/login', '/myadmin/logout', '/myadmin/dologin', 'myadmin_verify']
        # 判断当前请求url地址是否以/myadmin开头，并且不在urllist中，才做是否登录判断
        if re.match(r'^/myadmin', path) and (path not in urllist):
            # 判断是否登录
            if 'adminuser' not in request.session:
                # 重定向到登录页面
                return redirect(reverse('myadmin_login'))

        response = self.get_response(request)

        return response
