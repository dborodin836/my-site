from myserver.shortcuts import render_static


def index():
    with open('templates/index.html') as template:
        return render_static(template)


def not_found():
    with open('templates/not_found.html') as template:
        return render_static(template)


def not_allowed():
    with open('templates/index.html') as template:
        return render_static(template)
