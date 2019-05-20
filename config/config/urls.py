from django.contrib import admin
from django.urls import path, include
import theme.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', theme.views.home, name="home"),
    path('index/', include('theme.urls')),
    path('blog/', theme.views.blog, name='blog'),
    path('contact/', theme.views.contact, name='contact'),
    path('blogform/', theme.views.blogform, name='blogform'),
    path('blog/<int:pk>/edit/', theme.views.edit, name='edit'),
    path('blog/<int:pk>/remove/', theme.views.remove, name='remove'),
    path('blog/<int:pk>/detail/', theme.views.detail, name='detail'),
    path('detail/<int:pk>/edit/<int:blog_pk>/',
         theme.views.comment_edit, name='comment_edit'),
    path('detail/<int:pk>/remove/<int:blog_pk>/',
         theme.views.comment_remove, name='comment_remove'),
]
