from django.urls import path
from . import views
from .views import days, day_plan, update
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name= "home"),
    path('register/', views.registerPage, name = "register"),
    path('login/', views.loginPage, name="login"), 
    path('logout', views.logoutUser, name = "logout"),
    path('upload/', views.upload, name = "upload"),
    path('days/', days.as_view(), name = "days"),
    path('day_plan/', views.day_plan,name = 'day_plan'),
    path('update/<int:pk>/', views.update, name = 'update'),
    path('form_submitted', views.form_submitted, name = "form_submitted"),
    path('day_plan2/', views.day_plan2,name = 'day_plan2'),
    path('rec/', views.rec1,name = 'rec'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
]
