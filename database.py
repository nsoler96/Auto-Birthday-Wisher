import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()

many_contacts = [
					('Jenny','Smith','551-555-0124'),
					('Maria', 'Aragon','551-296-8001'),
					('Michael', 'Soriano', '347-818-3092'),
				]

c.executemany("INSERT INTO contacts VALUES (?,?,?)",many_contacts)


print("Command executed successfully")
# Commit our command
conn.commit()

#Close our connection
conn.close()