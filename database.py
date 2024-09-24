import sqlite3

# Query The DB and Return All Records
def show_all():
	#Connect to database 
	conn=sqlite3.connect('contact_manager.db')
	#Create a cursor
	c = conn.cursor()

	# Query The Database
	c.execute ("SELECT rowid, * FROM contacts")
	items = c.fetchall()

	for item in items:
		print(item)

	# Commit our command
	conn.commit()

	#Close our connection
	conn.close()

#Add A New Record to the table
def add_one(first_name, last_name, phone_number):
	conn = sqlite3.connect('contact_manager.db')
	c = conn.cursor()
	c=conn.cursor()
	c.execute("INSERT INTO contacts VALUES (?,?,?)", (first_name, last_name, phone_number))
	conn.commit()
	conn.close()