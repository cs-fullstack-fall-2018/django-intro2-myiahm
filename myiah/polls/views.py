from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request, entry1):
    return HttpResponse(("Hello  ", entry1))


def times2(request, num1):
    return HttpResponse(("The product is ", num1*2))


def sum(request, num1):
    sum1 = 0
    for x in range(0, num1):
        print(x)
        sum1 +=x
    return HttpResponse(("Sum is: ", sum1 ))