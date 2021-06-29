from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.conf import settings

from faculty.serializers import FacultySerializer
from .utils.login import (validate_phone_sign_in,
                              validate_email_sign_in,
                              get_auth_user_using_allauth_sign_in,
                              validate_sign_in)

from .utils.registration import (validate_phone_sign_up,
                                     get_cleaned_data_sign_up,
                                     custom_signup_sign_up)


try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


class SignInSerializer(LoginSerializer):

    phone = serializers.CharField(required=False, allow_blank=True)

    def _validate_email(self, email, password):

        return validate_email_sign_in(self, email, password)

    def _validate_phone(self, password, phone):

        return validate_phone_sign_in(self, password, phone)

    def get_auth_user_using_allauth(self, username, email, password, phone):

        return get_auth_user_using_allauth_sign_in(self, username, email, password, phone)

    def get_auth_user(self, username, email, password, phone):

        if 'allauth' in settings.INSTALLED_APPS:
            return self.get_auth_user_using_allauth(username, email, password, phone)
        return self.get_auth_user_using_orm(username, email, password)

    def validate(self, attrs):

        return validate_sign_in(self, attrs)


class SignUpSerializer(RegisterSerializer):

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField(allow_blank=True, allow_null=True)
    status = serializers.CharField()
    phone = serializers.CharField()
    birth_date = serializers.DateField()
    faculty = FacultySerializer()


    def validate_phone(self, phone):

        return validate_phone_sign_up(self, phone)

    def get_cleaned_data(self):

        return get_cleaned_data_sign_up(self)

    def save(self, request):

        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        custom_signup_sign_up(self, user)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        return user

