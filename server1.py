from bottle import route, run


@route('/')
@route('/hello')
def hello_world():
    return  'Hello World!'


@route('/howru')
def howru():
    return 'Hi, How are you?'

@route('/string/<name>')
def hello_world(name):
    return 'Hello %s' % name

@route('/integer/<num:int>')
def hello_world(num):
    return 'Hello number %d' % num


run(host='172.20.10.3',post=80)
