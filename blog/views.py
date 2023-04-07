from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from blog.models import Users
from blog.service.excel import service


def login(request):
    item_list = service()
    # for item in item_list:
    #     user_obj = models.Goods(**item)
    #     user_obj.save()  # 保存数据
    return render(request, 'login.html', locals())

def res(request):
    item_list = service()
    return render(request,'res.html',locals())

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        rname = request.POST.get("rname")
        rpasswd = request.POST.get("rpasswd")

        #注册成功跳转到登录页面，注册加判断已经存在提示改用用户已存在
        users = Users.objects.all()
        for i in users:
            if rname == i.name:
                return  HttpResponse("用户已存在")
        try:
            Users.objects.create(name = rname,password = rpasswd)
        except Exception as e:
            print(e)
            return HttpResponse("注册失败")

        return redirect('/login/')

class LoginView(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        lname = request.POST.get('lname')
        lpasswd = request.POST.get('lpasswd')

        #登录失败时需要提示是用户名不存在还是密码错误
        try:#存放可能出现异常的代码，查询数据多个条件默认是并且的关系
            user = Users.objects.get(name = lname)
            #当输入的用户名在数据库里查询不到，说明try里面的代码存在异常
            #执行万能异常里面的语句
        except Exception as e:
            print(e)
            return HttpResponse("用户名不存在")

        #如果用户名对，就判断密码有没有输入正确
        if lpasswd != user.password:
            return HttpResponse("用户名和密码不匹配")

        return redirect('/res/')


