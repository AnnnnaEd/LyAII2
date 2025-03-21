from flask import Flask, request, render_template
from Arbol import Nodo
from DFS_rec import buscar_solucion_dfs_rec
from Puzzle import buscar_solucion_BFS
from Puzzle1 import buscar_solucion_DFS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Procesar los datos del formulario
        estado_inicial = list(map(int, request.form['estado_inicial'].split(',')))
        solucion = list(map(int, request.form['solucion'].split(',')))
    except ValueError:
        return "Los valores de 'estado_inicial' y 'solucion' deben ser números separados por comas.", 400

    resultado = []

    # Intentar resolver con los tres métodos
    try:
        # Método DFS Recursivo
        visitados = []
        nodo_inicial = Nodo(estado_inicial)
        nodo = buscar_solucion_dfs_rec(nodo_inicial, solucion, visitados)
        if nodo:
            resultado.append(("DFS Recursivo", reconstruir_camino(nodo)))

        # Método BFS
        nodo = buscar_solucion_BFS(estado_inicial, solucion)
        if nodo:
            resultado.append(("BFS", reconstruir_camino(nodo)))

        # Método DFS Iterativo
        nodo = buscar_solucion_DFS(estado_inicial, solucion)
        if nodo:
            resultado.append(("DFS", reconstruir_camino(nodo)))

    except Exception as e:
        return f"Error al procesar la solución: {str(e)}", 500

    return render_template('index.html', resultado=resultado)

def reconstruir_camino(nodo):
    """Reconstruye el camino desde el nodo solución hasta el nodo inicial."""
    camino = []
    while nodo:
        camino.append(nodo.get_datos())
        nodo = nodo.get_padre()
    return list(reversed(camino))

if __name__ == '__main__':
    app.run(debug=True)
