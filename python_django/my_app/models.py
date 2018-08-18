from django.contrib import admin
from django.db import models
from .models import *
import uuid
# from super_inlines.admin import SuperInlineModelAdmin,SuperModelAdmin
def getUniqueString():
  return str(uuid.uuid4())[:20]
class School(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=20)
  location=models.CharField(max_length=100, blank=True, null=True)
  maximum_students = models.PositiveIntegerField(default=0)
  # students = PrimaryKeyRelatedField(queryset=Student.objects.all())
  # def get_absolute_url(self):
  #     return ('School', (), {'name': self.name,'maximum_students': self.maximum_students})
  # def save(self):
  #     super(School, self).save()
  # def students(self):
  #   return self.student_set.all()
  def __str__(self):
      return self.name

class Student(models.Model):
  id=models.AutoField(primary_key=True)
  first_name= models.CharField(max_length=20)
  last_name= models.CharField(max_length=20)
  student_identification= models.CharField(max_length=20, unique=True, default= getUniqueString)
  school= models.ForeignKey(School,  related_name='students', editable=True ,on_delete=models.CASCADE)
  nationality=models.CharField(max_length=20, blank=True, null=True)
  age=models.PositiveIntegerField(default=0)
  # def get_absolute_url(self):
  #     return ('Student', (), {'first_name': self.first_name,'last_name': self.last_name,'student_identification': self.student_identification,'school': self.school})
  # def save(self):
  #     super(School, self).save()

  def __str__(self):
      return self.first_name
 

