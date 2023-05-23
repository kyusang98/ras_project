from bottle import route, run, request, post

@route('/')
@route('/login')
def login():
    return '''
       <form action='/login' method='post'>
            Username: <input name='username' type='text' />
            Password: <input name='password'
                       type='password' / >
            <input value='Login' type='submit' />
       </form>
           '''
def check_login(username, password):
    if username == 'pi' and password == 'raspberry':
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def login_auth():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return '<p>User %s has been successfully logged in!</p>' % username
    else:
        return '<p>Login failed!</p>'

run(host='172.20.10.3', post=80) #post! not port!
