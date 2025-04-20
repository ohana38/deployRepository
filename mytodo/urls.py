from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500
from mytodo.views import bad_request, permission_denied, page_not_found, server_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("", include("todo.urls"))
]

handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error

# handler400 = 'mytodo.views.bad_request'
# handler403 = 'mytodo.views.permission_denied'
# handler404 = 'mytodo.views.page_not_found'
# handler500 = 'mytodo.views.server_error'

