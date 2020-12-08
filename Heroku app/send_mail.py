import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '1d8c8f2b390249'
    password = '2d3153e1db79a5'
    message = f"<h3>New Feedbask Submission</h3><ul><li>Customer: {customer}</li><li>Customer: {dealer}</li><li>Customer: {rating}</li><li>Customer: {comments}</li></ul>"
    sender_email = 'szabolcsisti@gmail.com'
    receiver_email = 'szabolcsisti@gmail.com'
    msg = MIMEText(message, 'html')
    msg['subject'] = "Lexus Feedback"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())