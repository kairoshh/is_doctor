from rest_framework import permissions
from django.conf import settings
import jwt

#creating a model IsDoctor:
class IsDoctor(permissions.BasePermission):

#give permission:
    def has_permission(self, request, view):
        token = request.headers.get('Authorization').split(' ')[1]
        decode_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256']).get('is_doctor')
        return decode_token
    