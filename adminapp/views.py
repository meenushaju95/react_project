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
    serializer = loginserializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user:
            user_type = user.user_type
            if user_type == '1':
                role = 'admin'
            elif user_type == '2':
                role = 'user'
            elif user_type == '3':
                role = 'moderator'
            else:
                role = 'unknown'
            return JsonResponse({"status": "success", "role": role})
        else:
            return JsonResponse({"status": "failure", "error": "Invalid username or password"}, status=400)
    else:
        return JsonResponse({'error': 'Invalid data'}, status=400)