from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
def draft(request):
    return render(request,'draft/create.html')
=======
def draft_list(req):
    return render(req , './draft/list.html')

def draft_detail(req):
    return render(req , './draft/detail.html')

>>>>>>> d360ac2e76473f663c2c05c35b60b8a78cd14e17
