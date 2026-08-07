# Community-Driven Appointment Scheduler & Resource Hub
#### Video Demo:  [YOUR VIDEO URL HERE]
#### Description:
The Community-Driven Appointment Scheduler & Resource Hub is a comprehensive, full-stack web application meticulously engineered to connect community members through an online instruction scheduling system and a robust shared educational resource library. Built as the capstone final project for CS50x, this software seeks to bridge the gap between eager learners and knowledgeable instructors by centralizing both the booking process and the distribution of crucial educational materials into a single, cohesive platform. As a student focused on computer engineering, I approached this project with a strong emphasis on scalable architecture, modular design, and robust database management, ensuring the backend systems could efficiently handle concurrent requests and maintain high data integrity.

The application solves the persistent, real-world problem of fragmented peer-to-peer tutoring and community knowledge sharing. Traditionally, finding an instructor, negotiating a time, and sharing study materials requires multiple disparate applications, leading to friction and lost educational opportunities. By combining a relational scheduling engine with a community resource feed, this platform eliminates those barriers, fostering a more collaborative and accessible learning environment. The implementation of this system significantly reduces the cognitive load on users, allowing them to focus entirely on the educational content rather than the logistics of coordination.

## Technical Architecture & Design Choices
The backend is powered by Python and the Flask framework, selected for its lightweight efficiency and seamless integration with Jinja2 templating. I utilized Flask-Session to maintain secure, server-side user state management, ensuring that users can navigate seamlessly between booking sessions and sharing resources without compromising their authentication status. 

For the database tier, I engineered a relational schema using SQLite3. While larger enterprise applications might leverage PostgreSQL or MySQL, SQLite3 provided the optimal balance of zero-configuration deployment and relational robustness necessary for this scope. The database architecture relies on three primary, normalized tables: `users`, `appointments`, and `resources`. A significant design challenge was representing the dual nature of our users, who can act as both students and instructors simultaneously. I resolved this by employing foreign keys in the `appointments` table that link to the `users` table twice (as `provider_id` and `client_id`), enabling complex `JOIN` queries to dynamically populate the user dashboard based on their current role.

The frontend interface is constructed with HTML5, CSS3, and Bootstrap 5. I heavily leveraged Bootstrap's responsive grid system and modern component library to ensure the application remains fully accessible and visually consistent across all device sizes. To elevate the user experience beyond standard templates, I integrated a custom CSS stylesheet that introduces subtle hover effects, modernized card aesthetics, and refined layout spacing, creating a professional and inviting environment for community members.

## File Directory and Core Functions

* `app.py`: Serving as the central controller, this file contains all backend routing logic, user authentication handlers, and direct SQL execution commands. It securely processes form submissions and dynamically renders the appropriate views based on the user's session data.
* `schema.sql`: This file defines the structural foundation of the database, explicitly detailing the table creations, primary keys, and relational constraints required to maintain data consistency.
* `project.db`: The live, local SQLite database generated directly from the schema instructions.
* `static/styles.css`: The custom stylesheet responsible for the polished, interactive visual elements that override default Bootstrap behaviors.
* `templates/layout.html`: The base Jinja template that establishes the site's uniform skeleton, housing the responsive navigation bar and the centralized logic for displaying dynamic flash messages.
* `templates/dashboard.html`: The most sophisticated view in the application, featuring a dual-compartment layout that distinctly separates the sessions a user is attending from the sessions they are actively teaching.
* `templates/book.html`: The dedicated scheduling engine interface, allowing users to query available instructors and reserve open time slots.
* `templates/resources.html`: The interactive community hub designed for the seamless submission and visualization of shared educational links and study guides.

## Future Implementations and Roadmap
Looking forward, there are several key features planned to enhance the application's functionality. First, integrating a timezone conversion utility will allow users from different geographical locations to coordinate seamlessly without mental math errors. Additionally, implementing a robust time-conflict validation system within the booking engine will ensure that instructors cannot be double-booked for the same time slot, further increasing the reliability of the platform. Finally, adding a comprehensive search and tagging system to the resources hub will enable users to quickly filter and discover specific educational materials, transforming the feed into a highly organized and searchable database.

#### Author
Pranav Maturi
