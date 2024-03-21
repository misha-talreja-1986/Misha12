import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login('chikujoshi1998@gmail.com','gkxpkweegsrcotrh')
conn.sendmail('chikujoshi1998@gmail.com','chikujoshi1998@gmail.com','Subject:This is subject\n\n This is msg write here...')
conn.quit()