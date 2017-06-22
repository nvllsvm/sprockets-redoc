from tornado import web

import sprockets_redoc

app = web.Application()
sprockets_redoc.install(app)
