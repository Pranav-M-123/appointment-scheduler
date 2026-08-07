# Community-Driven Appointment Scheduler & Resource Hub
#### Video Demo: https://youtu.be/hSdpSdYpIJg
#### Description:
The Community-Driven Appointment Scheduler & Resource Hub is a full-stack web application designed to connect community members through an online instruction scheduling system and a shared educational resource library. Built as my final project for CS50x, this application solves the real-world problem of disorganized peer-to-peer tutoring and community knowledge sharing by centralizing both scheduling and resource distribution into a single, intuitive platform.

## Design Choices & Architecture
When designing this application, I had to make several key structural decisions. I chose Python and the Flask framework for the backend because of its lightweight nature and seamless integration with Jinja2 templating, which we utilized heavily in Week 9 of the course. 

For the database, I opted for SQLite3. While a more robust system like PostgreSQL could handle larger-scale applications, SQLite3 was the perfect fit for this scope, allowing for quick iteration and easy local testing without the overhead of running a separate database server. I designed a relational schema with three main tables: `users`, `appointments`, and `resources`. A major design choice here was utilizing foreign keys to link appointments to two different users simultaneously (a `provider_id` and a `client_id`). This allowed me to build a dynamic, dual-view dashboard.

On the frontend, I utilized Bootstrap 5. I decided to rely on Bootstrap's grid system and pre-built components (like cards and accordions) to ensure the application was mobile-responsive and accessible out of the box. I supplemented this with a custom `styles.css` file to add modern hover effects and softer UI elements, prioritizing user experience.

## File Hierarchy and Functions

### Backend & Database
* **`app.py`**: This is the core engine of the application. It handles all route definitions, session management, and database executions. It includes complex SQL `JOIN` queries to fetch readable usernames rather than raw user IDs when populating the dashboard.
* **`schema.sql`**: Contains the `CREATE TABLE` commands and indexing logic to build the relational database.
* **`project.db`**: The live, local SQLite database containing the registered users, booked timeslots, and shared links.

### Frontend Templates
* **`layout.html`**: The foundational Jinja template. It includes the Bootstrap CDN, the responsive navigation bar (which dynamically renders links based on active session state), and a centralized flash-message container.
* **`index.html`**: The welcoming landing page containing a call-to-action hero section.
* **`register.html` & `login.html`**: The user authentication interfaces. The backend logic tied to these forms utilizes Werkzeug's security libraries to hash and verify passwords.
* **`dashboard.html`**: The most complex view in the application. It splits the user interface into two compartments: "Sessions I'm Attending" and "Students I'm Instructing." This caters to the dual nature of community learning, where a user can be both a student and a teacher.
* **`book.html`**: The scheduling engine. It queries the database for all available providers and populates a dropdown form for easy selection.
* **`resources.html`**: The community hub. It features a collapsible form for submitting new resources (keeping the UI uncluttered) and a dynamic feed iterating through the database to display links shared by peers.

## Future Implementation
If I were to expand this project, I would implement a time-conflict validation system in the `/book` route to prevent double-booking, and add a timezone converter for the scheduling form to accommodate a global community.
