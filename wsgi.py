from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
