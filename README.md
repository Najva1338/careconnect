# CareConnect – Doctor Appointment Booking System

**CareConnect** is a Django-based doctor appointment booking web application designed to help patients find doctors, explore hospitals, and book appointments easily in Calicut (Kozhikode), Kerala.

The application provides separate dashboards for patients, doctors, and staff, along with an AI-powered Care Guide to help patients identify suitable medical specializations based on their symptoms.

## Project Overview

CareConnect aims to simplify the doctor appointment booking process by connecting patients, doctors, hospitals, and healthcare staff through a single web application.

The system provides an easy-to-use and responsive interface that works on both mobile phones and desktop computers.

## Main Features

### 1. User Authentication
- Patient registration and login.
- Secure logout functionality.
- Role-based access control.

### 2. Doctor Management
- Browse available doctors.
- View doctor profiles and specializations.
- View hospital details.
- Staff can add, edit, and manage doctor information.

### 3. Hospital Management
- View hospitals in Calicut.
- View hospital details and contact information.
- Staff can add, edit, and manage hospital information.

### 4. Appointment Management
- Book doctor appointments.
- View personal appointments.
- Manage appointment status.
- Cancel appointments.
- Prevent duplicate doctor appointment time slots.

### 5. Patient Dashboard
- View appointment details.
- Track appointment status.
- Receive notifications.

### 6. Doctor Dashboard
- View patient appointments.
- Manage appointment requests.
- Update appointment statuses.

### 7. Staff Dashboard
- View appointment statistics.
- Manage doctors and hospitals.
- Search and filter appointments.
- Update appointment statuses.

### 8. AI Care Guide
- Patients can enter their symptoms.
- AI provides general guidance about suitable medical specializations.
- Helps patients identify which type of doctor they may consult.

*AI suggestions are informational only and do not replace professional medical diagnosis or advice.*

### 9. Responsive Design
- Bootstrap-based user interface.
- Mobile-friendly layouts.
- Desktop and laptop support.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application framework |
| SQLite | Database |
| HTML5 | Web page structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| JavaScript | Frontend interactions |
| Ollama | Local AI integration |

## Project Structure

```text
CareConnect/
│
├── booking/
│   ├── migrations/
│   ├── templates/
│   │   └── booking/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── decorators.py
│   └── admin.py
│
├── careconnect/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Najva1338/careconnect.git
cd careconnect
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Set your Django secret key before running the application.

Windows Command Prompt:

```cmd
set DJANGO_SECRET_KEY=your-secret-key
```

For the AI Care Guide, make sure Ollama is installed and the required local AI model is available.

### Step 5: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 6: Create an Admin Account

```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```

## Database

CareConnect uses SQLite for storing application data, including:

- User information
- Doctor details
- Hospital information
- Appointment records
- Patient notifications

## Future Enhancements

- Online payment integration.
- Email and SMS appointment reminders.
- Advanced AI-based healthcare assistance.
- Doctor availability calendar.
- Online consultation facilities.

## Project Information

**Project Name:** CareConnect

**Domain:** Healthcare / Doctor Appointment Booking

**Location Focus:** Calicut (Kozhikode), Kerala

**Developer:** Najva1338

**Framework:** Django

**Repository:** https://github.com/Najva1338/careconnect

---

*CareConnect – Making healthcare access easier and more convenient.*
