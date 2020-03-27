from django.urls import path
from .views import LoginView,RegisterView,LogoutView,get_pic

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'), #as_view()返回函数句柄
    path('logout/',LogoutView.as_view(),name='logout'),
    path('vcode/<int:num>',get_pic,name='get_pic'),

]