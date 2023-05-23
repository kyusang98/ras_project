from bottle import route, run, request, post


@route('/board') #/board?id=1&page=5
def display_board():
    board_id = request.query.id
    board_page = request.query.page or '1'
    return 'Board ID: %s (Page %s)'%(board_id,
board_page)

run(host='172.20.10.3', post=80) #post! not port!
