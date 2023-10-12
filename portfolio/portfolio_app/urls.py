from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name= 'students'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('portfolios/', views.PortfolioListView.as_view(), name= 'portfolios'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('projects/', views.ProjectListView.as_view(), name= 'projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
]
