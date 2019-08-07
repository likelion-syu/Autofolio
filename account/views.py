from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(req):
    return render(req, './account/index.html')

def signup(req):
    if req.method == 'POST':
        if req.POST['password'] == req.POST['password_confirm']:
            try:
                user = User.objects.get(username=req.POST['username'])
                return render(req, './account/index.html', {
                    'id_error' : '가입된 이메일이 존재합니다.'
                })
            except User.DoesNotExist:    
                user = User.objects.create_user(
                    username=req.POST['username'],
                    password=req.POST['password']
                )
                auth.login(req, user)
                return redirect('portfolio_list')
        else:
            return render(req, './account/index.html', {
                'pwd_error' : '비밀번호가 일치하지 않습니다.'
            })        
    return render(req, './account/index.html')   

def signin(req):
    # return True
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(req, username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('portfolio_list')
        else:
            return render(req, './account/index.html', {
                'login_error' : '아이디 또는 패스워드가 알맞지 않습니다.'            
            })
    else:
        return render(request, './account/index.html')


def account_find(req):
    return render(req, './account/find.html')

def account_detail(req):
    return render(req, './account/detail.html')   

def account_edit(req):
    return render(req, './account/edit.html')   