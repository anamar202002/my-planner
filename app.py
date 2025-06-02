from flask import Flask
from modelos.modelos import db
from vistas import *
from flask_restful import Api
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(vistas.VistaCategoria, '/categoria', endpoint = 'crear')
api.add_resource(vistas.VistaCategoria, '/categoria/<int:id_categoria>', endpoint = 'editar&borrar')
api.add_resource(vistas.VistaSubcategoria,'/categoria/<int:id_categoria>/subcategoria', endpoint = 'crearSubcategoria')
api.add_resource(vistas.VistaSubcategoria,'/subcategoria/<int:id_subcategoria>', endpoint = 'editar&borrarSubcategoria')

""" @app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
 """