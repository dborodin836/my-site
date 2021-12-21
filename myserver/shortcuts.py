import jinja2
from setting import STATIC_URL


def render_static(template):
    return jinja2.Template(template.read()).render(static=STATIC_URL)
