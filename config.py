class Config():
  DEBUG = True
  TESTING = True
  
  #Configuracion de base de datos
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/blog_db"
  
class ProductionConfig(Config):
  DEBUG = False
  
class DevelopmentConfig(Config):
  SECRET_KEY = 'dev'
  DEBUG = True
  TESTING = True