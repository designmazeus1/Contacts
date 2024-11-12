from django.urls import path
from .views import (
    ContactListApiView,
    ContactDetailApiView
)

urlpatterns = [
    path('', ContactListApiView.as_view(), name="apicontact1"),
    path('<int:contact_id>/', ContactDetailApiView.as_view(),name="apicontact2"),
]