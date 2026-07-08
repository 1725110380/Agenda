import web
import sqlite3

render = web.template.render('views', base='layout')

class EditarContacto:

    def obtenerContacto(self, id_contacto):
        try:
            conn = sqlite3.connect('sql/agenda.db')
            cursor = conn.cursor()
            query = "SELECT * FROM contactos WHERE id_contacto = ?;"
            cursor.execute(query, (id_contacto,))
            row = cursor.fetchone()
            
            if row:
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                conn.close()
                return contacto
            else:
                conn.close()
                return None
        except sqlite3.Error as error:
            print(f"ERROR 200: {error.args}")
            return None
        except Exception as error:
            print(f"ERROR 201: {error.args}")
            return None

    def GET(self, id_contacto):
        contacto = self.obtenerContacto(id_contacto)
        if contacto:
            return render.editar_contacto(contacto)
        else:
            return "Contacto no encontrado"

    def POST(self, id_contacto):
        formulario=web.input()
        contacto = {
        "id_contacto": formulario['id_contacto'],
        "nombre": formulario['nombre'],
        "primer_apellido": formulario['primer_apellido'],
        "segundo_apellido": formulario['segundo_apellido'],
        "email": formulario['email'],
        "telefono": formulario['telefono']
    }
        return contacto
