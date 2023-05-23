from bottle import route, run

@route('/')
def hello_world():
    return  'Hello World!'


run(host='172.20.10.3',post=80)
