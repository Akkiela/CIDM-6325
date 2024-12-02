from django.urls import path
from django.views.decorators.cache import cache_page
from .views import course_detail,edit_student_work,delete_student_work,portfolio

from . import views

from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path(
        'register/',
        views.StudentRegistrationView.as_view(),
        name='student_registration',
    ),
    path(
        'enroll-course/',
        views.StudentEnrollCourseView.as_view(),
        name='student_enroll_course',
    ),
    path(
        'courses/',
        views.StudentCourseListView.as_view(),
        name='student_course_list',
    ),
    path(
        'course/<pk>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail',
    ),
    path(
        'course/<pk>/<module_id>/',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module',
    ),

    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('course/<int:course_id>/module/<int:module_id>/',course_detail, name='course_detail'),
    path('edit_work/<int:work_id>/',edit_student_work,name='edit_student_work'),
    path('delete_work/<int:work_id>/',delete_student_work,name='delete_student_work'),
    path('/portfolio/',portfolio,name='portfolio'),
   
]
