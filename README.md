# Community-Driven Appointment Scheduler & Resource Hub
#### Video Demo:  [VIDEO URL HERE]
#### Description:
A full-stack web application designed to connect community members through an online instruction scheduling system and a shared resource library. Built as a final project for CS50x.

## Technologies Used
* **Backend:** Python, Flask, Flask-Session
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, Bootstrap 5, Jinja2

## Core Features
1. **User Authentication:** Secure registration and login system utilizing Werkzeug password hashing.
2. **Dual-View Dashboard:** A custom interface that dynamically separates sessions a user is attending (as a student) from sessions they are hosting (as an instructor).
3. **Booking Engine:** A streamlined interface for users to select available instructors, dates, and times, saving the appointments relationally in the database.
4. **Community Resource Hub:** A feed where users can share educational links, materials, and guides with the rest of the community.

## Project Structure
* `app.py`: The core Flask application containing all backend routing, authentication logic, and database queries.
* `schema.sql`: The database schema outlining the relational tables for `users`, `appointments`, and `resources`.
* `project.db`: The local SQLite database generated from the schema.
* `static/styles.css`: Custom CSS styling for hover effects, card aesthetics, and layout spacing.
* `templates/`: 
  * `layout.html`: The base Jinja template containing the Bootstrap navbar and flash message logic.
  * `index.html`: The welcome landing page.
  * `register.html` & `login.html`: The user authentication forms.
  * `dashboard.html`: The dual-compartment view for upcoming scheduled sessions.
  * `book.html`: The form engine for scheduling new appointments.
  * `resources.html`: The interactive feed for submitting and viewing shared community links.

#### Author
Pranav Maturi
