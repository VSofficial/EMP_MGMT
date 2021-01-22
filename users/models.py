from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
  
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  username = models.CharField(max_length=10, unique=True)
  email = models.EmailField(max_length=100)
  datetime = models.DateTimeField(auto_now=True)

  #Seperation Line
  #empid = models.CharField(max_length=10)
  phone = models.CharField(max_length=10)
  joindate = models.DateField()
  role = models.CharField(max_length=40)
  #first_name = models.CharField(max_length=50)
  #last_name = models.CharField(max_length=50)
  gender = models.CharField(max_length=10)
  dob = models.DateField()
  salary = models.CharField(max_length=10)
  team = models.CharField(max_length=100)

  


  def __str__(self):
    return self.username

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=200,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('password',)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
