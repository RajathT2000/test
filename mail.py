import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

def get_environment():
    if 'DYNO' in os.environ:
        return 'Heroku'
    else:
        return 'Local'

sender_email = "testpersonal81@gmail.com"
app_password = "mragzfcuyhnnqgup"
receiver_email = "rajathttt@gmail.com"


def send_email(subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)

        email_body = f"Subject: {subject}\n\n{message}\n\nThis message is from {get_environment()}"
        server.sendmail(sender_email, receiver_email, email_body)

        print("Email notification sent!")
    except Exception as e:
        print("Error sending email:", str(e))
    finally:
        server.quit()


# now = datetime.now()
# message = "Hi, \n This email has been sent just for a verification process. Kindly ignore the message.\nEmail triggered at " + \
#     str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

# send_email("Email Verification", message)
