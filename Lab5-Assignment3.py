# Answers for Assignment-3

# Importing mySQL connector
import mysql.connector

# Initialize database connection properties
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="my_first_db"
)

# Show newly created database (my_first_db should be on the list)
print(db_connection)

# (a)Write a MySQL statement to create a simple table countries including columns-country_id, country_name and region_id.

# 1) Creating database_cursor to perform SQL operation
db_cursor = db_connection.cursor()

# 2) We create and execute command to create a database table (countries)
db_cursor.execute(
	"CREATE TABLE countries(country_id INT AUTO_INCREMENT PRIMARY KEY, country_name VARCHAR(255), region_id INT(6))")

# 3) Print the database table (Table countries should be on the list)
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
	
# (b)Write a MySQL statement to rename the table countries to country_new.
	
# 1) Altering the database table countries name
db_cursor.execute(
	"ALTER TABLE countries RENAME TO country_new")

# 2) Print the newly altered table (countries should changed to country_new)
db_cursor.execute("SHOW TABLES")
for table in db_cursor:
	print(table)
