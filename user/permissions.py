from django.http import request
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.profile.status == 'AD':
            return True
        else:
            return False


class IsStudent(BasePermission):

    def has_permission(self, request, view):
        if request.user.profile.status == 'ST':
            return True
        else:
            return False


class IsTeacher(BasePermission):

    def has_permission(self, request, view):

        if request.user.profile.status == 'TC':
            return True
        else:
            return False
