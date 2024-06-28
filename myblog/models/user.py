from myblog import db
#crear una tabla llamada 'users' con columnas llamadas id, username y password
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50))
  password = db.Column(db.Text)
  email = db.Column(db.String(255), nullable=False)
  
  #constructor
  def __init__(self, username, password, email) -> None:
    self.username = username
    self.password = password
    self.email = email
    
  #representar como se va a mostrar este objeto
  def __repr__(self) -> str:
    return f'User: {self.username}'