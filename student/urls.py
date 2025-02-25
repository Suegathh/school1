from django.urls import path
from .views import StudentView, CourseView

urlpatterns = [
    path('', StudentView.as_view(), name='student-view'),
    path('course/', CourseView.as_view(), name='course-view'),
    path('<int:id>/', StudentView.as_view(), name='student-details'),
    path('course/<int:id>/', CourseView.as_view(), name='course-details')

]
