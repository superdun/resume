from flask import Flask,render_template,redirect,request,jsonify
import transModule
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

@app.route('/translation')
def translation():

    return render_template('translation/index.html')
@app.route('/api/translation',methods=["POST",])
def translationApi():
    text = request.form["text"]
    mode = request.form["mode"]
    trans = transModule.Translate()
    if mode =="e":
        result = {"status":"ok","msg":trans.translation_e(text)}
    else:
        result = {"status":"failed","msg":"no jap"}
    return jsonify(result)
application=app

if __name__ == '__main__':
    app.run(port=8081)
