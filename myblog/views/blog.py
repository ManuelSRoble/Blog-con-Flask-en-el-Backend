from flask import(
  render_template, Blueprint, flash, g, redirect, request, url_for
)

from werkzeug.exceptions import abort

from myblog.models.post import Post
from myblog.models.user import User

from myblog.views.auth import login_required

from myblog import db

blog = Blueprint('blog', __name__)

#obtener un usuario
def get_user(id):
  user = User.query.get_or_404(id)
  return user

#listar las publicaciones
@blog.route('/')
def index():
  posts = Post.query.all() #recuperar todos los posts
  db.session.commit()
  return render_template('blog/index.html', posts = posts, get_user = get_user)

#registrar o crear un posts
@blog.route('/blog/create', methods=['GET','POST'])
@login_required
def create():
  if request.method == 'POST':
    title = request.form.get('title')
    body = request.form.get('body')
    
    #creo un objeto de tipo post
    post = Post(g.user.id, title, body)
    
    error = None
    if not title:
      error = 'Se requiere un titulo'
    
    if error is not None:
      flash(error)
    else:
      db.session.add(post)
      db.session.commit()
      return redirect(url_for('blog.index'))
    
    flash(error)
    
  return render_template('blog/create.html')
  
#obtener post
def get_post(id, check_author=True): #asigno de forma predeterminada True a check_author
  post = Post.query.get(id)
   
  if post is None: #si la publicacion no existe
    abort(404, f"Id {id} de la publicación no existe")
    
  if check_author and post.author != g.user.id:
    abort(404)
    
  return post

#Actualizar un post
@blog.route('/blog/update/<int:id>', methods=('POST','GET'))
@login_required #debe estar logeado para actualizar un post
def update(id):
  post = get_post(id)
  
  if request.method == 'POST':
    #actualizar titulo y contenido
    post.title = request.form.get('title')
    post.body = request.form.get('body')
    
    #manejar errores
    error = None
    if not post.title:
      error = 'Se requiere un título'
    
    if error is not None:
      flash(error)
    else:
      db.session.add(post)
      db.session.commit()
      return redirect(url_for('blog.index'))
    
    flash(error)
  
  return render_template('blog/update.html', post = post)

#eliminar una publicacion
@blog.route('/blog/delete/<int:id>')
@login_required
def delete(id):
  post = get_post(id)
  db.session.delete(post)
  db.session.commit()
  
  return redirect(url_for('blog.index'))