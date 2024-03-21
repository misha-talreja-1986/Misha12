import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)  
conn.ehlo()
conn.starttls()
conn.login('misha.talreja22@gmail.com','hbogqvvaroykqezd')
conn.sendmail('misha.talreja22@gmail.com','misha.talreja22@gmail.com','subject:This is subject\n\n This is msg write here...')
conn.quit()

#  587 is the code of gmail.