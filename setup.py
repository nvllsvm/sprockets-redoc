import setuptools

from sprockets_redoc import __version__


setuptools.setup(
    name='sprockets-redoc',
    version=__version__,
    url='https://github.aweber.io/andrewr/sprockets-redoc',
    packages=['sprockets_redoc'],
    install_requires=['tornado'],
    package_data={'sprockets_redoc': ['data/*']}
)
