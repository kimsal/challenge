from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import School, Student
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from rest_framework.exceptions import APIException
from rest_framework_nested.relations import NestedHyperlinkedRelatedField
class StudentSerializer(NestedHyperlinkedModelSerializer):
    student_identification = serializers.CharField(read_only=True)
    parent_lookup_kwargs = {
        'school': 'school',
    }
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'student_identification', 'school')
    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        """
        if Student.objects.filter(school = validated_data.get('school')).count()>= validated_data.get('school').maximum_students:
            raise APIException("Maximum Students Reached!")
        else:
            instance = Student.objects.create(**validated_data)
            # student_datas = validated_data.pop('students')
            # for student in student_datas:
            #     Student.objects.create(student)
            return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `Student` instance, given the validated data.
        """
        if Student.objects.filter(school = instance.school).count()>= instance.school.maximum_students:
            raise APIException("Maximum Students Reached!")
        else:
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.student_identification = validated_data.get('student_identification', instance.student_identification)
            instance.school = validated_data.get('school', instance.school)
            instance.save()
            return instance

class SchoolSerializer(NestedHyperlinkedModelSerializer):
    # students = serializers.HyperlinkedRelatedField(many=True, view_name='students', queryset=Student.objects.all())
    # , read_only=True, view_name='students'
    students = StudentSerializer(many= True,read_only=True)
    class Meta:
        model = School
        fields = ('name', 'maximum_students', 'students')
    # students = NestedHyperlinkedRelatedField(
    #     many=True,
    #     read_only= True,
    #     view_name='students',
    #     parent_lookup_kwargs={'students': 'students'}
    # )