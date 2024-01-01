from django.urls import path
from .. import views

urlpatterns = [
    path("vendors/",views.VendorListCreateAPIView.as_view()),
    path("vendors/<int:pk>/",views.VendorDetailUpdateAPIView.as_view()),
]
