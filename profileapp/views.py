from django.shortcuts import render
from django.shortcuts import render

from rest_framework import generics
from .models import Verification_method, Gender, Account_type, Profile
from .serializers import Verification_methodSerializer, GenderSerializer, Account_typeSerializer, ProfileSerializer


# Create your views here.

class ListVerification_method(generics.ListCreateAPIView):
    queryset = Verification_method.objects.all()
    serializer_class = Verification_methodSerializer


class DetailVerification_method(generics.RetrieveUpdateDestroyAPIView):
    queryset = Verification_method.objects.all()
    serializer_class = Verification_methodSerializer


class ListAccount_type(generics.ListCreateAPIView):
    queryset = Account_type.objects.all()
    serializer_class = Account_typeSerializer


class DetailAccount_type(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account_type.objects.all()
    serializer_class = Account_typeSerializer


class ListGender(generics.ListCreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class DetailGender(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class ListProfile(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DetailProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
