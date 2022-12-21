from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('authentication.urls')),
    path('signin/', include('rest_framework.urls'))
]
