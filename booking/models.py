from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100, default="Kozhikode")
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(
        upload_to='hospitals/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='doctors'
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='doctors'
    )
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(
        upload_to='doctors/',
        blank=True,
        null=True
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.name}"


class DoctorAvailability(models.Model):
    DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='availability'
    )
    day = models.CharField(
        max_length=10,
        choices=DAYS
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    class Meta:
        verbose_name = "Doctor Availability"
        verbose_name_plural = "Doctor Availabilities"

    def __str__(self):
        return (
            f"Dr. {self.doctor.name} - "
            f"{self.day} - "
            f"{self.start_time} to {self.end_time}"
        )


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-appointment_date", "appointment_time"]
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "doctor",
                    "appointment_date",
                    "appointment_time",
                ],
                name="unique_doctor_appointment_slot",
            )
        ]
    def __str__(self):
        return (
            f"{self.patient} - {self.doctor} - "
            f"{self.appointment_date} {self.appointment_time}"
        )


class PatientProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_profile",
    )
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    profile_photo = models.ImageField(
        upload_to="patient_profiles/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("booking", "Appointment Booked"),
        ("confirmed", "Appointment Confirmed"),
        ("cancelled", "Appointment Cancelled"),
        ("reminder", "Appointment Reminder"),
    ]

    user = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    title = models.CharField(max_length=150)
    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
        default="booking",
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

    class Meta:
        ordering = ["-created_at"]




# Create your models here.
