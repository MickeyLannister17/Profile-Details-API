from rest_framework import serializers
from .models import Verification_method, Account_type, Gender, Profile


class Verification_methodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification_method
        fields = "__all__"

    def create(self, validated_data):
        return Verification_method.objects.create(**validated_data)


class Account_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_type
        fields = "__all__"

    def create(self, validated_data):
        return Account_type.objects.create(**validated_data)


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"

    def create(self, validated_data):
        return Gender.objects.create(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
