
from django.contrib import admin
from django.urls import path,include
from boards import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('boards.urls')),
    path('signup/',include('accounts.urls')),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),

    path('reset/',
         auth_views.PasswordResetView.as_view(

             template_name = 'password_reset.html',
             email_template_name = 'password_reset_email.html',
             subject_template_name = 'password_reset_subject.txt'
         ),
         name= 'password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),
        name ='password_reset_done.html'),

    path('reset/((?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/)',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'
         ),

    path('setting/password/',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('setting/password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),

]
