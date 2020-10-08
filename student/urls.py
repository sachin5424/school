
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token
from .views import RegisterView,ChangePasswordView,new_account
from student import views
app_name='student'
urlpatterns = [

    path('',views.student_list_view.as_view(),name='list_view'),
    path('update_view/<int:pk>',views.student_list_view_update.as_view(),name='update_view'),
    path('delete_view/<int:pk>',views.student_list_view_delete.as_view(),name='delete_view'),
    path('student_list_create_view/',views.student_list_create.as_view(),name='student_list_create'),

   # api urls
    path('register/',RegisterView.as_view(),name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('new_account/',new_account,name='new_account'),
    path('api-token/',obtain_jwt_token),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # ----------------api confirm password_reset ur-------------------------------l
    #-------------------- http://localhost:8000/student/api/password_reset/confirm/------------------------ 
    # ----------------api confirm password_reset ur-------------------------------
    # end api user
]
