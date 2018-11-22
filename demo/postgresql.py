import psycopg2

conn = psycopg2.connect(database="exampledb", user="dbuser", password="", host="127.0.0.1", port="5432")


cur = conn.cursor()
cur.execute('select * from student')
rows = cur.fetchall()
for row in rows:
    print(f'name:{row[0]}\nid:{row[1]}')
cur.close()
conn.close()
