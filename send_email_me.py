import smtplib, ssl


def send_email_me(message):
	host = "smtp.gmail.com"
	port = 465
	username = 'koynarecam@gmail.com'
	password = "bhmh atbl pmkh scug"
	receiver = "fragmantica.django@gmail.com"
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)