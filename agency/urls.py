from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),


    path('search_employee',views.search_employee,name='agency-search-employee'),
    path('employee_panel', views.employee_panel, name='agency-employee-panel'),
    path('register_employee', views.register_employee, name='agency-register-employee'),
    path('employee/<str:pk>/update_employee/', views.update_employee, name='agency-update-employee'),
    path('employee/<str:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('hotel/<int:pk>/', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('delete_employee', views.delete_employee, name='agency-delete-employee'),
    path('employees',views.EmployeesView,name='agency-employees-list'),
    path('book_custom_trip/', views.book_custom_trip,name = 'agency-book-custom-trip'),
    path('book_custom_trip/<str:pk>/select_car', views.select_car, name = 'agency-select-trip-car'),
    path('book_custom_trip/<str:trip_pk>/select_car/<str:car_pk>/select_hotel', views.select_hotel, name = 'agency-select-trip-hotel'),
    path('book_fixed_trip/<int:pk>/booking', views.create_fixed_booking, name = 'agency-fixed-booking'),
    path('book_custom_trip/<str:trip_pk>/select_car/<str:car_pk>/select_hotel/<str:hotel_pk>/booking', views.create_custom_booking, name = 'agency-custom-booking'),
    path('hotels',views.HotelsView,name='agency-hotel-list'),
    path('hotel/<int:pk>/hotel_form/', views.HotelUpdateView.as_view(), name='agency-hotel-form'),
    path('add_hotel', views.add_hotel, name='agency-add-hotel'),
    path('employees_panel/fixed_trips',views.TripsView,name='agency-fixed-trips-list'),
    path('employees_panel/add_fixed_trip', views.create_fixed_trip, name='agency-fixed-trip'),
    path('browse_fixed_trips', views.browse_fixed_trips, name='agency-browse-fixed-trips'),
    path('fixed_trips/<int:pk>/', views.TripDetailView.as_view(), name='fixed-trip-detail'),
    path('delete_hotel/<int:pk>', views.delete_hotel, name='agency-delete-hotel'),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoices', views.InvoiceView, name='agency-invoice-list'),
    path('invoice/<int:pk>/payment', views.make_payment, name='agency-make-payment'),
    path('fixed_invoice/<int:pk>/', views.FixedInvoiceDetailView.as_view(), name='fixed-invoice-detail'),
    path('fixed_invoices', views.FixedInvoiceView, name='agency-fixed-invoice-list'),
    # path('fixed_invoice/<int:pk>/payment', views.make_payment, name='agency-make-payment'),
]