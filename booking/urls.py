
from django.urls import path
from . import views

urlpatterns = [
    path("", views.onboarding, name="onboarding"),
    path("home/", views.home, name="home"),

    path("doctors/", views.doctors_list, name="doctors_list"),

    path(
        "doctor/<int:doctor_id>/",
        views.doctor_detail,
        name="doctor_detail",
    ),

    path(
        "book-appointment/<int:doctor_id>/",
        views.book_appointment,
        name="book_appointment",
    ),
    
    path(
    "available-slots/<int:doctor_id>/",
    views.available_slots,
    name="available_slots",
    ),

    
    path(
        "appointment-confirmation/<int:appointment_id>/",
        views.appointment_confirmation,
        name="appointment_confirmation",
    ),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('my-appointments/', views.my_appointments, name='my_appointments'),
    path(
    "ai-care-guide/",
    views.ai_care_guide,
    name="ai_care_guide",
    ),
    path(
    "cancel-appointment/<int:appointment_id>/",
    views.cancel_appointment,
    name="cancel_appointment"
),
path(
    "patient-profile/",
    views.patient_profile,
    name="patient_profile",
),
path(
    "patient-dashboard/",
    views.patient_dashboard,
    name="patient_dashboard",
),
path(
    "notifications/",
    views.notification_list,
    name="notification_list",
),
path(
    "notifications/read/<int:notification_id>/",
    views.mark_notification_read,
    name="mark_notification_read",
),
path(
    "notifications/read-all/",
    views.mark_all_notifications_read,
    name="mark_all_notifications_read",
),
]