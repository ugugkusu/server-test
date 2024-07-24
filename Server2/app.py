from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    client_ip = request.remote_addr
    return "Server 2'den selamlar. Burası 'index' sayfası. Sen bu {} IP Adresine sahipsin".format(client_ip)

@app.route('/example-endpoint')
def example_endpoint():
    client_ip = request.remote_addr
    return "Server 2'den selamlar. Burası 'example-endpoint' sayfası. Sen bu {} IP Adresine sahipsin".format(client_ip)

@app.route("/health-check")
def health_check():
    client_ip = request.remote_addr
    return "OK {}".format(client_ip), 200