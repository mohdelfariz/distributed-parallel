import mysql.connector
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="my_first_db"
)
print(db_connection)

# creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()
#Here creating database table as employee with primary key
db_cursor.execute(
	"ALTER TABLE countries RENAME TO countries_new")

#Get database table
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
