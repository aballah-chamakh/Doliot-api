from django.conf.urls import include
from django.contrib import admin
from django.urls import path,re_path

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

from thing import urls as thingUrl
from account import urls as accountUrl
from documentation import urls as documentationUrl
from comment import urls as commentUrl
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(thingUrl)),
    path('api/', include(accountUrl)),
    path('api/', include(documentationUrl)),
    path('api/', include(commentUrl)),
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh', refresh_jwt_token, name='token_refresh'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += [
re_path(r'(?P<path>.*)',TemplateView.as_view(template_name='base.html')),
]
