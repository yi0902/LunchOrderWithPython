import smtplib

class GmailServer():

    def __init__(self, to_addr, title, body):
        self.gmail_user = "final.project.python.udacity@gmail.com"
        self.gmail_pwd = "finalproject"
        self.addr_from = self.gmail_user
        self.addr_to = [to_addr]
        self.subject = title
        self.text = body

    def send_email(self):
        message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
                  """ % (self.addr_from, ", ".join(self.addr_to),
                         self.subject, self.text)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(self.gmail_user, self.gmail_pwd)
            server.sendmail(self.addr_from, self.addr_to, message)
            server.close()
            return True
        except:
            return False

