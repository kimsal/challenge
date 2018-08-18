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
        fields = ('id', 'first_name', 'last_name', 'student_identification', 'school', 'nationality', 'age')
    def create(self, validated_data):
        """
        Create and return a new `Student` instance, given the validated data.
        """
        if Student.objects.filter(school = validated_data.get('school')).count()>= validated_data.get('school').maximum_students:
            raise APIException("Maximum Students Reached!")
        else:
            instance = Student.objects.create(**validated_data)
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
    # students = serializers.HyperlinkedRelatedField(many=True, view_name='students', queryset=[])
    # , read_only=True, view_name='students'
    students = StudentSerializer(many= True,read_only=True)
    
    class Meta:
        model = School
        fields = ('id', 'name', 'maximum_students', 'students', 'location')
    def create(self, validated_data):
        """
        Create and return a new `School` instance, given the validated data.
        """
        instance = School.objects.create(**validated_data)
        students = self.data.get('students')    
        # print str(validated_data)
        if(students):
            for student in students:
                Student.objects.create(school=instance, **student)
        return instance

    def update(self, instance, validated_data):
        """
        Update and return an existing `School` instance, given the validated data.
        """
        # print str(self.data.get('students'))
        instance.name = validated_data.get('name', instance.name)
        instance.maximum_students = validated_data.get('maximum_students', instance.maximum_students)
        instance.save()
        students = self.data.get('students')
        if(students):
            for student in students:
                students_id = student.get('id', None)
                print str(students)
                if students_id:                   
                    inv_students = Student.objects.filter(id=students_id).last()
                    inv_students.first_name = student.get('first_name', inv_students.first_name)
                    inv_students.last_name = student.get('last_name', inv_students.last_name)
                    inv_students.student_identification = student.get('student_identification', inv_students.student_identification)
                    inv_students.school = instance
                    print str(student.get('last_name'))
                    inv_students.save()
                else:
                    print 'add new'
                    Student.objects.create(school=instance, **student)
        return instance