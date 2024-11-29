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
    path(
        '<pk>/module/',
        views.CourseModuleUpdateView.as_view(),
        name='course_module_update',
    ),
    path(
        'module/<int:module_id>/content/<model_name>/create/',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_create',
    ),
    path(
        'module/<int:module_id>/content/<model_name>/<id>/',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_update',
    ),
    path(
        'content/<int:id>/delete/',
        views.ContentDeleteView.as_view(),
        name='module_content_delete',
    ),
    path(
        'module/<int:module_id>/',
        views.ModuleContentListView.as_view(),
        name='module_content_list',
    ),
    path(
        'module/order/',
        views.ModuleOrderView.as_view(),
        name='module_order',
    ),
    path(
        'content/order/',
        views.ContentOrderView.as_view(),
        name='content_order',
    ),
    path(
        '<pk>/module/',
        views.CourseModuleUpdateView.as_view(),
        name='course_module_update',
    ),
]