import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and Table Created Successfully")