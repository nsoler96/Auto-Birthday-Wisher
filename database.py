import sqlite3

#Connect to database
conn=sqlite3.connect('contact_manager.db')

#Create a cursor
c = conn.cursor()

#Query The Database
c.execute("SELECT * FROM contacts")



items = c.fetchall()

print("NAME " + "\t\tPHONE NUMBER")
print("----------" + "\t-----------")
for item in items:
	print(item[0] + " " + item[1] + "\t" + item[2])


print ("                    ")
print("Command executed successfully")
# Commit our command
conn.commit()

#Close our connection
conn.close()