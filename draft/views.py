from django.shortcuts import render

def draft_list(req):
    return render(req , './draft/list.html')

def draft_detail(req):
    return render(req , './draft/detail.html')

