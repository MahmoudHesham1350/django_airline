# django_airline

# Project Overview

This project consists of two apps: `flights` and `users`.

## ✈️ Flights App

### Default Page
- **URL:** `http://127.0.0.1:8000/flights/`
- **Description:** Shows the available flights and provides a link to each flight.

### Flight Detail Page
- **URL:** `http://127.0.0.1:8000/flights/<flight_id>/`
- **Description:** Displays information about the flight with the specified ID (`<flight_id>`), lists the passengers on this flight, and includes the ability to add passengers to this flight.

### Book a Flight
- **URL:** `http://127.0.0.1:8000/flights/<flight_id>/book/`
- **Description:** Submitting to this URL allows adding passengers to the flight with the specified ID (`<flight_id>`).

## 👤 Users App

### Default Page
- **URL:** `http://127.0.0.1:8000/users/`
- **Description:** Displays a greeting message to the logged-in user, some user information, and provides a link to log out, directing to `http://127.0.0.1:8000/users/logout/`.
- **Note:** If no user is logged in, the user is redirected to the login page at `http://127.0.0.1:8000/users/login/`.

### 🔐 Login Page
- **URL:** `http://127.0.0.1:8000/users/login/`
- **Description:** Allows the user to enter a valid username and password to log in.

## 📝 Available Accounts

### 🛠️ Admin Account
- **Username:** mahmoud
- **Password:** dummypassword
- **Email:** mahmoudhesham656@gmail.com

### 👥 User Accounts

1. **Username:** harry
   - **Password:** dummypassword
   - **First Name:** Harry
   - **Last Name:** Potter
   - **Email Address:** harrypotter@example.com

2. **Username:** ron
   - **Password:** dummypassword
   - **First Name:** Ron
   - **Last Name:** Weasley
   - **Email Address:** ronweasley@example.com
