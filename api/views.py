from django.shortcuts import render
import requests
import json
from PIL import Image
import numpy as np
from django.http import JsonResponse
# Create your views here.


def test(request):
    msg=request.GET.get('msg','success')
    return JsonResponse({"msg":msg})


def mnist(request):
    result1 = request.GET.getlist('mnist_x[]')
    result2 = request.GET.getlist('mnist_y[]')
    # print(result1)
    # print(result2)
    data = np.matrix([[0] * 28 for i in range(28)])
    n = len(result1)

    for i in range(n):
        x = int((int(result1[i])-1) / 350 * 28)
        y = int((int(result2[i])-1) / 350 * 28)
        # print(x, " ", y)
        data[x, y] = 1
    ans = 5
    return JsonResponse({"res": ans})


def cast(url):
    im = Image.open(url)

    print(im.size)
    im = im.resize((28, 28)).convert("LA")
    matrix = np.asarray(im)
    list = []
    for i in range(0, 28):
        temp = []
        for j in range(0, 28):
            temp.append(matrix[i][j][0] / matrix[i][j][1])
        list.append(temp)
    data = np.matrix(list)
    print(data.shape)
    return data
# print(matrix[][][1])