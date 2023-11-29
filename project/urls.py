"""
URL configuration for project project.

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from posts.views import List_Post,Detail_post,create_post,update_post,Delete_post
from posts.api import list_post_api,detail_post_api,List_api,List_new_api,List_api_test
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="BLOG API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',List_Post.as_view()),
    path('create/',create_post.as_view()),
    path('details/<int:pk>',Detail_post.as_view()),
    path('update/<int:pk>',update_post.as_view()),
    path('delete/<int:pk>',Delete_post.as_view()),
    path('summernote/', include('django_summernote.urls')),

    path('post/api',list_post_api),
    path('details/api/<int:pk>',detail_post_api),

    path('posts/api',List_api.as_view()),
    path('posts/api/list',List_new_api.as_view()),
    path('test/api/<int:pk>',List_api_test.as_view()),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    

]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
