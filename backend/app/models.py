from django.db import models

# Create your models here.

import uuid

from django.db import models
from django.core.mail import send_mail

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.contrib.auth.base_user import AbstractBaseUser

from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

# classe de modification de gestion des utilisateur par defaut de django
class UserManager(BaseUserManager):

    def create_user(self,email,username,first_name=None,adress=None,phone_number=None,password=None):
        if email is None:
            raise TypeError('Mail est obligatoire')
        if username is None:
            raise TypeError('Nom est bligatoire')

        user=self.model(username=username,email=self.normalize_email(email), first_name=first_name,adress=adress,phone_number=phone_number)
        user.user_type= 'is_client'
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,first_name,adress,phone_number,password=None):
        user = self.create_admin(
            
            email,
            username,
            first_name,
            adress,
            phone_number,
            password=password,

        )
        user.is_staff = True
        user.is_superuser= True
        user.is_autorise  = True
        user.save(using=self._db)
        return user
    def email_user(self, *args, **kwargs):
        send_mail(
        '{}'.format(args[0]),
        '{}'.format(args[1]),
        '{}'.format(args[2]),
        [self.email],
        fail_silently=False,
    )

 
    


    
    # organisme_sous = models.ForeignKey(OrganismeFormation,on_delete=models.CASCADE)
class User(AbstractBaseUser, PermissionsMixin):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True,null=True)
    username = models.CharField(_('username '), max_length=50,null=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True,null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True) 
    avatar = models.FileField(upload_to='avatars/', null=True, blank=True)
    signature_former = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20,null=True,unique=True)
    adress = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','adress','phone_number']

    session_token = models.CharField(max_length=10, default=0)

    active = models.BooleanField(default=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
  
    # fontction personalisé pour envoie des messages à l'utilisateur
    def email_user(self, *args, **kwargs):
        send_mail(
        '{}'.format(args[0]),
        '{}'.format(args[1]),
        '{}'.format(args[2]),
        [self.email],
        fail_silently=False,
    )

    objects = UserManager()

    def __str__(self):
        return self.username or ''
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        # return refresh.access_token
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }