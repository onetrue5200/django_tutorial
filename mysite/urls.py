"""
mysite urls
"""
from django.contrib import admin
from django.urls import path, include
# register url exception for certain app(turn DEBUG = False)
handler404 = "demo.views.page_not_found"

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
]
