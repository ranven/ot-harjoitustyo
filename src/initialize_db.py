from db_connection import get_db_connection

def initialize_database():
    connection = get_db_connection()
    create_tables(connection)
    
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PROJECTS(
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );   
        """)
    connection.commit()
    
if __name__ == "__main__":
    initialize_database()