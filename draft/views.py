from django.shortcuts import render

<<<<<<< HEAD
# create
def draft(request):
    return render(request,'./draft/create.html')
=======
def draft_new(request):
    return render(request,'draft/new.html')
>>>>>>> dfe8bfd96574af1db2129066294a08594a205210

# list
def draft_list(request):
    return render(request , './draft/list.html')

# detail
def draft_detail(request):
    return render(request , './draft/detail.html')
