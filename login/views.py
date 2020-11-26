from django.shortcuts import render
import random
from .models import Login
from rest_framework.decorators import api_view
from .serializer import LoginSerializer
from tracking.models import Courier
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from utilities.sms_sender import send_sms


#get phone num and create a token
@api_view(['POST'])
def login_API(request):
    #create a 4digits code
    rand=""
    for i in range(4):
        rand=rand+str(random.randint(0,9))

    #send securty code
    if request.method == 'POST':
        Login_info = LoginSerializer(data=request.data)
        if Login_info.is_valid():
            Login_info.save(token=rand)
            #send code via sms
            send_sms(phone=str(request.data['phone']),text=str(rand))
            return Response(Login_info.data, status=status.HTTP_201_CREATED)
        return Response(Login_info.errors, status=status.HTTP_400_BAD_REQUEST)


#get phone num and token then login the user
@api_view(['POST'])
def login_confirm(request):

    Login_user = LoginSerializer(data=request.data)
    if Login_user.is_valid():
        if request.method == 'POST':
            p=request.data['phone']
            t=request.data['token']
            if not len(Login.objects.filter(phone=p,token=t)) == 0 :
                user=Courier.objects.get(phone=p).user
                #login user
                if user !=None:
                    login(request,user)
                    return Response(Login_user.data, status=status.HTTP_201_CREATED)
    return Response(Login_user.errors, status=status.HTTP_400_BAD_REQUEST)
