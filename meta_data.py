import sqlite3

# Connect to SQLite database 
db_path = "metadata.db"
connection = sqlite3.connect(db_path)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()


create_documents_table = """
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    upload_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    path TEXT NOT NULL
);
"""

create_queries_table = """
CREATE TABLE IF NOT EXISTS queries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    document_id INTEGER NOT NULL,
    query TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
);
"""


cursor.execute(create_documents_table)
cursor.execute(create_queries_table)


connection.commit()
connection.close()

print(f"Database initialized at {db_path}")
