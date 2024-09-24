import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()

#Query The Database
c.execute("SELECT * FROM contacts WHERE last_name LIKE 'S%' ")

items = c.fetchall()

for item in items:
	print(item)



print ("                    ")
print("Command executed successfully")
# Commit our command
conn.commit()

#Close our connection
conn.close()