from django.conf import settings
from django.utils import timezone

from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from django.contrib.auth.models import User
from user.models import Profile


try:
    from django.utils.translation import gettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


def validate_phone_sign_in(self, phone, password):

    user = None

    if phone and password:
        try:
            user = Profile.objects.filter(phone=phone).first().user
        except:
            user = None

        if user != None and user.check_password(password):
            user = user
        else:
            msg = _('Неправильный номер или пароль')
            raise exceptions.AuthenticationFailed(msg)

    return user


def get_auth_user_using_allauth_sign_in(self, username, email, password, phone):
    from allauth.account import app_settings

    # Authentication through email
    if email:
        return self._validate_email(email, password)

    # Authentication through username
    # if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
    #     print(222)
    #     return self._validate_username(username, password)

    # Authentication through phone number
    if phone:
        
        return self._validate_phone(phone, password)

    # Authentication through either username or email
    if phone == '' and email == '' or phone == None and email == None \
            or phone == '' and email == None or phone == None and email == '':
        msg = _('Заполните номер или пароль')
        raise exceptions.ValidationError(msg)

    return self._validate_username_email(username, email, password)


def validate_email_sign_in(self, email, password):
    user = None

    if email and password:
        try:
            user = User.objects.get(email=email)
        except:
            user = None

    else:
        msg = _('Must include "email" and "password".')
        raise exceptions.ValidationError(msg)

    if user is not None and user.check_password(password):
        return user
    else:
        msg = _('Неправильный логин или пароль')
        raise exceptions.AuthenticationFailed(msg)



def validate_sign_in(self, attrs):

    username = attrs.get('username')
    email = attrs.get('email')
    password = attrs.get('password')
    phone = attrs.get('phone')
    user = self.get_auth_user(username, email, password, phone)

    if not user:
        msg = _('Unable to log in with provided credentials.')
        raise exceptions.ValidationError(msg)

    # Did we get back an active user?
    self.validate_auth_user_status(user)

    # If required, is the email verified?
    if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
        self.validate_email_verification_status(user)

    attrs['user'] = user
    return attrs


def get_response_sign_in_view(self):
    serializer_class = self.get_response_serializer()
    access_token_expiration = None
    refresh_token_expiration = None
    if getattr(settings, 'REST_USE_JWT', False):
        from rest_framework_simplejwt.settings import api_settings as jwt_settings
        access_token_expiration = (timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
        refresh_token_expiration = (timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
        return_expiration_times = getattr(settings, 'JWT_AUTH_RETURN_EXPIRATION', False)

        data = {
            'user': self.user,
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }

        if return_expiration_times:
            data['access_token_expiration'] = access_token_expiration
            data['refresh_token_expiration'] = refresh_token_expiration

        serializer = serializer_class(instance=data,
                                      context=self.get_serializer_context())
    else:
        serializer = serializer_class(instance=self.token,
                                      context=self.get_serializer_context())
    response = Response(serializer.data, status=status.HTTP_200_OK)
    # if getattr(settings, 'REST_USE_JWT', False):
    #     from dj_rest_auth.jwt_auth import set_jwt_cookies
    #     set_jwt_cookies(response, self.access_token, self.refresh_token)
    response.data['user']['status'] = self.user.profile.status
    response.data['user']['accepted'] = self.user.profile.is_accept
    return response