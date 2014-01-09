from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('actualize', 'templates'))


def render_template(template_name, vars):
    template = env.get_template(template_name)
    return template.render(**vars)
