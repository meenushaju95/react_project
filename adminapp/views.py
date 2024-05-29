from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .serializers import loginserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token

@api_view(['GET'])
def home(request):
    #user = restapi.objects.all()
    #serialiser = restserializer(user,many=True)
    
    return HttpResponse('KKKKKKK')
@api_view(['POST'])
def loginview(request):
    serialiser = loginserializer(data=request.data)
    if serialiser.is_valid():
            user = authenticate(username = request.data.get('username'),password = request.data.get('password'))
            #user = CustomUser.objects.create_user(username = request.data.get('username'),password = request.data.get('password'))
            if user:
                 
                #token = Token.objects.get(user=user)
                #print(token)
                return JsonResponse({"Token":"success"})
            else:
                return Response(serialiser.errors)
