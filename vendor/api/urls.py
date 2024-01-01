from django.urls import path
from .. import views

urlpatterns = [
    path("",views.VendorListCreateAPIView.as_view()),
    path("<int:pk>/",views.VendorDetailUpdateAPIView.as_view()),
]
