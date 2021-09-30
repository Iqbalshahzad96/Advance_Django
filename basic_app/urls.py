from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('schools/', views.SchoolListView.as_view(), name='list'),
    path('schools/<int:pk>/', views.SchoolDetailView.as_view(), name='detail'),

]