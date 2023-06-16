from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<pk>', views.student_details),
    path('student-all/', views.student_details_all),
]
