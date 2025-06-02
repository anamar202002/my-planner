from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from modelos import *
categoria_schama = CategoriaSchema(many=True)
subcategoria_schama = SubcategoriaSchema(many=True)
tarea_schama = TareaSchema(many=True)
subtarea_schama = SubcategoriaSchema(many=True)

class VistaCategoria (Resource):
    def post(self):
        nueva_categoria = Categoria(nombre=request.json["Nombre"])
        db.session.add(nueva_categoria)
        db.session.commit()
        return categoria_schama.dump(nueva_categoria)
    
    def put(self, id_categoria):
        categoria = db.get_or_404(Categoria, id_categoria)
        categoria.nombre = request.json.get("Nombre", categoria.nombre)
        db.session.commit()
        return categoria_schama.dump(categoria)
    
    def delete (self, id_categoria):
        categoria = db.get_or_404(Categoria, id_categoria)
        db.session.delete(categoria)
        db.session.commit()
        return '', 204
    
    def get (self):
        categorias=db.session.query(Categoria).all()
        print(categorias)
        return categoria_schama.dump(categorias)

class VistaSubcategoria (Resource):
    def post(self, id_categoria):
        nueva_subcategoria = Subcategoria(nombre=request.json["Nombre"], id_categoria=id_categoria)
        db.session.add(nueva_subcategoria)
        db.session.commit()
        return categoria_schama.dump(nueva_subcategoria)
