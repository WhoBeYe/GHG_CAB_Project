import psycopg2

# Link the database called demo_database1
conn = psycopg2.connect("host=localhost dbname=demo_database1 user=postgres")
cur = conn.cursor()