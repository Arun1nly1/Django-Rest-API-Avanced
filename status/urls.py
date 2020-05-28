from django.urls import path
from .views import StatusAPIView, StatusDetailAPIView


urlpatterns = [
    path('',StatusAPIView.as_view()),
    path('<id>/',StatusDetailAPIView.as_view()),
#     path('<pk>/update/',StatusUpdateAPIView.as_view()),
#     path('<pk>/delete/',StatusDeleteAPIView.as_view()),
]
