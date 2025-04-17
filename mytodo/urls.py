from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("", include("todo.urls"))
]

handler400 = 'mytodo.views.bad_request'
handler403 = 'mytodo.views.permission_denied'
handler404 = 'mytodo.views.page_not_found'
handler500 = 'mytodo.views.server_error'

