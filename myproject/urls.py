
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


]
