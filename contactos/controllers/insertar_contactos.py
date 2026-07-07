import web
render = web.template.render('views', base='layout')
class insertar_contactos:
    def GET(self):
        return render.insertar_contactos()
    def POST(self):
        raise web.seeother('/lista_contactos')