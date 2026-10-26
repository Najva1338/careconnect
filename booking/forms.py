
from django import forms
from django.utils import timezone
from .models import Appointment
from django.contrib.auth import get_user_model
from .models import PatientProfile

User = get_user_model()


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {
            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
                
            "appointment_time": forms.Select(
                 attrs={
                    "class": "form-select",
                    "id": "appointment_time",
                },
                choices=[("", "Select a date first")],
            ),


            "reason": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Describe your reason for visiting (optional)",
                }
            ),
        }

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data["appointment_date"]

        if appointment_date < timezone.localdate():
            raise forms.ValidationError(
                "Please select today or a future date."
            )
        return appointment_date
        


class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your first name",
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your last name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email address",
            }),
        }


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ["phone", "address", "profile_photo"]

        widgets = {
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number",
            }),
            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Enter your address",
            }),
            "profile_photo": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
            }),
        }

        

