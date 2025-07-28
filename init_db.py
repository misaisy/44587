import psycopg2
conn = psycopg2.connect(host='db', user='postgres', password='secret', dbname='mydb')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50), email VARCHAR(50));")
conn.commit()
print("Table created!")