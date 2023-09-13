from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from association.models import Court

class UserManager(BaseUserManager):
    use_in_migration = True
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        return self.create_user(email, password, **extra_fields)

class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        return self.name

USER_CHOICES = (
    ('normal_advocate', 'Normal Advocate'),
    ('normal_admin', 'Normal Admin'),
    ('super_admin', 'Super Admin'),
)    

class Advocate(models.Model):
    user = models.ForeignKey(UserData,on_delete=models.CASCADE)
    age=models.IntegerField()
    phone=models.CharField(max_length=200)
    enrollment_id=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200)
    address=models.CharField(max_length=200,default='not given')
    profile_image=models.ImageField(upload_to='media/', null=True, blank=True)
    document_image=models.ImageField(upload_to='media/', null=True, blank=True)
    is_suspend=models.BooleanField(default=False)
    type_of_user = models.CharField(max_length=255,choices=USER_CHOICES,default='normal_advocate')
    def __str__(self):
        return self.user.email+" , "+self.type_of_user
    
class Registrar(models.Model):
    user = models.ForeignKey(UserData,on_delete=models.CASCADE)
    court=models.ForeignKey(Court,on_delete=models.CASCADE)
    date_of_birth = models.DateField(default='2000-01-01')
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200,default='not given')
    profile_image=models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self): 
        return self.user.email