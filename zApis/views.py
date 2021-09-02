from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from .models import Register
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt
def RegisterApi(request,id=0):
    if request.method=='GET':
        registers=Register.objects.all()
        register_serializer=RegisterSerializer(registers,many=True)
        return JsonResponse(register_serializer.data,safe=False)
    elif request.method=='POST':
        register_data=JSONParser().parse(request)
        register_serializer=RegisterSerializer(data=register_data)
        if register_serializer.is_valid():
            register_serializer.save()
            return JsonResponse("Added data successfuly",safe=False)

        return JsonResponse("Failed to add",safe=False)