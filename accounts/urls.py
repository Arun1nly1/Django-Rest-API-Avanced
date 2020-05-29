from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token 
#Put it in account app if there is account app
from rest_framework_jwt.views import refresh_jwt_token
from .views import AuthAPIView, RegisterAPIView


urlpatterns = [
    path('', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
]