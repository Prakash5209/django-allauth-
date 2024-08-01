from django.shortcuts import render
from django.contrib.auth import get_user_model

user = get_user_model()
def home(request):
    context = {
        'user':request.user
    }
    return render(request,'home.html',context)
