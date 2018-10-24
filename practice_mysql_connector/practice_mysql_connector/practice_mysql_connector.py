import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="oneofthezombies"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE opentutorials")  # opentutorials = database name
#mycursor.execute("DROP DATABASE opentutorials")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("USE opentutorials")
#mycursor.execute("SET PASSWORD = PASSWORD('oneofthezombies')") # oneofthezombies = password
#mycursor.execute("exit")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("DESC topic") # topic = table name
#mycursor.execute("INSERT INTO topic (title,description,created,author,profile) VALUES('MySQL','MySQL is ...',NOW(),'egoing','developer'")  # MySQL = title, My SQL is ... = description, NOW() = created, egoing = author, developer = prifle
#mycursor.execute("SELECT * FROM topic")
#mycursor.execute("SELECT id, title, created, author FROM topic")
#mycursor.execute("SELECT id, title, created, author FROM topic WHERE author='egoing'")
#mycursor.execute("SELECT id, title, created, author FROM topic WHERE author='egoing' ORDER BY id DESC LIMIT 2")
#mycursor.execute("RENAME TABLE topic TO topic_backup")
#mycursor.execute("SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id")
#mycursor.execute("SELECT topic.id, title, description, created, name, profile FROM topic LEFT JOIN author ON topic.author_id = author.id")
#mycursor.execute("SELECT topic.id AS topic_id, title, description, created, name, profile FROM topic LEFT JOIN author ON topic.author_id = author.id")
#mycursor.execute("UPDATE author SET profile='database administrator' WHERE id = 2")
#mycursor.execute("SELECT DISTINCT Country FROM Customers")
#mycursor.execute("SELECT COUNT(DISTINCT Country) FROM Customers")
