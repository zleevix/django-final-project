from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views # Import xong đổi tên :)
from . import views # File urls.py và views.py cùng 1 folder
from . import base_class_views
from . import user_views
# app_name = "myapp" # dành cho nhiều web app
# Khi định nghĩa xong, thì name của url phải thêm dạng `app_name:<tên view>`
urlpatterns = [
    # Hàm views
    url(r"^$", views.index, name="index"), # ^$ là bắt đầu và kết thúc luôn thì nó rỗng :))
    url(r"^list-reporter$", views.list_reporter, name="list_reporters"), # ^$ là bắt đầu và kết thúc luôn thì nó rỗng :))
    url(r"^search", views.search_reporter, name="search_reporter"),
    url(r"^add-reporter$", views.add_reporter, name="add_reporter"),
    url(r"^add-article$", views.add_article, name="add_article"),
    url(r"^validate-email$", views.validate_email, name="validate_email"),
    url(r"^validate-username$", views.validate_username, name="validate_username"),
    # Step 2: vào urls.py của app để thêm đường dẩn tới views mới tạo
    # path("reporter/<int:reporter_id>", views.view_detail_reporter, name = "view_detail_reporter"),
    url(r"^reporter/(?P<reporter_id>[0-9]+)$",views.view_detail_reporter, name = "view_detail_reporter"),
    url(r"^update-reporter/(?P<reporter_id>[0-9]+)$",views.update_reporter, name = "update_reporter"),
    url(r"^delete-reporter/(?P<reporter_id>[0-9]+)$",views.delete_reporter, name = "delete_reporter"),
    # Class base view
    url(r"^all-reporter$", base_class_views.ReportListView.as_view(), name="all_reporters"),
    url(r"^view-reporter/(?P<pk>[0-9]+)$", base_class_views.ReporterDetailView.as_view(), name="view_reporter"),
    url(r"^insert-reporter$", base_class_views.ReporterCreateView.as_view(), name="insert_reporter"),
    url(r"^edit-reporter/(?P<pk>[0-9]+)$", base_class_views.ReporterUpdateView.as_view(), name="edit_reporter"),
    url(r"^remove-reporter/(?P<pk>[0-9]+)$", base_class_views.ReporterDeleteView.as_view(), name="remove_reporter"),

    # User authentication/authorization
    url(r"^register$", user_views.register_user, name="register_user"),
    url(r"^login$", user_views.login_user, name="login_user"),
    url(r"^logout$", auth_views.LogoutView.as_view(next_page="/"), name="logout_user"),
    url(r"^change-password$", auth_views.PasswordChangeView.as_view(template_name="user/change_password.html"), name="change_password"),
]