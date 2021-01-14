from django.shortcuts import render, HttpResponse

# Create your views here.


def post_list(request):
    return HttpResponse('글 리스트')
