from flask import Flask, request, jsonify
from domain.usecases.create_user import CrearUsuario
from infrastructure.adapters.sqlite_adapter import SqliteAdapter

app = Flask(__name__)

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    json = request.get_json(force=True)
    crear_usuario = CrearUsuario(SqliteAdapter())
    usuario = crear_usuario.ejecutar(json['id'], json['nombre'], json['correoElectronico'], json['contrasena'])
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'correoElectronico': usuario.correoElectronico}), 201