from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^crawler/', include('crawler.urls')),
    url(r'^admin/', admin.site.urls),
]
