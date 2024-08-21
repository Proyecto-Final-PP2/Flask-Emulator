from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Datos de usuarios (simulación sin base de datos)
users = {
    'user1': {
        'username': 'user1',
        'email': 'user1@example.com',
        'password': generate_password_hash('password1')  # Ejemplo de hash de contraseña
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
            'password': generate_password_hash(password)  # Ejemplo de hash de contraseña
        }
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
        
        # Aquí deberías registrar esta acción en tu base de datos
        # Ejemplo básico de impresión para propósitos de demostración
        print(f"Registro en la base de datos: Emulador {emulator} - Acción {action}")
        
        # Aquí podrías retornar una respuesta JSON, si fuera necesario
        return jsonify({'message': f'Emulador {emulator} {action} registrado correctamente'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
