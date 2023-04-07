# This file is just a demo file on how to load CSV data into the database using psycopg2
import psycopg2

# Link the database called demo_database1
conn = psycopg2.connect("host=localhost dbname=demo_database1 user=postgres")
cur = conn.cursor()

# This command can only be executed once after the table has been created
# cur.execute("""
#     CREATE TABLE users(
#         id integer PRIMARY KEY,
#         email text,
#         name text,
#         address text
#     )
# """)

cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (10, 'hello@dataquest.io', 'Some Name', '123 fake st.'))
conn.commit()

cur.execute('SELECT * FROM users')

all = cur.fetchall()