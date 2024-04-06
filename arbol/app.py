from flask import Flask, request, jsonify, render_template
from expresion_arbol import construir_arbol_expresion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar-arbol', methods=['POST'])
def generar_arbol():
    expresion = request.form['expresion']
    arbol_expresion = construir_arbol_expresion(expresion)
    arbol_json = arbol_a_json(arbol_expresion)
    return jsonify(arbol_json)

def arbol_a_json(nodo):
    if nodo is None:
        return None
    return {
        "valor": nodo.valor,
        "izquierda": arbol_a_json(nodo.izquierda),
        "derecha": arbol_a_json(nodo.derecha)
    }

if __name__ == '__main__':
    app.run(debug=True)
