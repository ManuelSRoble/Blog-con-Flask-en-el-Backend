def configDelMail(app):
  app.config['SECRET_KEY'] = "this1sThemosdsecretkey_ever"
  app.config['MAIL_SERVER'] = "smtp.gmail.com"
  app.config['MAIL_PORT'] = 587
  app.config['MAIL_USE_TLS'] = True
  app.config['MAIL_USERNAME'] = "manuel.trabajo.programador@gmail.com"
  app.config['MAIL_PASSWORD'] = "hnlnfxhgayodrinb"
  app.config['MAIL_DEFAULT_SENDER'] = "roblecito2023@gmail.com"