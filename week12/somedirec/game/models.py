from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string



# class GamerManeger(BaseUserManager):
#     def _create(self,nickname,password,**extra_fields):
#         if not nickname:
#             raise ValueError('поле nickname не может быть пустым')
#         user = self.model(email=nickname,**extra_fields)
#         user.set_password(password)
#         user.save()
#         return user


#     def create_gamer(self,nickname,password,**extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_active',True)
#         return self._create(nickname,password,**extra_fields)
    

# class Gamer(AbstractBaseUser):
#     nickname = models.CharField(primary_key=True)
#     name = models.CharField(max_length=15)
#     is_active = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=20, blank=True)


#     objects = GamerManeger()

#     USERNAME_FIELD = 'nickname'
#     REQUIRED_FIELDS = ['name']


#     def __str__(self):
#         return self.nickname
    

#     def has_module_perms(self, app_lable):
#         return self.is_staff
    
#     def has_perm(self, perm, obj=None):
#         return self.is_staff
    
#     def create_activation_code(self):
#         code = get_random_string(15)
#         self.activation_code = code 
#         self.save()