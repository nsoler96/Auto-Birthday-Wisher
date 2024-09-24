import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()

c.execute("INSERT INTO contacts VALUES ('Elin', 'Moya', '862-318-0388')")


print("Command executed successfully")
# Commit our command
conn.commit()

#Close our connection
conn.close()