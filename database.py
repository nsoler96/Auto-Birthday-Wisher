import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()

#Create a Table
c.execute("""CREATE TABLE contacts (	
	first_name text,
	last_name text,
	phone_number text 
	)""")

print("Command executed successully...")

# Commit our command
conn.commit()

#Close our connection
conn.close()