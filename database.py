import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()


# Update Records

c.execute("""UPDATE contacts SET first_name = 'Linnette' 
			WHERE rowid = 1
	""")

conn.commit()


# Query The Database
c.execute ("SELECT rowid, * FROM contacts")

items = c.fetchall()

for item in items:
	print(item)



print ("                    ")
print("Command executed successfully")
# Commit our command
conn.commit()

#Close our connection
conn.close()