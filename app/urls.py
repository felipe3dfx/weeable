from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout
from django.utils.translation import ugettext_lazy as _


admin.site.site_title = _('Knowledge Base')
admin.site.site_header = _('Knowledge Base')


urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),

    url(
        r'^markdownx/',
        include('markdownx.urls')
    ),

    url(
        _(r'^logout/$'),
        logout,
        {'next_page': '/'},
        name='logout'
    ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
