from django.urls import path

from rest_framework_simplejwt.views import(TokenObtainPairView,)
from rest_framework.routers import DefaultRouter 

from hos.views import PatientView, TokenView


router = DefaultRouter()

router.register('api',PatientView )

urlpatterns = [
   path('token',  TokenView.as_view(),  name='token_obtain_pair'),
]

urlpatterns += router.urls