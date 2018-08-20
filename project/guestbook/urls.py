from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path(''                                         , TemplateView.as_view(template_name='frontend/index.html'), name='index'),
    path('api/guestbooks'                           , views.guestbooks, name='guestbooks'),
    path('api/guestbook/create'                     , csrf_exempt(views.create_guestbook), name='create_guestbook'),
    path('api/guestbook/edit/<int:guestbook_id>'    , csrf_exempt(views.edit_guestbook), name='edit_guestbook'),
    path('api/guestbook/remove/<int:guestbook_id>'  , csrf_exempt(views.remove_guestbook), name='remove_guestbook')
]

urlpatterns += staticfiles_urlpatterns()