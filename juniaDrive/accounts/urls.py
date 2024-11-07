from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
     path('folders/', views.folder_list, name='folder_list'),
    # path('folders/<int:folder_id>/upload/', views.upload_file, name='upload_file'),
    path('folders/<int:folder_id>/', views.folder_detail, name='folder_detail'),
     path('create_folder/', views.create_folder, name='create_folder'),
      
    path('folders/<int:folder_id>/', views.folder_detail, name='folder_detail'),
    path('folders/<int:folder_id>/upload/', views.file_upload, name='file_upload'),
    path('file/<int:file_id>/delete/', views.delete_file, name='delete_file'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('file/<int:file_id>/move/', views.move_file, name='move_file'),
     path('file/<int:file_id>/copy/', views.copy_file, name='copy_file'),
      path('folder/<int:folder_id>/delete/', views.delete_folder, name='delete_folder'),
]
