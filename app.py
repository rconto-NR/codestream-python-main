import newrelic.agent
newrelic.agent.initialize('./newrelic.ini')

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, CodeStream!'

@app.route('/mathError')
def mathError():
    return 20/0

app.run(host='0.0.0.0', port=81)