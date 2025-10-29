from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserRegister(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)


    def save(self, *args, **kwargs):
        # Hash the password before saving (only if it’s not already hashed)
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super(UserRegister, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(UserRegister,on_delete=models.CASCADE,related_name='profile')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=15)
    dob = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
