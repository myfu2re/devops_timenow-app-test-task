from flask import Flask
from datetime import datetime

app = Flask(__name__)  

@app.route('/api')
def time():
    now = datetime.now()
    responseBody = now.strftime("%H:%M:%S")
    return responseBody

# uncomment to modify response headers for all requests
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app.run(debug=True, port=8080, host="0.0.0.0")

#if __name__ == "__main__":

#    app.run(ssl_context=("nginx-selfsigned.crt", "nginx-selfsigned.key"), debug=True, port=8080, host="0.0.0.0")

#app.run(ssl_context=('nginx-selfsigned.crt', 'nginx-selfsigned.key'))

#app.run(ssl_context=('nginx-selfsigned.crt', 'nginx-selfsigned.key'), debug=True, port=8080, host="0.0.0.0")
