from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adds/', views.add, name='home'),
    # path('customer/', include('customer.urls')),
    path('list/', views.LicenseListAPIView.as_view(), name='lic-list'),
	path('add/', views.AddLicense.as_view(), name='lic-add'),
    path('<RouterSerial>/', views.ShowLicense.as_view(), name='lic-show'),
    # path('<RouterSerial>/', views.SnippetDetail.as_view(), name='lic-show'),
	path('delete/<RouterSerial>/', views.DeleteLicense.as_view(), name='lic-delete'),
    path('user/', views.userList.as_view(),name='user'),
    path('post/', views.postList.as_view(),name='arafat'),
    # path('register/', views.register, name='register'),
]