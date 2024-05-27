from domain.entities.user import User

class CrearUsuario:
    def __init__(self, adapter):
        self.adapter = adapter

    def ejecutar(self, id, nombre, correoElectronico, contrasena):
        usuario = User(id, nombre, correoElectronico, contrasena)
        self.adapter.guardar(usuario)
        return usuario