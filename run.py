from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.has_key('source'):
        source = request.args['source']
        return render_template('%s/index.html'%source,source=source)
    else:
        return render_template('index.html' )
@app.route('/cn')
def chineseIndex():
    if request.args.has_key('source'):
        source = request.args['source']
        return render_template('%s/cnindex.html'%source,source=source)
    else:
        return render_template('cnindex.html' )
@app.route('/project/<name>')
def porject(name):
    if request.args.has_key('source'):
        source = request.args['source']
        return render_template('%s/%s.html' % (source, name))
    else:
        return render_template('index.html' )
@app.route('/cnproject/<name>')
def chinesePorject(name):
    if request.args.has_key('source'):
        source = request.args['source']
        return render_template('%s/cn%s.html' % (source, name),source=source)
    else:
        return render_template('index.html' )
application=app

if __name__ == '__main__':
    app.run(port=8081)
