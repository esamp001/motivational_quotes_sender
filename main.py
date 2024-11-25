import smtplib
import datetime as dt
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import pytz

num_min = 60
time_zone = pytz.timezone("Asia/Manila")

smtp_server = "smtp.gmail.com"
smtp_port = 587
my_email = "sampagaellejun.dev@gmail.com"
my_password = "mble fntc ttyl cvlw"
receiver_email = "arielajanetaraneta.bolanos@bicol-u.edu.ph"

with open("quotes.txt", "r") as file:
        quotes = file.readlines()
        get_quotes = random.choice(quotes)

current_time_in_timezone = datetime.now(time_zone)

def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Daily Quotes'

        body = f"Here's your motivational quotes for today:\n\n {get_quotes}"
        msg.attach(MIMEText(body, 'plain'))

        connection = smtplib.SMTP(smtp_server, smtp_port, timeout=30)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(my_email, receiver_email, msg.as_string())
        connection.close()
    except Exception as error:
        print(f"Failed to send an email: {error}")

    else:
        print("Email sent successfully!")

def schedule_sent():
    current_time = datetime.now(time_zone)
    for i in range(num_min):
        current_time + timedelta(minutes=i)
        send_email()
        time.sleep(60)

        time.sleep(1)
schedule_sent()





# today = datetime.today()
# specific_time = today.replace(hour=18, minute=40, second=0, microsecond=0)
#
# now = dt.datetime.now()
#
# for i in range(7):
#     day = today + timedelta(days=i)
#     scheduled_time = today.replace(hour=18, minute=40, second=0, microsecond=0)
#
#     while datetime.now() < scheduled_time:
#         time.sleep(1)
#
#
#
#
#
#
#     password = "laoz urtu npgl zutd"
#
#
#
#
#     try:
#
#
#     except Exception as error:
#         print(f"Error sending email for {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')}: {error}")
#
#     else:
#         print("Sending an email everyday will start now!")


