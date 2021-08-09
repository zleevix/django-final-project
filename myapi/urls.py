from os import name
from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
urlpatterns = [
    # Hàm views
    url(r'^token$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r"^reporters$", views.api_all_reporter, name="api_all_reporter"),
    url(r"^reporters-class$", views.ReporterListAPI.as_view()),
    url(r"^reporter-class/(?P<reporter_id>[0-9]+)$", views.ReporterAPI.as_view()),
    url(r"^add-reporters$", views.api_add_reporter, name="api_add_reporter"),
    url(r"^reporter/(?P<reporter_id>[0-9]+)$", views.api_view_reporter, name="api_view_reporter"),
    url(r"^update-reporter/(?P<reporter_id>[0-9]+)$", views.api_update_reporter, name="api_update_reporter"),
    url(r"^patch-reporter/(?P<reporter_id>[0-9]+)$", views.api_patch_reporter, name="api_patch_reporter"),
    url(r"^delete-reporter/(?P<reporter_id>[0-9]+)$", views.api_delete_reporter, name="api_delete_reporter")
]