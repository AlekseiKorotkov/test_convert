from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from . import convert_arabic_and_roman
import re
# Create your views here.
def show(request):
    return render(request,'index.html',None)
@csrf_exempt
def convert_numbers(request):
    number = str(request.POST['number'])
    print(number)

    if re.match(r'^\d+$', number):
        rez =convert_arabic_and_roman.arabic_to_roman(int(number))
    elif re.match(r'^[MDCLXVI]+$', number):
        rez = convert_arabic_and_roman.roman_to_arabic(number)
    else:
        rez = 'Please set correct number'

    data = {
        'value': rez
    }

    return JsonResponse(data)