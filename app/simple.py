from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World! App for docker-compose"

if __name__ == '__main__':
    app.run()

