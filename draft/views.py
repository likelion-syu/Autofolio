from django.shortcuts import render

def draft_new(request):
    return render(request,'draft/new.html')

def draft_list(req):
    return render(req , './draft/list.html')

def draft_detail(req):
    return render(req , './draft/detail.html')
