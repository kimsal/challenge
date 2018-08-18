# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Student, School
from my_app.serializers import SchoolSerializer, StudentSerializer
# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    def get_queryset(self):
        params = self.request.query_params
        # return []
        if self.kwargs:
            datas= Student.objects.filter(school= self.kwargs['schools_pk']).all()
        else:
            datas= Student.objects.all()
        if params.get('first_name') :
            # print 'query first name:'+params.get('first_name')
            datas= datas.filter(last_name = params.get('first_name'))
        if params.get('last_name'):
            # print 'query last name:'+ params.get('last_name')
            datas= datas.filter(last_name = params.get('last_name'))
        if params.get('age'):
            # print 'query age:'+params.get('age')
            datas= datas.filter(age = params.get('age'))
        if params.get('nationality'):
            # print 'query nationality:'+params.get('nationality')
            datas= datas.filter(nationality = params.get('nationality'))
        return datas.order_by('id')
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = School.objects.all().order_by('id')
    serializer_class = SchoolSerializer
    def get_queryset(self):
        params = self.request.query_params
        datas= School.objects.all()
        if params.get('name'):
            datas= datas.filter(name = params.get('name'))
        if params.get('location'):
            datas= datas.filter(location = params.get('location'))
        return datas
        
    
    # def get_serializer_class(self):
    #     # if self.action == 'list' or self.action == 'retrieve':
    #     #     return SchoolSerializer
    #     return SchoolSerializer