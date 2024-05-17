-- Create a simple students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER,
    email VARCHAR(100)
);

-- Insert 20 rows of sample data into the students table
INSERT INTO students (first_name, last_name, age, email) VALUES
('John', 'Doe', 20, 'john.doe@example.com'),
('Jane', 'Doe', 21, 'jane.doe@example.com'),
('James', 'Smith', 22, 'james.smith@example.com'),
('Emily', 'Johnson', 23, 'emily.johnson@example.com'),
('Michael', 'Brown', 24, 'michael.brown@example.com'),
('Emma', 'Davis', 25, 'emma.davis@example.com'),
('Christopher', 'Miller', 26, 'christopher.miller@example.com'),
('Olivia', 'Wilson', 27, 'olivia.wilson@example.com'),
('Daniel', 'Moore', 28, 'daniel.moore@example.com'),
('Sophia', 'Taylor', 29, 'sophia.taylor@example.com'),
('Andrew', 'Anderson', 20, 'andrew.anderson@example.com'),
('Isabella', 'Thomas', 21, 'isabella.thomas@example.com'),
('Joshua', 'Jackson', 22, 'joshua.jackson@example.com'),
('Ava', 'White', 23, 'ava.white@example.com'),
('Matthew', 'Harris', 24, 'matthew.harris@example.com'),
('Mia', 'Martin', 25, 'mia.martin@example.com'),
('David', 'Thompson', 26, 'david.thompson@example.com'),
('Charlotte', 'Garcia', 27, 'charlotte.garcia@example.com'),
('Joseph', 'Martinez', 28, 'joseph.martinez@example.com'),
('Amelia', 'Robinson', 29, 'amelia.robinson@example.com');
