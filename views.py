def index():
    with open('templates/index.html') as template:
        return template.read()


def not_found():
    with open('templates/not_found.html') as template:
        return template.read()
