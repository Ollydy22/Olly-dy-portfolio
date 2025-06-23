from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line sends any request to the root URL to our portfolio app's urls.
    path('', include('portfolio.urls')),
]
