from . import db
from werkzeug.security import generate_password_hash

class User(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `users` (plural) or some other name.
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)

    def __init__(self, fname, lname, email, password, weight, height):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.weight = weight
        self.height = height

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.uid)  # python 2 support
        except NameError:
            return str(self.uid)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.first_name)

class Recipe(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `users` (plural) or some other name.
    __tablename__ = 'recipes'

    rid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(511))
    instruction = db.Column(db.String(511))
    ingredients = db.Column(db.String(255))

    def __init__(self, name, instruction, ingredients):
        self.name = name
        self.instruction = instruction
        self.ingredients = ingredients

    def get_id(self):
        try:
            return unicode(self.uid)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.name)