import smtplib
import datetime
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read the data from the Excel file
df = pd.read_excel("data.xlsx")

# Get today's date
today = datetime.datetime.now().date()

# Lambda function to filter people whose birthday is today
birthday_today = df[df['Birthday'].apply(lambda x: datetime.datetime.strptime(x, "%d-%m-%Y").date() == today)]

# Define the email function (for sending email to each person)
def send_email(to_email, subject, body):
    # Your email credentials
    sender_email = "ns@dryfastmetro.com"
    password = "ffgewduwxzynbbdy"
    
    # Set up the SMTP server (this is for Gmail, adjust if you're using a different provider)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        
        # Compose the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())

# Lambda function to generate the birthday message
generate_email_message = lambda name: f"Happy Birthday, {name}! Wishing you a wonderful day!"

# Loop through each person whose birthday is today and send them an email
for index, row in birthday_today.iterrows():
    name = row['Name']
    email = row['Email']
    subject = "Happy Birthday!"
    message = generate_email_message(name)
    
    # Send the email
    send_email(email, subject, message)
    print(f"Email sent to {name} ({email})")

