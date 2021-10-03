from flask import Flask

app = Flask(__name__)


@app.route('/router')
def hello_world():
    return 'Hello World!'

@app.route("/router/<ip_address>")
def router(ip_address: str):
    return 'hello' + ip_address



if __name__ == '__main__':
    app.run(port=8081, debug=True)
