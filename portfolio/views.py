from django.shortcuts import render
from draft.models import Draft , DraftActivity , DraftPortfolio , DraftResume

def portfolio_list(req):
    drafts_count = Draft.objects().filter()
    
    return render(req , './portfolio/list.html')	

def portfolio_detail(req):
    return render(req , './portfolio/detail.html')

def portfolio_preview(req):
    return render(req , './portfolio/preview.html')