from django.shortcuts import render

def portfolio_list(req):
    return render(req , './portfolio/list.html')	

def portfolio_detail(req):
    return render(req , './portfolio/detail.html')

def portfolio_preview(req):
    return render(req , './portfolio/preview.html')