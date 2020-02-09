import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

PASSWORD = "bbbqgfvkvpavrrwb" # This is the gmail App Password
OUR_MAIL = "trespassing.detection@gmail.com"
SUBJECT = "Trespasser Detected!"
MESSAGE = ("Hi!\n\nA trespasser has been detected in your area. "
    "You can find an image with the tresspasser in the attachments!"
    "\n\nStay safe,\nTresspassing Detection Team")


def send_mail(send_to, file):
    port = 465  # For SSL
    
    # Create a secure SSL context
    context = smtplib.ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        # Log in with the App Password
        server.ehlo() 
        server.login(OUR_MAIL, PASSWORD)

        msg = MIMEMultipart()
        msg['From'] = OUR_MAIL
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = SUBJECT

        msg.attach(MIMEText(MESSAGE))

        with open(file, "rb") as f:
            part = MIMEApplication(
                f.read(),
                Name=basename(file)
            )
            print("File " + file + " read successfully")

        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
        msg.attach(part)

        print("Sending mail...")
        server.sendmail(OUR_MAIL, send_to, msg.as_string())
        server.close()
        print("Mail sent successfully")

def main():
    send_mail("n.lilla96@gmail.com", "trespassers.png")

if __name__== "__main__":
    main()