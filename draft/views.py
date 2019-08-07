from django.shortcuts import render

# Create your views here.
def draft(request):
    return render(request,'draft/create.html')
