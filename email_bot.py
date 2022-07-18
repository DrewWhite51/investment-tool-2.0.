import smtplib, ssl

# Username and password for stockbot email
gmail_user = 'stockbot51@gmail.com'
gmail_password = '5Y4jAtqrJNtxTXL'

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = gmail_user  # Enter your address
receiver_email = gmail_user  # Enter receiver address
password = 'rxhqdzmigobsahcn'

message = """\
Subject: Hi there
This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

