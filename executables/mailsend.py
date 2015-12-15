from boto.ses import SESConnection
import os


def sendmail(name, comment):
    source = "patte.wilhelm@googlemail.com"
    subject = "Kommentar eingegangen"
    body = 'Es wurde ein neues Wetter bewertet. Von: ' + name + ': ' + comment
    to_addresses = ["patte.wilhelm@googlemail.com"]
    connection = SESConnection(aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
                               aws_secret_access_key=os.environ['AWS_SECRET_KEY'])
    connection.send_email(source, subject, body, to_addresses)