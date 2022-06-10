import os
from email.message import EmailMessage
import smtplib
import imghdr

'''
THE EMAIL MODULE by Jules Okoye-ezeh
'''

#'add' is the environment variable that holds the senders email address, 'pass' is it's corresponding password.
add = os.environ.get('add')
password = os.environ.get('pass')

def basic_email(to,subject,body):
	'''
	This sends basic emails without attachments

	to: the receiver's email address (could be a list)
	subject: the subject of the email 
	body: the body of the email 
	THE VALUES OF ALL ITEMS ABOVE CAN BE ENTERED AS VARIABLES
	'''
	message = EmailMessage()
	message['to']=to
	message.set_content(body)
	message['subject']=subject
	message['from'] = add

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(add,password)
		smtp.send_message(message)

def email_with_images(to,subject,img_dir,body):
	'''
	This sends emails with image attachments
	
	to: the receiver's email address (could be a list)
	subject: the subject of the email
	img_dir: a list the full path directory of the image(s) to be sent 
	body: the body of the email 
	THE VALUES OF ALL ITEMS ABOVE CAN BE ENTERED AS VARIABLES
	'''
	message = EmailMessage()
	message['to']=to
	message.set_content(body)
	message['subject']=subject
	message['from'] = add
	for x in img_dir:
		with open(x,'rb') as pic:
			pic_data = pic.read()
			pic_type = imghdr.what(pic.name)
			pic_name = pic.name
		message.add_attachment(pic_data,maintype='image',subtype=pic_type,filename=pic_name)

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(add,password)
		smtp.send_message(message)



def email_with_files(to,subject,file_dir,body):
	'''
	This sends emails with file attachments
	
	to: the receiver's email address (could be a list)
	subject: the subject of the email
	file_dir: a list of the full path directory of the file(s) to be sent 
	body: the body of the email 
	THE VALUES OF ALL ITEMS ABOVE CAN BE ENTERED AS VARIABLES
	'''
	message = EmailMessage()
	message['to']=to
	message.set_content(body)
	message['subject']=subject
	message['from'] = add
	for x in img_dir:
		with open(x,'rb') as books:
			book = books.read()
		message.add_attachment(book,maintype='application',subtype='octet-stream',filename=books.name)

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(add,password)
		smtp.send_message(message)


def email_with_html(to,subject,html_file,body):
	'''
	This sends emails with html
	to: the receiver's email address (could be a list)
	subject: the subject of the email 
	html_file: the html document to be sent. Should be a string
	body: the body of the email 
	THE VALUES OF ALL ITEMS ABOVE CAN BE ENTERED AS VARIABLES

	'''
	message = EmailMessage()
	message['to']=to
	message.set_content(body)
	message['subject']=subject
	message['from'] = add
	message.add_alternative(html_file,subtype='html')

	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(add,password)
		smtp.send_message(message)
