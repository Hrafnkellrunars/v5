from bottle import route, error, template, static_file, run
import urllib.request, json

with urllib.request.urlopen("http://apis.is/concerts") as url:
    gogn = json.loads(url.read().decode())

@route('/')
def index():
    return template('static/templates/index.tpl', data=gogn)

run()


@error(404)
def error404(error):
    return template('static/templates/error.tpl')

run(host='localhost', port=8080, debug=True)