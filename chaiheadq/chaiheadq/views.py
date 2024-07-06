from django.shortcuts import render


def Web_Home(request):
    return render(request,'Home.html')