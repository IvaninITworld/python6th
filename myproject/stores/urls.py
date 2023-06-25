from django.urls import path
from . import views

app_name = "stores"

urlpatterns = [
    # class 형태로 받아서 사용하겠다.
    path("", views.IndexView.as_view(), name="index")
]