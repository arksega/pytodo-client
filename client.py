from flask import Flask, render_template
import httplib
import json

app = Flask(__name__)

@app.route('/')
def get(name=None):
    conn = httplib.HTTPConnection("localhost", 8080)
    conn.request('get', '/')
    response = conn.getresponse()
    data = response.read()
    data = json.loads(data)
    return render_template('todo.html',tasks=data)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

# vim: sw=4 sts=4 si et
