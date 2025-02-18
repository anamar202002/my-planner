from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categoria (db.Model):
    __tablename__ = 'categoria'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))


class Subcategoria (db.Model):
    __tablename__ = 'subcategoria'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(250))
    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    
class Tarea (db.Model):
    __tablename__='tarea'

    id = db.Column(db.Integer, primary_key = True)