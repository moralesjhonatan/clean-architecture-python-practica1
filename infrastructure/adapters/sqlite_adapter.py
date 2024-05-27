import sqlite3

class SqliteAdapter:
    def __init__(self):
        self.conexion = sqlite3.connect('usuarios.db')
        self.cursor = self.conexion.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT, correo TEXT, contrasena TEXT)')
        self.conexion.commit()

    def guardar(self, usuario):
        self.cursor.execute('INSERT INTO usuarios VALUES (?, ?, ?, ?)',
                            (usuario.id, usuario.nombre, usuario.correoElectronico, usuario. contrasena))
        self.conexion.commit()

    def consultarPorId(self, id):
        self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
