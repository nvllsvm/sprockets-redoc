import os
import pkgutil

from tornado import web


__version__ = '0.1.0'
DEFAULT_TITLE = 'Documentation - {}'


class IndexHandler(web.RequestHandler):
    """Handles rendering of index.html"""

    template = 'index.html'

    def initialize(self, title, path, swagger_filename):
        self.title = title
        self.template_path = path
        self.swagger_filename = swagger_filename

    def get_template_path(self):
        return self.template_path

    def get(self):
        self.render(
            self.template,
            paths={'swagger': '/{}'.format(self.swagger_filename),
                   'redoc': '/redoc/redoc.min.js'},
            title=self.title,
            settings=self.settings)


class SwaggerHandler(web.RequestHandler):
    """Handles rendering of swagger.yaml"""

    def initialize(self, path, swagger_filename):
        self.swagger_path = path
        self.swagger_filename = swagger_filename

        self.content_type = None
        if swagger_filename.lower().endswith(('.yaml', '.yml')):
            self.content_type = 'text/yaml'
        elif swagger_filename.lower().endswith('.json'):
            self.content_type = 'application/json'

    def get_template_path(self):
        return self.swagger_path

    def get(self, *args, **kwargs):
        if self.content_type:
            self.set_header('Content-Type', self.content_type)
        self.render(
            self.swagger_filename, host=self.request.host,
            scheme=self.request.protocol, settings=self.settings)


def install(application, module_name, swagger_path, title=None):
    """Add the ReDoc endpoints to a Tornado application

    :param str application: The Tornado application.
    :param swagger_path: Local path to the Swagger file
    """

    static_path = os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'data')

    module_path = os.path.dirname(pkgutil.get_loader(module_name).path)
    full_path = os.path.join(module_path, swagger_path)

    swagger_dir = os.path.dirname(full_path)
    swagger_filename = os.path.basename(full_path)

    if title is None:
        title = DEFAULT_TITLE.format(module_name)

    application.add_handlers(r'.*', [
        ('/', IndexHandler, {'title': title,
                             'path': static_path,
                             'swagger_filename': swagger_filename}),
        (r'/({})'.format(swagger_filename), SwaggerHandler,
         {'path': swagger_dir, 'swagger_filename': swagger_filename}),
        (r'/redoc/(.*)', web.StaticFileHandler, {'path': static_path})
    ])
