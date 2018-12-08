from django.shortcuts import render

# Create your views here.
def test(request):
    #测试页
    return render(request,'index.html')

def login(request):
    #登录页
    return render(request,'login.html')

def question(request):
    #选题页
    return render(request,'question.html')

def rank(request):
    #排名结果页
    return render(request,'rank.html')

def mnist(request):
    #手写识别页
    return render(request,'mnist.html')

def model(request):
    #模型修改页
    return render(request,'model.html')