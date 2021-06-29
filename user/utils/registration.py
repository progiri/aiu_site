from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import Group
from rest_framework import serializers
from user.models import Profile


try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


def validate_phone_sign_up(self, phone):

    phone_check = Profile.objects.filter(phone=phone).first()

    if phone_check is None:
        return phone
    else:
        raise serializers.ValidationError(
            _("Пользователь с таким номером телефона уже существует"))


def get_cleaned_data_sign_up(self):

    return {
        'username': self.validated_data.get('email', ''),
        'first_name': self.validated_data.get('first_name', ''),
        'last_name': self.validated_data.get('last_name', ''),
        'password1': self.validated_data.get('password1', ''),
        'email': self.validated_data.get('email', ''),
    }


def custom_signup_sign_up(self, user):

    status = self.validated_data.get('status', '')
    middle_name = self.validated_data.get('middle_name', '')
    phone = self.validated_data.get('phone', '')
    birth_date = self.validated_data.get('birth_date', '')
    

    phone = validate_phone_sign_up(self, phone)

    profile = Profile.objects.create(user=user) # Получение профиля пользователя
    profile.middle_name = middle_name # Изменение отчества пользователя
    profile.phone = phone # Изменение номера телефона
    profile.status = status # Сохранение статуса
    profile.birth_date = birth_date
    profile.save()
    return profile


