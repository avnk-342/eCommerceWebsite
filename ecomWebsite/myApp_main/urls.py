from django.urls import path
from myApp_main.views import index

app_name = "myApp_main"
urlpatterns = [
    path("",index)
]
