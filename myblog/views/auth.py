from flask import(
  render_template, Blueprint, flash, g, redirect, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from myblog.models.user import User

from myblog import db

import functools

from myblog.send_wellcome_email import *

#creo un blueprint llamado 'auth', registro una lista llamada 'auth' para acceder a listas y rutas
auth = Blueprint('auth', __name__, url_prefix='/auth')#(lista, nombre de archivo de vista, como comienza la url en este caso comienza con /auth)

#Registrar un usuario
@auth.route('/register', methods=('GET','POST'))
def register():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    
    user = User(username, generate_password_hash(password), email)#crear un objeto; crear la tabla, (username, contrasena encriptada)
    #verificar si hubo un error
    error = None
    if not username: #if username is not empty
      error = 'Se requiere nombre de usuario'
    elif not password:
      error = 'Ser requiere contraseña'
    elif not email:
      error = 'Se debe ingresar un email'
      
    #consulto a la base de datos si ya existe
    user_name = User.query.filter_by(username = username).first()
    if user_name == None: #si no existe lo agrego
      db.session.add(user)
      db.session.commit()
      #envio mail
      send_email(email)
      
      
      return redirect(url_for('auth.login'))
    else: 
      error = f"El usuario {username} ya esta registrado"
      
    flash(error)
    
  return render_template("auth/register.html")

#Iniciar Sesion
@auth.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    
    error = None
    
    user = User.query.filter_by(username = username).first()#consulta sql
    #si no existe
    if user == None:
      error = 'Nombre de usuario incorrecto'
    elif not check_password_hash(user.password, password): #si no coinciden la contra que obtendo de la consula sql con la ingresada
      error = 'Contraña incorrecta'
    
    if error is None:
      session.clear()
      session['user_id'] = user.id
      return redirect(url_for('blog.index'))
    
    flash(error)
  return render_template('auth/login.html')
    
    
#verificar si un usuario esta registrado o no
@auth.before_app_request
def load_logged_in_user():
  user_id = session.get('user_id')
  
  if user_id is None:
    g.user = None
  else:
    g.user = User.query.get_or_404(user_id)
    
@auth.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('blog.index'))

#se requiere logearse para modificar su contenido, y decorar vistas para logearse
def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    if g.user is None: #si es nulo necesita logearse
      return redirect(url_for('auth.login'))  
    return view(**kwargs)
  return wrapped_view    