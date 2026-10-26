from django.contrib import admin
from .models import (
    Specialization,
    Hospital,
    Doctor,
    DoctorAvailability,
    Appointment,
)

from .models import Notification

admin.site.register(Notification)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'email')
    search_fields = ('name', 'city')
    list_filter = ('city',)
class DoctorAvailabilityInline(admin.TabularInline):
    model = DoctorAvailability
    extra = 7



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
        'hospital',
        'experience',
        'consultation_fee',
        'is_available',
    )

    search_fields = (
        'name',
        'specialization__name',
        'hospital__name',
    )

    list_filter = (
        'specialization',
        'hospital',
        'is_available',
    )

    inlines = [DoctorAvailabilityInline]


@admin.register(DoctorAvailability)
class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'doctor',
        'day',
        'start_time',
        'end_time',
    )
    list_filter = ('day', 'doctor')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status',
        'created_at',
    )
    search_fields = (
        'patient__username',
        'doctor__name',
    )
    list_filter = (
        'status',
        'appointment_date',
        'doctor',
    )
# Register your models here.
