import web
import sqlite3

render = web.template.render('views', base='layout')

class BorrarContacto:

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
            print(f"ERROR 300: {error.args}")
            return None
        except Exception as error:
            print(f"ERROR 301: {error.args}")
            return None

    def GET(self, id_contacto):
        contacto = self.obtenerContacto(id_contacto)
        if contacto:
            return render.borrar_contacto(contacto)
        else:
            return "Contacto no encontrado"

    def POST(self, id_contacto):
        # Aquí iría la lógica para eliminar el contacto
        pass