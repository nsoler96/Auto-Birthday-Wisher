import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()

#Query The Database
c.execute("SELECT * FROM contacts")

print (c.fetchall())

print("Command executed successfully")
# Commit our command
conn.commit()

#Close our connection
conn.close()