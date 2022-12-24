from setuptools import setup

setup(
    name='testApi',
    version='0.0.0.1',
    author='Stepan.F',
    author_email='f.stepa.n@yandex.ru',
    description='FastApi app',
    install_requires=[
        'fastapi==0.78.0',
        'uvicorn==0.18.2',
        'SQLAlchemy==1.4.45',
        'pytest==7.2.0',
        'requests==2.27.1'
    ],
    scripts=['app/main.py', 'scripts/create_db.py']
)