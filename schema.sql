-- Users table to store credentials and account types
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'client' -- Roles can be 'client', 'provider', or 'admin'
);

-- Appointments table to manage booking slots
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider_id INTEGER NOT NULL,
    client_id INTEGER,
    date TEXT NOT NULL, -- Recommended format: YYYY-MM-DD
    time TEXT NOT NULL, -- Recommended format: HH:MM
    status TEXT NOT NULL DEFAULT 'available', -- States: 'available', 'booked', 'canceled'
    FOREIGN KEY (provider_id) REFERENCES users (id),
    FOREIGN KEY (client_id) REFERENCES users (id)
);

-- Resources table for the community hub
CREATE TABLE resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    link TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users (id)
);

-- Indexes to speed up database queries when the app scales
CREATE INDEX idx_appointments_provider ON appointments (provider_id);
CREATE INDEX idx_appointments_client ON appointments (client_id);
CREATE INDEX idx_resources_author ON resources (author_id);