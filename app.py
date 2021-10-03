from flask import Flask, render_template, request, make_response, redirect
from connector.Connector import Connector

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/router/<ip_address>")
def router(ip_address: str):
    connection = Connector(ip_address)
    return 'hello' + ip_address

@app.route("/router/validate_router", methods=["POST"])
def validate_router():
    ip = request.form['ip']
    return redirect(f"{ip}")


if __name__ == '__main__':
    app.run(port=8081, debug=True)
