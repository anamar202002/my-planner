from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from modelos import *
categoria = CategoriaSchema()
subcategoria = SubcategoriaSchema()
tarea = TareaSchema()
subtarea = SubcategoriaSchema()

class VistaCategoria (Resource):
    def post(self):
        nueva_categoria = Categoria(nombre=request.json["Nombre"])
        db.session.add(nueva_categoria)
        db.session.commit()
        return {"mensaje":"categoria creada exitosamente"}

