from flask import Flask, request, render_template
# import mysql.connector
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__, static_folder='static')

# conn = mysql.connector.connect(
#   host="localhost",
#   port="3306",
#   user="root",
#   password="Vikram@1029",
#   database="contactform"
# )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    message = ''
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
    # conn.commit()

    if request.form.get("send_response") == "yes":
        msg = MIMEText("Thank you for contacting us. We will get back to you soon.")
        msg['Subject'] = 'Contact Form Submission'
        msg['From'] = 'socialconnect23@gmail.com'
        msg['To'] = email
        recipients = [email, "ocialconnect23@gmail.com"]
        # create an instance of the SMTP class
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # start the TLS encryption
        server.starttls()

        # login to the server using your email and password
        server.login("socialconnect23@gmail.com", "aewfewssqbnhtdui")

        # send the email to the recipient
        server.sendmail('socialconnect23@gmail.com', recipients, msg.as_string())
        server.quit()
        message = 'Your message has been sent successfully!'

        return render_template('index.html', message=message)
    else:
        message = 'Your message has been sent successfully!'
        return render_template('index.html', message=message)
    
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1029)
