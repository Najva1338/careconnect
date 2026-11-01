
from django import forms
from django.utils import timezone
from .models import Appointment
from django.contrib.auth import get_user_model
from .models import PatientProfile
from .models import Doctor
from .models import Hospital

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
        


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'name',
            'specialization',
            'hospital',
            'qualification',
            'experience',
            'consultation_fee',
            'phone',
            'email',
            'bio',
            'profile_photo',
            'is_available',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter doctor name'
            }),
            'specialization': forms.Select(attrs={
                'class': 'form-select'
            }),
            'hospital': forms.Select(attrs={
                'class': 'form-select'
            }),
            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. MBBS, MD'
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Years of experience'
            }),
            'consultation_fee': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Consultation fee'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'profile_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = [
            'name',
            'address',
            'city',
            'phone',
            'email',
            'image',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Hospital name'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

        

