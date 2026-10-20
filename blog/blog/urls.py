from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    path('book/new/', views.create_book, name='create_book'),
    path('register/', views.register, name='register'),   # ← добавили
    path('login/', views.login_view, name='login'),       # ← добавили
    path('logout/', views.logout_view, name='logout'),    # ← добавили
    re_path(r'^book/(?P<book_id>\d+)/$', views.get_book, name='get_book'),
]