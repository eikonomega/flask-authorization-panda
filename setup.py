"""
Flask-Authorization-Panda
-------------

Flask Authorization for Pandas!

Provides decorators for Flask view methods that implement various
authentication schemes.

"""
from setuptools import setup


setup(
    name='Flask-Authorization-Panda',
    version='0.2',
    url='https://github.com/eikonomega/flask-authorization-panda',
    license='MIT',
    author='Mike Dunn',
    author_email='mike@eikonomega.com',
    description='Flask Authorization for Pandas!',
    long_description=__doc__,
    packages=['flask_authorization_panda'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'PyTest'
        'pytest-cov'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)