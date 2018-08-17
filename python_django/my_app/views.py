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
class SchoolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = School.objects.all().order_by('id')
    serializer_class = SchoolSerializer
    # def get_queryset(self):
    #     return Student.objects.all().order_by('id')
        # filter(school=self.kwargs['school'])

    # def get_serializer_class(self):
    #     # if self.action == 'list' or self.action == 'retrieve':
    #     #     return SchoolSerializer
    #     return SchoolSerializer