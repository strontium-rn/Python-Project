import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#email credentials
sender_email = "xyz@gmail.com"
sender_password = "wbqk dgxb vflr tcvb"

#email details
subejct = "Class Jersey Payment Reminder"
body = """Hi everyone,

This is a friendly reminder about the payment for our class jerseys!

We understand that some of you have filled out the order form but haven't yet submitted the payment. The jerseys have already been printed, and the shop will be requesting the total amount in the next day or two.

To ensure you receive your jersey on time, we kindly ask you to transfer the payment of ₹1300 as soon as possible.

Here are the payment details:
Esewa Account: 1234567890

Please include your name in the reference section when making the transfer. This will help us track the payments efficiently.

If you've already submitted your payment, please disregard this email.  Thank you!

For any questions or concerns, feel free to reply to this email.

Looking forward to seeing everyone in our class jerseys!


Regards


"""
recipients = ["example@gmail.com", "example@gmail.com", "example@gmail.com"]

def send_email(sender_email, sender_password, recipients, subject, body):
    #set up the smtp server
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    for recipient in recipients:
        #create the email
        msg = MIMEMultipart()
        msg['Form'] = sender_email
        msg['To'] = recipient
        msg['Subject'] = subejct
        msg.attach(MIMEText(body, 'plain'))

        #send the email
        smtp_server.send_message(msg)
        print(f"Email sent to {recipient}")

    smtp_server.quit()

send_email(sender_email, sender_password, recipients, subejct, body)