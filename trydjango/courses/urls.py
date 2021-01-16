from django.urls import path
from .views import my_fbv, CourseView, CourseCreateView,CourseUpdateView
urlpatterns = [
    path('', CourseView.as_view(template_name = 'contact.html'), name = 'courses-list'),

    path('<int:id>/', CourseView.as_view(), name = 'courses-detail'),

    path('create/', CourseCreateView.as_view(), name = 'course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name = 'course-update')
]