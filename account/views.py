from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(req):
    return render(req, './account/index.html')

def signup(req):
    if req.method == 'POST':
        if req.POST['password'] == req.POST['password_confirm']:
            try:
                user = User.objects.get(emailaddress=req.POST['email'])
                return render(req, './account/index.html', {
                    'error' : '가입된 이메일이 존재합니다.'
                })
            except User.DoesNotExist:    
                user = User.objects.create_user(
                    emailaddress=req.POST['email'],
                    username='user'+user.id,
                    password=req.POST['password']
                )
                auth.login(req, user)
                return redirect('portfolio_list')
        else:
            return render(req, './account/index.html', {
                'error' : '비밀번호가 일치하지 않습니다.'
        })        
    return render(req, './account/index.html')   

def signin(req):
    return True

def account_find(req):
    return render(req, './account/find.html')

def account_detail(req):
    return render(req, './account/detail.html')   

def account_edit(req):
    return render(req, './account/edit.html')   