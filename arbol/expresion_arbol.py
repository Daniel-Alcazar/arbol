class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def construir_arbol_expresion(expresion):
    # Implementa la lógica para construir el árbol de expresión aquí
    pass

def imprimir_arbol_expresion(nodo):
    if nodo is None:
        return ""

    # Recorrer recursivamente los nodos del árbol
    html = f'<div class="node">{nodo.valor}</div>'
    html += '<div class="ramas">'
    html += imprimir_arbol_expresion(nodo.izquierda)
    html += '<div class="line"></div>'
    html += imprimir_arbol_expresion(nodo.derecha)
    html += '</div>'

    return html
