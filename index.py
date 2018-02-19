from bottle import route, error, template, static_file, run
import urllib.request, json
import os

with urllib.request.urlopen("http://apis.is/concerts") as url:
    gogn = json.loads(url.read().decode())

@route('/')
def index():
    return template('index.tpl', data=gogn)

run()


@error(404)
def error404(error):
    return template('error.tpl')

run(host='0.0.0.0', port=os.environ.get('PORT'))
