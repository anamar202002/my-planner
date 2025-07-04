from flask_sqlalchemy import SQLAlchemy
import enum
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class EnumImportancia(enum.Enum):
    BAJA = "Baja"
    MEDIA = "Media"
    ALTA = "Alta"
    CRITICA = "Crítica"

class EnumProgreso (enum.Enum):
    NO_INICIADA = "No Iniciada"
    EN_PROGRESO = "En Progreso"
    COMPLETADA = "Completada"

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
    id_subcategoria = db.Column(db.Integer, db.ForeignKey('subcategoria.id'))
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(550))
    fecha = db.Column(db.DateTime(timezone=True))
    importancia = db.Column(db.Enum(EnumImportancia), nullable=False)
    progreso = db.Column(db.Enum(EnumProgreso), nullable=False)


class Subtarea (db.Model):
    __tablename__='subtarea'

    id = db.Column(db.Integer, primary_key = True)
    id_tarea = db.Column(db.Integer, db.ForeignKey('tarea.id'))
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(550))
    fecha = db.Column(db.DateTime(timezone=True))

class CategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Categoria
        include_relationships =True
        include_fk = True
        load_instance = True
    nombre = fields.String()

class SubcategoriaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subcategoria
        include_relationships =True
        include_fk = True
        load_instance = True
    nombre = fields.String()

class TareaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        include_relationships =True
        include_fk = True
        load_instance = True
    nombre = fields.String()

class SubtareaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Subtarea
        include_relationships =True
        include_fk = True
        load_instance = True
    nombre = fields.String()