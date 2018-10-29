#First Project for Getting Reminder

def main():
    send_mail()
    
def send_mail():
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login("pranaldongare@gmail.com","Unicorn1@")
    message = 'Subject: Test\n\nTest'
    server.sendmail ('pranaldongare@gmail.com','pranaldongare@gmail.com',message)
    server.quit()
    print ('Mail Sent')
    
if __name__ == '__main__': main()