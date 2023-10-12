from rest_framework.permissions import (IsAuthenticated,)
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from hos.serializers import Patient, PatientSerializer, TokenSerializer
from hos.permission import IsDoctor

#creating a view PatientView:
class PatientView(ModelViewSet):
    queryset = Patient.objects.all()[:3]
    serializer_class = PatientSerializer
    permission_classes = (IsAuthenticated, IsDoctor)

#creating a view TokenView:
class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer


