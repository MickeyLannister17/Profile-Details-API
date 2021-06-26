from django.db import models


# Create your models here.

class Verification_method(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Verification"

    def __str__(self):
        return self.title


class Account_type(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Account_type"

    def __str__(self):
        return self.title


class Gender(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Gender"

    def __str__(self):
        return self.title


class Profile(models.Model):
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    phone_number = models.IntegerField(null=True)
    account_type = models.ForeignKey(Account_type, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    business_name = models.CharField(max_length=150)
    business_address = models.CharField(max_length=150)
    verification_method = models.ForeignKey(Verification_method, on_delete=models.CASCADE)

    # verification_type = models.CharField(max_length=150) This brings about an error i'm yet to understand nor rectify
    # cac_no = models.CharField(max_length=250) same terror in this field

    def __str__(self):
        return self.first_name
