from django.shortcuts import render
from draft.models import Draft , DraftActivity , DraftPortfolio , DraftResume
from .models import Portfolio , Subdomain

def portfolio_list(req):
    # 현재 생성된 draft의 수를 확인
    # drafts_count = Draft.objects.filter(author=req.user).count()
    portfolios = Portfolio.objects.all().filter(author=req.user)
    
    return render(req , './portfolio/list.html' , {
        'drafts_count' : 0,
    })	

def portfolio_detail(req):
    return render(req , './portfolio/detail.html')

def portfolio_preview(req):
    return render(req , './portfolio/preview.html')