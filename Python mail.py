
import sys
import smtplib
import getpass

server_name = 'smtp.gmail.com'
payload = """From: {}
To: {}
Subject: Hello world!
Guess what? I figured out how to send email via. a python
script and the smptlib library! I'm sending this mail from
my local PC.
The current authentication approach I'm using right now is
pretty insecure though, so I will need to fix that.
Right now, I'm using: https://myaccount.google.com/lesssecureapps
But I'll look into creating a proper Google App: https://console.developers.google.com
"""

# NOTE: After testing using https://myaccount.google.com/lesssecureapps, turn it back off!
# It's a pretty insecure method that's not meant to be used in the long run.
# Create a proper Google app from the developer's console instead.

if __name__ == '__main__':
    if sys.version_info[0] < 3:
        username = str(raw_input("Enter your email address: "))
    else:
        username = str(input("Enter your email address: "))
    
    password = str(getpass.getpass("Enter gmail password for {}: ".format(username)))

    conn = smtplib.SMTP(server_name, 587)
    conn.ehlo()
    conn.starttls()
    conn.login(username, password)
    conn.sendmail(username, [username], payload.format(username, username))
    conn.quit()
    
print('Success!')
