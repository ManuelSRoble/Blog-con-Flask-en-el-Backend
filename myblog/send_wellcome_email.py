from flask import render_template
from flask_mail import Mail, Message

# from config_para_email import configDelMail
from myblog.config_para_email import configDelMail

from myblog import app

# app = Flask(__name__)
configDelMail(app)
mail = Mail(app)

# @app.route('/')
# def index():
#     return 'enviar email pagaina home / /send_email/<email>'

# @app.route('/send_email/<email>', methods=['GET'])
def send_email(email):
    msg_title = 'Bienvenido'
    sender = 'noreply@app.com'
    msg = Message(msg_title, sender=sender, recipients=[email])
    msg_body = 'Bienvenido al blog'
    msg.body = "hola 123"
    data = {
        'app_name': 'News Blog',
        'title': msg_title,
        'body': msg_body,
    }
  
    msg.html = render_template('email.html', data=data)
  
    try:
        mail.send(msg)
        return "Email sent..."
    except Exception as e:
        print(e)
        return f'The email was not sent: {e}'

# if __name__ == '__main__':
#     app.run(debug=True)