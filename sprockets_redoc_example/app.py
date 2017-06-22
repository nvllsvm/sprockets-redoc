import sprockets_redoc
import tornado.web
import tornado.ioloop

app = tornado.web.Application(service='example-api', version='1.0.0')
sprockets_redoc.install(app,
                        module_name='sprockets_redoc_example',
                        swagger_path='data/swagger.yaml')

app.listen(8000)
tornado.ioloop.IOLoop().current().start()
