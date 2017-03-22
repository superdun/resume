from flask import Flask,render_template,redirect,request

app = Flask(__name__)


@app.route('/')
def index():
    if request.args.has_key('source'):
        source = request.args['source']
        return redirect('en?source=%s'%source)
    else:
        return redirect('en')
@app.route('/en')
def englishIndex():
    source ='index'
    if request.args.has_key('source'):
        source = request.args['source']
    return render_template('%s/index.html'%source,source=source)

@app.route('/cn')
def chineseIndex():
    source = 'index'
    if request.args.has_key('source'):
        source = request.args['source']
    return render_template('%s/cnindex.html'%source,source=source)

@app.route('/project/<name>')
def porject(name):
    source = 'index'
    if request.args.has_key('source'):
        source = request.args['source']
    return render_template('%s/%s.html' % (source, name),source=source)
@app.route('/cnproject/<name>')
def chinesePorject(name):
    source = 'index'
    if request.args.has_key('source'):
        source = request.args['source']
    return render_template('%s/cn%s.html' % (source, name),source=source)
application=app

if __name__ == '__main__':
    app.run(port=8081)
