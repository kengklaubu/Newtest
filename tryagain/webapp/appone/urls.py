from django.urls import path
from appone.views import Show

urlpatterns = [
    path("", Show.as_view(), name="Show")

]