from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


#imported the signup function from views.py to routed a path signup
urlpatterns = [
	path('signup/',views.signup,name='signup'),
	path('signin/',views.signin,name='signin'),
	path('',views.homePage,name='home'),
	path('logout/',views.logoutPage,name='logout'),
	
	path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
	path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name= 'password_reset_complete')
]