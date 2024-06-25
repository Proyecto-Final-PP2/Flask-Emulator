from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Datos de usuarios (simulación sin base de datos)
users = {
    'user1': {
        'username': 'user1',
        'password': generate_password_hash('password1')  # Ejemplo de hash de contraseña
    }
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists')
        else:
            users[username] = {
                'username': username,
                'password': generate_password_hash(password)  # Ejemplo de hash de contraseña
            }
            flash('Registration successful. Please login.')
            return redirect(url_for('login'))
    return render_template('register.html')

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
