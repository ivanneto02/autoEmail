import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

port = 587  # For starttls
# Account information - Email information
smtp_server = "smtp.gmail.com"
sender_email = "ivanneto0101@gmail.com"
receiver_email = "ineto001@ucr.edu"
password = input("Type your password and press enter:")

def send_email(receiver):
    # Read file, set content
    with open("emailmessage.txt") as textmessage:
        message_content = textmessage.read()

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Undergraduate Research"

    # Message content
    message.attach(MIMEText(message_content, 'plain'))

    # Attachment information
    attachment_name = "MyResume.pdf"
    attachment_file = open(attachment_name, 'rb') # Open the file as binary mode

    # Payload
    payload = MIMEBase('application', 'pdf')
    payload.set_payload(attachment_file.read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=attachment_name)

    # Attach message
    message.attach(payload)

    # SMTP session
    try:
        session = smtplib.SMTP(smtp_server, 587)
        session.starttls()
        session.login(sender_email, password)
        text = message.as_string()
        session.sendmail(sender_email, receiver, text)
        session.quit()
        print("Email sent to \'" + receiver + "\'")
    except Exception as e:
        print("Email NOT sent: " + e)

def iterate_emails():
    with open('email_list.txt') as el:
        for x in el:
            send_email(x.strip())

if __name__ == "__main__":
    iterate_emails()