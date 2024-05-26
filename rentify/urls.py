"""
URL configuration for rentify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rentals import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path("",views.index,name="index"),
    path("user_login",views.user_login,name="user_login"),
    path("register",views.register,name="register"),
    path('logout', views.user_logout, name='logout'),
    
    # seller_urls
    path("seller_dashboard",views.seller_dashboard,name="seller_dashboard"),
    path('post_property/', views.post_property, name='post_property'),
    path('seller_properties/', views.seller_properties, name='seller_properties'),
    path('update_property/<int:property_id>/', views.update_property, name='update_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    
    
    
    # buyer_urls 
    path("buyer_dashboard",views.buyer_dashboard,name="buyer_dashboard"),
    path('express_interest/<int:property_id>/', views.express_interest, name='express_interest'),
    path('property_filter/', views.property_filter, name='property_filter'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path("like_property/<int:property_id>/",views.like_property,name="like_property"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
