import mysql.connector
import json

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz",
        database="rottentomatoes"
    )
def create_movies_table():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,

        name VARCHAR(255),
        score VARCHAR(10),
        reviews_count VARCHAR(50),

        description TEXT,
        poster TEXT,
        critics_consensus TEXT,

        cast_crew JSON,
        reviews JSON,
        videos JSON,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

import json
import mysql.connector

def insert_movie(data):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO movies (
            name, score, reviews_count, description,
            poster, critics_consensus,
            cast_crew, reviews, videos
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            data.get("name"),
            data.get("score"),
            data.get("reviews_count"),
            data.get("description"),
            data.get("poster"),
            data.get("critics_consensus"),

            json.dumps(data.get("cast_crew", [])),   
            json.dumps(data.get("reviews", [])),     
            json.dumps(data.get("videos", []))      
        )

        cursor.execute(query, values)
        conn.commit()

        print("Inserted:", data.get("name"))

    except Exception as e:
        print("DB INSERT ERROR:", e)

    finally:
        cursor.close()
        conn.close()