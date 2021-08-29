import smtplib

gmail_user = 'your_email@gmail.com'
gmail_password = 'your_password'

sent_from = gmail_user
to = ['person_a@gmail.com']
subject = 'REGARDING BLOOD DONATION NOTIFICATION'
body = "DEAR DONORS \tTHIS IS A HUMBLE REQUEST FROM XYZ BLOOD BANK THAT PERSON WITH BLOOD GROUP 'X' PLEASE RESPOND AS SOON AS POSSIBLE AS WE ARE IN A URGENT REQUIERMENT\tFOR MORE DETAILS REPLY TO THE SAME MAIL\tTHANK YOU"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)