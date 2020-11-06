from django.shortcuts import render
from testapp.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from testapp.serializers import StudentSerializer



#-----browserable api for student------------------#

@api_view(['GET','POST'])
def student_detail(request):
    if request.method =="GET":
        data =  Student.objects.all()
        serializer =StudentSerializer(data ,many= True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer =StudentSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps({"msg":"student added succefully"}),content_type="application/json",status=200)
        return Response(serializer.error,statu =status.HTTP_400_BAD_REQUEST)



@api_view(["GET","PUT","DELETE"])
def student_all_detail(request,pk):
    try:
        obj =Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


 #---------browseable ---api for adminregistration -----------
'''
@api_view(['GET','POST'])
def admin_registration(request,self):
    if request.method =="GET":
        data = AdminRegistraion.objects.all()
        serializer = AdminSerializer(data ,many= True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer = AdminSerializer(data =request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"user":LoginSerializer(user,context =self.get_serializer()).data,"token":AuthToken.objects.create(user)[1],"msg":"user register succefully"})
            #return HttpResponse(json.dumps({"msg":"user register succefully"}),content_type="application/json",status=200)
        return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])
def admin_all_detail(request,pk):
    try:
        obj =AdminRegistraion.objects.get(pk=pk)
    except AdminRegistraion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdminSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''


# ----------- registeration --LOGIN  and Logout API----------------------
from django.contrib.auth import login
from rest_framework import permissions ,generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from knox.models import AuthToken
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
         "msg": "You have been succefully registered "
        })


@api_view(["GET","PUT","DELETE"])
def admin_all_detail(request,pk):
    try:
        obj =User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegisterSerializer(obj)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegisterSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return HttpResponse(json.dumps({"msg":"something is wrong"}),content_type="application/json" ,status =200)



    elif request.method == 'DELETE':
        obj.delete()
        return Response({"msg":"You are deleted succefully"}, status=status.HTTP_204_NO_CONTENT,)



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        #return Response(LoginAPI, self,).post(request, format=None)


        return super(LoginAPI, self,).post(request, format=None)
