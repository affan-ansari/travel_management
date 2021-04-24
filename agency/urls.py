from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),


    path('search_employee',views.search_employee,name='agency-search-employee'),
    path('manage_employee', views.manage_employee, name='agency-manage-employee'),
    path('register_employee', views.register_driver, name='agency-register-employee'),
    path('employee/<str:pk>/update_employee/', views.update_employee, name='agency-update-employee'),
    path('employee/<str:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('delete_employee', views.delete_employee, name='agency-delete-employee'),
    path('employees',views.EmployeesView,name='agency-employees-list'),
]