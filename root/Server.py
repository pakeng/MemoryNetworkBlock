from flask import Flask

from root.manger import Manager

app = Flask('MyTestWebServer')

@app.route('/')
def root():
    return 'hello world!'


@app.route('/register')
def register():
    return 'success'


@app.route(r'/registerNew')
def registerNew():
    return 'registerNew'


def find_node_with_name(name):
    for son in Manager.sons:
        if son.name == name:
            return son


if __name__ == '__main__':
    print(app.name)
    app.run()


