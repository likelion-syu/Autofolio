from django.shortcuts import render

# new
def draft_new(request):
    return render(request,'draft/new.html')

# list
def draft_list(request):
    return render(request , './draft/list.html')

# detail
def draft_detail(request):
    return render(request , './draft/detail.html')
