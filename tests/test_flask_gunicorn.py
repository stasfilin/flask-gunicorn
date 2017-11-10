import sys

from flask import Flask

sys.path.append('..')

from flask_gunicorn import *


def test_server_port():
    assert server_port() == '5000'

    os.environ['PORT'] = '1111'

    assert server_port() != '5000'
    assert server_port() == '1111'


def test_server_bind_address():
    assert server_bind_address() == '127.0.0.1'

    os.environ['HTTP_HOST'] = '127.0.0.2'

    assert server_bind_address() != '127.0.0.1'
    assert server_bind_address() == '127.0.0.2'


def test_number_of_workers():
    os.environ['WEB_CONCURRENCY'] = '9'

    assert number_of_workers() == '9'


def test_GunicornStandalone():
    app = Flask(__name__)
    gunicorn_app = GunicornStandalone(app)

    assert gunicorn_app.application is app
