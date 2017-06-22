import setuptools


setuptools.setup(
    name='sprockets-redoc-example',
    version='0.0.1',
    packages=['sprockets_redoc_example'],
    install_requires=['sprockets_redoc'],
    package_data={'sprockets_redoc_example': ['data/*']}
)
