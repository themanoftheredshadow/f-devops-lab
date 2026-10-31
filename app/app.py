from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>¡Hola desde mi contenedor Docker! 🚀</h1><p>Proyecto ASIR en marcha.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)