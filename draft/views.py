from django.shortcuts import render

# create
def draft(request):
    return render(request,'./draft/create.html')

# list
def draft_list(request):
    return render(request , './draft/list.html')

# detail
def draft_detail(request):
    return render(request , './draft/detail.html')
