sprockets-redoc
===============

Easily integrate `ReDoc`_-powered documetation into your Tornado application.

Setup
-----

The Tornado application needs to have the template path set to the location of
the ``swagger.yaml`` file. ``sprockets-redoc`` will automatically set this up
based on the ``TEMPLATE_PATH`` environment variable.

Invoke ``sprockets_redoc.install`` on your application to expose the endpoints.

.. code:: python

    import sprockets_redoc
    import tornado.web

    app = tornado.web.Application()
    sprockets_redoc.install(app)


Endpoints
---------

``sprockets-redoc`` exposes the following paths in your application.

+-------------------+-----------------------------+
| Path              | Description                 |
+===================+=============================+
| ``/``             | Redoc-powered Documentation |
+-------------------+-----------------------------+
| ``/swagger.yaml`` | The Swagger file template   |
+-------------------+-----------------------------+
| ``/redoc/(.*)``   | Static files used by ReDoc  |
+-------------------+-----------------------------+


.. _Redoc : https://github.com/Rebilly/ReDoc
