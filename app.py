from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Muestra el ID del contenedor para verificar el balanceo de carga
    container_id = os.uname()[1]
    return f"Hello word: Carlos Paul Giraldo Palacios {container_id}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)