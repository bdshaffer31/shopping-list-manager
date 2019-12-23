import smtplib, ssl
from email.message import EmailMessage
from book_shelf import shelf



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

def book_content_to_string(book):
    email_text = book.name + ': \n'
    for rec in shelf.master_list.get(shelf.master_list.recipes, book.recipes):
        email_text = email_text + '    ' + rec.name + '\n'
        for ing in shelf.master_list.get(shelf.master_list.ingredients, rec.ingredients):
            email_text = email_text + '       - '   + ing.name + '\n'
    return email_text