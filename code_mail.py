import smtplib

# Ejemplo de envío de correo desde Python.
# Para que funcione tiene que estar habilitado el acceso para aplicaciones poco seguras de la cuenta que envía. 
# Cuenta de google --> seguridad --> Acceso de aplicaciones poco seguras. 


gmail_user = 'no.pienso.arreglar.tu.pc@gmail.com'
gmail_password = input("password = ") 

sent_from = gmail_user
to = ['no.pienso.arreglar.tu.pc@gmail.com']
subject = 'Hola holita desde Python ! '
body = 'Holi. Buenos dias por la manyana.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email enviado!')
except:
    print ('Algo parece que ha ido mal.... ')