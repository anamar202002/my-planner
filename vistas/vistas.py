from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from modelos import *
categoria_schama = CategoriaSchema(many=False)
categorias_schama = CategoriaSchema(many=True)
subcategoria_schama = SubcategoriaSchema(many=False)
subcategorias_schama = SubcategoriaSchema(many=True)
tarea_schama = TareaSchema(many=True)
subtarea_schama = SubcategoriaSchema(many=True)

class VistaCategoria (Resource):
    def post(self):
        nueva_categoria = Categoria(nombre=request.json["nombre"])
        db.session.add(nueva_categoria)
        db.session.commit()
        return categoria_schama.dump(nueva_categoria)
    
    def put(self, id_categoria):
        categoria = db.get_or_404(Categoria, id_categoria)
        categoria.nombre = request.json.get("nombre", categoria.nombre)
        db.session.commit()
        return categoria_schama.dump(categoria)
    
    def delete (self, id_categoria):
        categoria = db.get_or_404(Categoria, id_categoria)
        db.session.delete(categoria)
        db.session.commit()
        return '', 204
    
    def get (self):
        categorias=db.session.query(Categoria).all()
        return categorias_schama.dump(categorias)

class VistaSubcategoria (Resource):
    def post(self, id_categoria):
        nueva_subcategoria = Subcategoria(nombre=request.json["nombre"], id_categoria=id_categoria)
        db.session.add(nueva_subcategoria)
        db.session.commit()
        return subcategoria_schama.dump(nueva_subcategoria)
    
    def put(self, id_subcategoria):
        subcategoria = db.get_or_404(Subcategoria, id_subcategoria)
        subcategoria.nombre = request.json.get("nombre", subcategoria.nombre)
        subcategoria.id_categoria = request.json.get("id_categoria", subcategoria.id_categoria)
        db.session.commit()
        return subcategoria_schama.dump(subcategoria)
    
    def delete (self, id_subcategoria):
        subcategoria = db.get_or_404(Subcategoria, id_subcategoria)
        db.session.delete(subcategoria)
        db.session.commit()
        return '', 204
    
    def get (self,id_categoria):
        subcategorias=db.session.query(Subcategoria).filter_by(id_categoria = id_categoria).all()
        return subcategorias_schama.dump(subcategorias)
    
class VistaTarea (Resource):
    def put(self, id_subcategoria):
        nueva_tarea = Subcategoria(nombre=request.json["nombre"], descripcon=request.json["descripcion"], id_subcategoria=id_subcategoria)
        db.session.add(nueva_tarea)
        db.session.commit()
        return subcategoria_schama.dump(nueva_tarea)

