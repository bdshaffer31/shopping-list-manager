import smtplib, ssl
from email.message import EmailMessage



def send_email(message, receiver_email):
    port = 465  # For SSL
    password = input("Type your password and press enter: ")
    sender_email = "bdshaffer.mailer@gmail.com"

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Shopping List'
    msg['From'] = sender_email
    msg['To'] = receiver_email


    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)
    
    print(' -sent- ')

def shop_dict_to_string(shopping_dict):
    email_text = ''
    for key, value in shopping_dict.items():
            email_text = email_text + key + ': \n'
            for ingr in value:
                email_text = email_text + '    -' + ingr.name + '\n'

    return email_text