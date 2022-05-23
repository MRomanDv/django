from django.contrib import admin
from django.urls import path
from book_api.views import books_list

urlpatterns = [
    path('list/', admin.site.urls),
]