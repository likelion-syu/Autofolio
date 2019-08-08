from django.shortcuts import render

<<<<<<< HEAD
<<<<<<< HEAD
# create
=======
>>>>>>> 034ec784de9a49b1aa855f86a85bd322ecfc9674
def draft_new(request):
    return render(request,'draft/new.html')

# list
def draft_list(request):
    return render(request , './draft/list.html')

# detail
def draft_detail(request):
    return render(request , './draft/detail.html')
