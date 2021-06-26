from django.contrib import admin
from .models import Verification_method, Account_type, Gender, Profile

# Register your models here.

admin.site.register(Verification_method)
admin.site.register(Account_type)
admin.site.register(Gender)
admin.site.register(Profile)
