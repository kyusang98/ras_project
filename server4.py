from bottle import route, run, request, post
import base64

@route('/')
@route('/login')
def login():
    return '''
       <form action='/login' method='post'>
            StudentID: <input name='studentid' type='text' />
            Password: <input name='password' type='password' />
            PhoneNumber: <input name='phonenum' type='text' />
            <input value='Login' type='submit' />
       </form>
           '''
def check_login(studentid, password):
    if studentid == '2018732006' and password == 'raspberry':
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def login_auth():
    studentid = request.forms.get('studentid')
    password = request.forms.get('password')
    phonenum = request.forms.get('phonenum')
    password_bytes = password.encode('ascii')
    password_base64 = base64.b64encode(password_bytes)
    if check_login(studentid, password):
        return '''
           <p>Student_ID:%s has been successfully logged in!
              Password:%s
              PhoneNumber:%s
           </p>

               ''' % (studentid ,password_base64 ,phonenum)
    else:
        return '<p>Login failed!</p>'

run(host='172.20.10.3', post=80) #post! not port!
