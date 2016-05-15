import os

from jinja2 import Template


def generate_single_template(name):
    tname = '{0}.j2'.format(name)
    template = Template(
        open(
            os.path.normpath(os.path.join(__file__, '..', 'templates', tname)),
            'r'
        ).read()
    )
    context = {}
    return template.render(context)
