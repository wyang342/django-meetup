from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', include('meetup_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
