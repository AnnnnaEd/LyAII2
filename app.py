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
        algoritmo = request.form.get('algoritmo')  # Evitar KeyError
        if not algoritmo:
            return "El campo 'algoritmo' es obligatorio.", 400
    except ValueError:
        return "Los valores de 'estado_inicial' y 'solucion' deben ser números separados por comas.", 400

    resultado = []

    if algoritmo == 'DFS':
        # Resolver usando DFS
        visitados = []
        nodo_inicial = Nodo(estado_inicial)
        nodo = buscar_solucion_dfs_rec(nodo_inicial, solucion, visitados)

        # Reconstruir el camino desde la solución
        nodo_actual = nodo
        while nodo_actual.get_padre() is not None:
            resultado.append(nodo_actual.get_datos())  # Extraer datos del nodo
            nodo_actual = nodo_actual.get_padre()
        resultado.append(nodo_actual.get_datos())  # Añadir el nodo inicial
        resultado.reverse()

    elif algoritmo == 'Puzzle':
        # Resolver usando BFS del archivo Puzzle.py
        nodo = buscar_solucion_BFS(estado_inicial, solucion)
        if nodo:
            # Reconstruir el camino desde la solución
            nodo_actual = nodo
            while nodo_actual.get_padre() is not None:
                resultado.append(nodo_actual.get_datos())
                nodo_actual = nodo_actual.get_padre()
            resultado.append(nodo_actual.get_datos())  # Añadir el nodo inicial
            resultado.reverse()

    elif algoritmo == 'Puzzle1':
        # Resolver usando DFS del archivo Puzzle1.py
        nodo = buscar_solucion_DFS(estado_inicial, solucion)
        if nodo:
            # Reconstruir el camino desde la solución
            nodo_actual = nodo
            while nodo_actual.get_padre() is not None:
                resultado.append(nodo_actual.get_datos())
                nodo_actual = nodo_actual.get_padre()
            resultado.append(nodo_actual.get_datos())  # Añadir el nodo inicial
            resultado.reverse()

    return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)