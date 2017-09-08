from distutils.core import setup
from postdown import __version__, __author__

setup(
    name='Postdown',
    version=__version__,
    author=__author__,
    author_email='sun.qd.china@outlook.com',
    packages=['postdown'],
    package_data={
        'postdown': ['README.rst', 'LICENSE']
    },
    scripts=['bin/postdown'],
    url='https://github.com/TitorX/Postdown',
    description='Generate markdown API document from Postman.',
    long_description=open('README.rst').read(),
)
