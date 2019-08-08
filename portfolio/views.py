from django.core import serializers
from django.shortcuts import render ,get_object_or_404, redirect
from draft.models import Draft , DraftActivity , DraftPortfolio , DraftResume
from theme.models import Theme
from .models import Portfolio , Subdomain
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

def portfolio_list(req):
    # 현재 생성된 draft의 수를 확인
    drafts_count = Draft.objects.filter(author=req.user).count()
    portfolios = Portfolio.objects.filter(author=req.user).all()
    portfolios_count = portfolios.count()
    
    return render(req , './portfolio/list.html' , {
        'drafts_count' : drafts_count,
        'portfolios' : portfolios,
        'portfolios_serialized' : serializers.serialize('json' , portfolios),
        'portfolios_count' : portfolios_count
    })

def portfolio_preview(req):
    return render(req , './portfolio/preview.html')


def portfolio_create(req):
    drafts = Draft.objects.filter(author=req.user).all()
    themes = Theme.objects.all()

    return render(req , './portfolio/detail.html' , {
        'type' : 'Create',
        'drafts' : drafts,
        'themes' : themes,
        'drafts_serialized' : serializers.serialize('json' , drafts),
        'themes_serialized' : serializers.serialize('json' , themes)
    })

def portfolio_update(req , portfolio_id):
    return render(req , './portfolio/detail.html' , {
        'type' : 'Update',
        'drafts' : drafts,
        'themes' : themes,
        'drafts_serialized' : serializers.serialize('json' , drafts),
        'themes_serialized' : serializers.serialize('json' , themes),
    })

# API
@csrf_exempt
def api_create(req):
    data = json.loads(req.body)
    
    try:
        draft_chaining = Draft.objects.get(pk = data['draft']['pk'])
    except Draft.DoesNotExists:
        return JsonResponse({
            'result' : -1,
            'mesg' : '드래프트가 존재하지 않습니다'
        })
    
    try:
        theme_chaining = Theme.objects.get(pk = data['theme']['pk'])
    except Theme.DoesNotExists:
        return JsonResponse({
            'result' : -2,
            'mesg' : '테마가 존재하지 않습니다' 
        })

    newPortfolio = Portfolio()
    newPortfolio.title = data['title']
    newPortfolio.created_dt = timezone.datetime.now()
    newPortfolio.draft = draft_chaining
    newPortfolio.theme = theme_chaining
    newPortfolio.tags = data['tags']
    newPortfolio.author = req.user
    newPortfolio.use_yn = 1
    newPortfolio.last_modified_user = req.user

    newPortfolio.save()

    return JsonResponse({
        'result' : 1
    } , json_dumps_params={'ensure_ascii' : True})

@csrf_exempt
def api_delete(req):
    data = json.loads(req.body)

    try:
        portfolio = Portfolio.objects.get(pk = data['pk'])
    except Portfolio.DoesNotExists:
        return JsonResponse({
            'result' : -1,
            'mesg' : '포트폴리오가 존재하지 않습니다'
        })

    portfolio.delete()
    
    return JsonResponse({
        'result' : 1
    } , json_dumps_params={'ensure_ascii' : True})

def get_drafts(req):    
    drafts = Draft.objects.filter(author = req.user).all()
    
    # return JsonResponse({
    #     'message' : '안녕 파이썬 장고',
    #     'items' : ['파이썬', '장고', 'AWS', 'Azure'],
    # }, json_dumps_params = {'ensure_ascii': True})

    return JsonResponse(drafts , json_dumps_params={'ensure_ascii' : True})

    