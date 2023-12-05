from django.contrib import admin
from django.urls import path

from Book.views import book_list
from Reader.views import reader_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_list/', book_list, name="book_list"),
    path('reader_list/', reader_list, name="reader_list"),
]
