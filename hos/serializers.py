from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from hos.models import  Diagnose, Patient

#creating a serializer DiagnoseSerializer:
class DiagnoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnose
        fields = (
            'id',
            'name_of_diagnoses',
        )

#creating a serializer PatientSerializer:
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id', 'date_of_birth',
            'diagnoses','created_at',
           
        )

#creating a serializer TokenSerializer:
class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_doctor'] = user.is_doctor

#returning a token:
        return token