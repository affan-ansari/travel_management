from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),


    path('search_employee',views.search_employee,name='agency-search-employee'),
    path('manage_employee', views.manage_employee, name='agency-manage-employee'),
    path('register_employee', views.register_employee, name='agency-register-employee'),
    path('employee/<str:pk>/update_employee/', views.update_employee, name='agency-update-employee'),
    path('employee/<str:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('delete_employee', views.delete_employee, name='agency-delete-employee'),
    path('employees',views.EmployeesView,name='agency-employees-list'),
    path('book_custom_trip/', views.book_custom_trip,name = 'agency-book-custom-trip'),
    path('book_custom_trip/<str:pk>/select_car', views.select_car, name = 'agency-select-trip-car'),
    path('book_custom_trip/<str:trip_pk>/select_car/<str:car_pk>/select_hotel', views.select_hotel, name = 'agency-select-trip-hotel'),
    path('book_custom_trip/<str:trip_pk>/select_car/<str:car_pk>/select_hotel/<str:hotel_pk>/booking', views.create_booking, name = 'agency-booking'),
    path('hotels',views.HotelsView,name='agency-hotel-list'),
    path('hotel/<int:pk>/hotel_form/', views.HotelUpdateView.as_view(), name='agency-hotel-form'),
    path('add_hotel', views.add_hotel, name='agency-add-hotel'),
]