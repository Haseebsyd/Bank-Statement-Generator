import smtplib
from email.message import EmailMessage
import os

def send_email_with_attachment(receiver_email, pdf_path, subject="Bank Statement", first_name="", last_name="", user_email=""):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Gmail uses port 587 for TLS
    smtp_username = 'fakeuser5940@gmail.com'
    app_password = 'hsmz iycn khbt fjyu'

    body = f"Dear {first_name} {last_name},\n\nHere is your requested bank statement. Please find the attached PDF.\n\nRegards,\nYour Bank Name"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = receiver_email
    msg.set_content(body)

    with open(pdf_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(pdf_path)

    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, app_password)
        server.send_message(msg)

    print(f"Email sent to {receiver_email}")

