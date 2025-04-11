import sqlite3

# Connect to database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)''')

# Function to add student
def add_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()

# Add sample students
add_student("Ekta", 20, "A")
add_student("Aman", 19, "B")

# Display all students
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()

