import os
from flask import Flask, render_template, render_template_string, redirect, url_for, request, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuración de Flask-Mail con SendGrid
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'apikey'  # Esto sigue siendo 'apikey'
app.config['MAIL_PASSWORD'] = os.getenv('SENDGRID_API_KEY')  # Cargar la API key desde una variable de entorno
app.config['MAIL_DEFAULT_SENDER'] = ('EmuladordeJuegos', 'emuladorflask@gmail.com')

mail = Mail(app)

# Datos de usuarios (simulación sin base de datos)
users = {
    'user1': {
        'username': 'user1',
        'email': 'user1@example.com',
        'password': generate_password_hash('password1')
    }
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Iterar sobre los usuarios para verificar el email y la contraseña
        for user_data in users.values():
            if user_data.get('email') == email and check_password_hash(user_data['password'], password):
                session['username'] = user_data['username']
                return redirect(url_for('index'))
        
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if username in users:
        flash('Username already exists')
    else:
        users[username] = {
            'username': username,
            'email': email,
            'password': generate_password_hash(password)
        }
        
        # Enviar correo de bienvenida
        send_welcome_email(email, username)

        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/index')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

# Ruta para manejar la acción de inicio o cierre de emuladores
@app.route('/emulator-action', methods=['POST'])
def emulator_action():
    if request.method == 'POST':
        data = request.get_json()
        emulator = data.get('emulator')
        action = data.get('action')
        
        print(f"Registro en la base de datos: Emulador {emulator} - Acción {action}")
        return jsonify({'message': f'Emulador {emulator} {action} registrado correctamente'})

# Función para enviar el correo de bienvenida
def send_welcome_email(to_email, username):
    msg = Message('Bienvenido a los mejores Emuladores de Juegos', recipients=[to_email])
    
    # Usar el cid (Content-ID) para referenciar la imagen en el HTML
    msg.html = render_template_string("""
    <html>
        <body>
            <h1>Hola {{ username }},</h1>
            <p>Gracias por registrarte en nuestra plataforma de juegos! Estamos emocionados de que te unas a nosotros.</p>
            <p>Para disfrutar de los mejores juegos, por favor inicia sesión con tus datos.</p>
        </body>
    </html>
    """, username=username)
    
    with app.open_resource('static/icons/favicon.ico') as logo_file:
        msg.attach('favicon.ico', 'image/x-icon', logo_file.read(), 'inline')

    
    msg.charset = 'utf-8'
    mail.send(msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)