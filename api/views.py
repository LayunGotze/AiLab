from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
# Create your views here.
def test(request):
    msg=request.GET.get('msg','success')
    return JsonResponse({"msg":msg})