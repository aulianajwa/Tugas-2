# TODO: Implement Routings Here
from django.urls import path
from todolist.views import delete_task, show_todolist, toggle_task
from todolist.views import register
from todolist.views import login_user, logout_user, create_task#sesuaikan dengan nama fungsi yang dibuat
from todolist.views import show_json, add_task
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('toggle-task/<int:id>', toggle_task, name='toggle-task'),
    path('json/',show_json, name='show_json'),
    path('add-task/', add_task, name='add_task'),
]