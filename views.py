from myserver import *
from setting import STATIC_URL


def index():
    with open('templates/index.html') as template:
        return jinja2.Template(template.read()).render(static=f'{STATIC_URL}')


def not_found():
    with open('templates/not_found.html') as template:
        return jinja2.Template(template.read()).render(static=f'{STATIC_URL}')


def not_allowed():
    with open('templates/index.html') as template:
        return jinja2.Template(template.read()).render(static=f'{STATIC_URL}')
